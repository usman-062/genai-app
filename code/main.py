import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 

load_dotenv() # Read .env file 
llm = init_chat_model(
    model=os.getenv("MODEL_Name"),
    temperature=os.getenv(key="TEMPERATURE")
)

response = llm.invoke(input="Hi")
print(response.text)