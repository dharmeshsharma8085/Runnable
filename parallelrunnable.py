from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel ,  RunnableLambda
model = ChatMistralAI( model = "mistral-small-2506")
parser = StrOutputParser()

short_prompts = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detaled_prompts = ChatPromptTemplate.from_template(
    "Explain {topic} in detail "
)

topic = "Deep Learning"

chain = RunnableParallel({
"Short" :RunnableLambda(lambda x : x ["Short"]) |  short_prompts | model | parser,

"Detailded" :RunnableLambda(lambda x : x ["Detailed"]) | detaled_prompts | model | parser
})


result = chain.invoke({
    "Short" : {"topic" : "Deep learning"},
    "Detailed" : {"topic" : "LLM"}
    })

print(result)