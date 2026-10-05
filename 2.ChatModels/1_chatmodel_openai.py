from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(model="gpt-4", temperature=0.8, max_completion_tokens=10)
#temprature controls the randomness and creativity of the answers
#max_token tells the tokens/words in the output
result=llm.invoke("what is the capital of india??")
print(result.content)
