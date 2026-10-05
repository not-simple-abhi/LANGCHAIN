from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.8-flash")
result=model.invoke("what is the capital of india?")
print(result.content)

# gemini-3.8-flash returns content as a list of dicts, extract text from it
if isinstance(result.content, list):
    print(result.content[0]['text'])
else:
    print(result.content)
