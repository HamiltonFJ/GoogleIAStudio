# -*- coding: utf-8 -*-
"""GA.AI - PrjAula4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A90SwEoxpHfAEOILTry1ZSPkxxFw_8iK

Instalando o SDK Google
"""

!pip install -qU google-generativeai

# Import the Python SDK
import google.generativeai as genai

# Replace with your API key
GOOGLE_API_KEY = "AIzaSyB7EeYVs_HOlxyTfrYwlyYsZiTUslQz11Y"

# Configure the API key
genai.configure(api_key=GOOGLE_API_KEY)

"""Listar os Modelos disponíveis"""

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

"""Configurações: Nº respostas,Temperatura, Safety  """

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}

safety_settings = {
  "HARASSMENT": "BLOCK_NONE",
  "HATE": "BLOCK_NONE",
  "SEXUAL": "BLOCK_NONE",
  "DANGEROUS": "BLOCK_NONE"
}

"""Inicializar o modelo"""

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

response = model.generate_content("Vamos aprender conteúdo sobre IA. Me dê sugestões.")
print(response.text)

"""Armazena o histórico do chat"""

varchat = model.start_chat(history=[])

"""Exibir o histórico (Config.Estética)"""

import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  """Helper function to format text to markdown"""
  text = text.replace("`", "'")
  return Markdown(textwrap.indent(text, "  > "))

# print histórico
for message in varchat.history:
  display(to_markdown(f"**{message.role}:** {message.parts[0].text}"))
print("---------------------------------------------------------")

"""Executa o prompt enquanto a resposta não for "fim"
"""

import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  """Helper function to format text to markdown"""
  text = text.replace("`", "'")
  return Markdown(textwrap.indent(text, "  > "))

varchat = model.start_chat(history=[])  # Assumindo que você já iniciou o chat

while True:
    prompt = input("Prompt: ")
    if prompt == "fim":
        break

    response = varchat.send_message(prompt)

    # Formatação Markdown - Saída
    display(to_markdown(f"**Você:** {prompt}"))
    display(to_markdown(f"**Gemini:** {response.text}"))

    print("-------------------------------------------------------------------")