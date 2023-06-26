# Databricks notebook source
# MAGIC %pip install openai

# COMMAND ----------

# MAGIC %pip install python-dotenv

# COMMAND ----------

# MAGIC %run "./Meeting_Notes"

# COMMAND ----------

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = 'OPEN-AI-KEYS'
# openai.api_key  = os.getenv('OPEN-AI-KEYS')

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

def get_keynotes_from_meeting(meetingNotes):
  prompt = prompt = f"""Summarize the text \
that is delimited by triple backticks 
into key points.
text: ```{meetingNotes}```
"""
  return get_completion(prompt)

# COMMAND ----------

prompt = f"""Summarize the meeting transcripts \
that is delimited by triple backticks 
into key points. Those key points could be actionable next steps in timely order. If there are time and location related to a key point, also show them in the summary.
text: ```{meetingNotes}```
"""

# COMMAND ----------

# Meeting of CTAS County Commission-Transcript of Dialogue
CTAS_summary = get_keynotes_from_meeting(CTAS_meeting)
print(CTAS_summary)

# COMMAND ----------

# Dialogue from huggingface
ami_summary = get_keynotes_from_meeting(ami_meeting)
print(ami_summary)

# COMMAND ----------


