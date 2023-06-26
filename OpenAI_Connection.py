# Databricks notebook source
# MAGIC %pip install openai

# COMMAND ----------

# MAGIC %pip install python-dotenv

# COMMAND ----------

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = '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'
# openai.api_key  = os.getenv('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')

# COMMAND ----------

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]


# COMMAND ----------

get_completion("What is 1+1?")

# COMMAND ----------


