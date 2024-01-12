# Imports
import os, re, openai, cohere
from googletrans import Translator

# API Keys Section

# Getting API Key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = input('Enter OpenAI API Key : ')

# Getting Cohere API Key from .env
cohere_key = os.getenv("COHERE_API_KEY")
# cohere_key = input('Enter Cohere API Key : ')

# Take Input Paragraph
def take_input_essay(input_essay):
  # Using filter to remove empty strings
  input_essay = input_essay.split('\n')
  processed_paragraph = list(filter(lambda x: x != '', input_essay))
  processed_paragraph = "\n".join(processed_paragraph)
  return processed_paragraph

#@title Metrics of Processed Paragraph
def metrics_of_processed_essay(processed_paragraph):
  no_of_words = len(processed_paragraph.split())
  total_digits = len(re.findall('[0-9]',processed_paragraph))
  total_letters = len(re.findall('[A-z]', processed_paragraph))
  print("Total words found :-", no_of_words)
  print("Total letters found :-", total_letters)
  print("Total digits found :-", total_digits)
  return no_of_words, total_letters, total_digits

# Summary Functions

# ChatGPT Related

# Prompt Summarise Function
def chatgpt_prompt_summarize_document(document):
  if(openai.api_key != None):
    no_of_words, total_letters, total_digits = metrics_of_processed_essay(document)
    prompt = f"You are great at summarizing the document I give as input to you. You need to summarize the document without loss of information. Summarize the following document in {no_of_words/3} words:\n\n" + document + "\n\nSummary:"
    prompt_response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1000,  # Adjust the length of the summary as per your needs
        temperature=0.3,  # Controls the randomness of the generated text
        n = 1,  # Set to 1 for a single summary
        stop = None,  # Specify a stop sequence if needed to end the summary
    )

    prompt_summary = prompt_response.choices[0].text.strip()
    no_of_words, total_letters, total_digits = metrics_of_processed_essay(prompt_summary) # Summary Metrics
    return prompt_summary, [no_of_words, total_letters, total_digits]
  else:
    return cohere_summarize_document(document=document)

# Chat Summarise Function
def chatgpt_chat_summarize_document(document):
  no_of_words, total_letters, total_digits = metrics_of_processed_essay(document)
  chat_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are great at summarizing the document I give as input to you. You need to summarize the document without loss of information."
    },
    {
      "role": "user",
      "content": "Summarize the following document in " + (no_of_words/3) + " words:\n\n" + document + "\n\nSummary:"
    }
  ],
  max_tokens = 1024,
  top_p=1,
  n=1,
  frequency_penalty=0,
  presence_penalty=0
  )

  chat_summary = chat_response.choices[0].text.strip()
  no_of_words, total_letters, total_digits = metrics_of_processed_essay(chat_summary) # Summary Metrics
  return chat_summary, [no_of_words, total_letters, total_digits]
  

# Cohere Related

# Cohere Summarise Function
def cohere_summarize_document(document):
  co = cohere.Client(cohere_key)
  response = co.summarize(
    text=document,
    length='long',
    format='paragraph',
    model='summarize-xlarge',
    # additional_command='focus on entire document',
    temperature=0.3,
  )
  no_of_words, total_letters, total_digits = metrics_of_processed_essay(response.summary) # Summary Metrics
  return response.summary, [no_of_words, total_letters, total_digits] 

def translate_to_another_language(document, language='fr'):
  translator = Translator()
  return translator.translate(document, dest=language)

"""
Conclusions

- The Summary that ChatGPT is better than the summary that Cohere has given. Cohere gives a good summary but inconsistent in giving a clean summary.

"""