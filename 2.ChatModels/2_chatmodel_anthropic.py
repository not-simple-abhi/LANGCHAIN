from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

llm=ChatAnthropic(model="claude-3-5-sonnet-20241022")

result=llm.invoke("what is the capital of india??")

print(result.content)