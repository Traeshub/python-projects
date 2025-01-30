
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2")

result = model.invoke(input="hellow world")
print(result)

#When virtual env is ran correctly it will execute the script and interact w the AI bot

#Run Ollama Locally: "Ollama run llama3.2"