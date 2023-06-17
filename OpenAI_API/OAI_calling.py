import os
import openai
openai.organization = "org-uIoNOrZkKMd0w2hOoyl8x6N6"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()