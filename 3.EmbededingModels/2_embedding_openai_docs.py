from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents=[
    "Delhi is captial of india",
    "kolakata in west bengal",
    "paris is in france"
]

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
#dimension more then cost will also be more
result=embedding.embed_documents(documents)
print(str(result))