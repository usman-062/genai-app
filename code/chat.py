import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv() # Read .env file 

model_name = os.getenv("MODEL_Name")
if not model_name:
    raise SystemError("MODEL_Name is not set in the .env file.")
llm = init_chat_model(
    model=os.getenv("MODEL_Name"),
    temperature=os.getenv(key="TEMPERATURE"),
    api_key=os.getenv("API_KEY")
)



SYSTEM_PROMPT = "You are a helpful assistant."

history = [
    {"role": "system","content":SYSTEM_PROMPT}
    ]

# question = input("you: ")
# response = llm.invoke(question)
# print(f"Bot: {response.text}")

print("Welcome to Cue chat!")

while True:
    try:
        question = input("you: ").strip()

    except (KeyboardInterrupt,EOFError):
        print("\n Goodbye!")
        break

    if not question:
        print("Please enter a question.")
        continue
    if question.lower() in ["exit", "quit", "bye"]:
        print("Exiting the chat. Goodbye!")
        break

    history.append({"role": "user", "content": question})
    print("Bot: ", end="", flush=True)
    # response = llm.invoke(history) # invoke always return ai meassage
   
    full = None # None | Ai Mesagechhunk
    for chunk in llm.stream(history):
        print(chunk.text, end="", flush=True)
        full=chunk if full is None else full + chunk
    print()    


    history.append(full.text)

    # print(f"Bot: {full.text}") 