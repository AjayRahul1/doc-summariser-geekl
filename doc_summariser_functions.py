# Imports
import os, re, openai, cohere

# API Keys Section

# Getting API Key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
# Getting Cohere API Key from .env
cohere_key = os.getenv("COHERE_API_KEY")

# Take Input Paragraph
def preprocess_document(input_essay: str):
  """
  Preprocesses the document by removing unnecessary new lines.

  Paramters:
  """
  input_essay = input_essay.split('\n')
  # Using filter to remove empty strings
  processed_paragraph = list(filter(lambda x: x != '', input_essay))
  processed_paragraph = "\n".join(processed_paragraph)
  return processed_paragraph

def document_text_metrics(document: str) -> tuple[int]:
  """
  Metrics of document

  Find Metrics of a input document provided such as the Word Count, Letter Count, Digit Count.

  Parameters:
  ---
  document : str
    The document text

  Returns:
  ---
  tuple[int]
    wordCount, letterCount, digitCount in their respective indices.
  """
  wordCount: int = len(document.split())
  digitCount: int = len(re.findall('[0-9]',document))
  letterCount: int = len(re.findall('[A-z]', document))
  print("Total words found :-", wordCount)
  print("Total letters found :-", letterCount)
  print("Total digits found :-", digitCount)
  return (wordCount, letterCount, digitCount)

# Summary Functions

def summarize_document(document: str):
  return chatgpt_prompt_summarize_document(document) if(openai.api_key != None) else cohere_summarize_document(document=document)

# ChatGPT Related

# Prompt Summarise Function
def chatgpt_prompt_summarize_document(document: str) -> tuple[str, tuple[int]]:
  """
  Summarize using a prompt

  This makes use of engineered prompt to let the `text-davinci-003` model Summarize Prompt API.
  This works only when you have an OpenAI API Key and there are tokens left for the key.
  
  Parameters:
  ---
  document : str
    The document text that need to be summarized.

  Returns:
  ---
  tuple[str, tuple[int]]
    A tuple containing a summary string as its first element and a tuple of three integers (metrics of the summary) as its second element.
  """

  wordCount, _, _ = document_text_metrics(document)
  prompt = f"You are great at summarizing the document I give as input to you. You need to summarize the document without loss of information. Summarize the following document in {wordCount/3} words:\n\n{document}\n\nSummary:"
  prompt_response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 1000,  # Adjust the length of the summary as per your needs
    temperature=0.3,  # Controls the randomness of the generated text
    n = 1,  # Set to 1 for a single summary
    stop = None,  # Specify a stop sequence if needed to end the summary
  )

  prompt_summary = prompt_response.choices[0].text.strip()
  return (prompt_summary, document_text_metrics(prompt_summary))

# Chat Summarise Function
def chatgpt_chat_summarize_document(document: str) -> tuple[str, tuple[int]]:
  """
  Summarize using a chat model gpt-3.5-turbo

  This makes use of engineered prompt to let the `text-davinci-003` model Summarize Prompt API.
  This works only when you have an OpenAI API Key and there are tokens left for the key.
  
  Parameters:
  ---
  document : str
    The document text that need to be summarized.

  Returns:
  ---
  tuple[str, tuple[int]]
    A tuple containing a summary string as its first element and a tuple of three integers (metrics of the summary) as its second element.
  """
  no_of_words, _, _ = document_text_metrics(document)
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
  return (chat_summary, document_text_metrics(chat_summary))

# Cohere Summarise Function
def cohere_summarize_document(document: str) -> tuple[str, tuple[int]]:
  """
  Summarize using a summarize-x-large that belongs to Co.summarize API of Cohere.

  This makes use of the Summarize API of Cohere that takes document text and other parameters. 
  This works only when you have an Cohere API Key.
  
  Parameters:
  ---
  document : str
    The document text that need to be summarized.

  Returns:
  ---
  tuple[str, tuple[int]]
    A tuple containing a summary string as its first element and a tuple of three integers (metrics of the summary) as its second element.
  """

  co = cohere.Client(cohere_key)
  response = co.summarize(
    text=document,
    length='long',
    format='paragraph',
    model='summarize-xlarge',
    temperature=0.3,
    additional_command='Take the context in entire document till the end.',
  )
  return (response.summary, document_text_metrics(response.summary))

"""
Conclusion:
---
The Summary that ChatGPT is better than the summary that Cohere has given. Cohere gives a good summary but inconsistent in giving a good one.
"""