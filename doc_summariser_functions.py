# Imports
import os, re, openai, cohere

# API Keys Section

# Getting API Key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
# Getting Cohere API Key from .env
cohere_key = os.getenv("COHERE_API_KEY")

# Take Input Paragraph
def take_input_essay(input_essay: str):
  # Using filter to remove empty strings
  input_essay = input_essay.split('\n')
  processed_paragraph = list(filter(lambda x: x != '', input_essay))
  processed_paragraph = "\n".join(processed_paragraph)
  return processed_paragraph

def document_text_metrics(document: str):
  """
  Find Metrics of a 
  """
  no_of_words: int = len(document.split())
  total_digits: int = len(re.findall('[0-9]',document))
  total_letters: int = len(re.findall('[A-z]', document))
  print("Total words found :-", no_of_words)
  print("Total letters found :-", total_letters)
  print("Total digits found :-", total_digits)
  return no_of_words, total_letters, total_digits

# Summary Functions

# ChatGPT Related

# Prompt Summarise Function
def chatgpt_prompt_summarize_document(document: str) -> tuple[str, list[int]]:
  if(openai.api_key != None):
    no_of_words, total_letters, total_digits = document_text_metrics(document)
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
    no_of_words, total_letters, total_digits = document_text_metrics(prompt_summary) # Summary Metrics
    return prompt_summary, [no_of_words, total_letters, total_digits]
  else:
    return cohere_summarize_document(document=document)

# Chat Summarise Function
def chatgpt_chat_summarize_document(document: str) -> tuple[str, list[int]]:
  no_of_words, total_letters, total_digits = document_text_metrics(document)
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
  no_of_words, total_letters, total_digits = document_text_metrics(chat_summary) # Summary Metrics
  return chat_summary, [no_of_words, total_letters, total_digits]
  

# Cohere Related

# Cohere Summarise Function
def cohere_summarize_document(document: str) -> tuple[str, list[int]]:
  co = cohere.Client(cohere_key)
  response = co.summarize(
    text=document,
    length='long',
    format='paragraph',
    model='summarize-xlarge',
    # additional_command='focus on entire document',
    temperature=0.3,
  )
  no_of_words, total_letters, total_digits = document_text_metrics(response.summary) # Summary Metrics
  return response.summary, [no_of_words, total_letters, total_digits] 

"""
Conclusions

- The Summary that ChatGPT is better than the summary that Cohere has given. Cohere gives a good summary but inconsistent in giving a clean summary.

"""