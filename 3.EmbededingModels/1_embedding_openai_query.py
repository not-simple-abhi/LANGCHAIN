from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
#dimension more then cost will also be more
result=embedding.embed_query("Delhi is the capital of india")
print(str(result))