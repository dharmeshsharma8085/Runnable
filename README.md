
# 🔗 LangChain Runnable

A hands-on project to understand **LangChain Runnables** and how different LLM components can be connected together to create simple and reusable AI pipelines.

This project demonstrates how **Prompt Templates, Chat Models, and Output Parsers** can be composed using LangChain's Runnable interface and the `|` operator.

---

## 📌 Overview

LangChain Runnables provide a standard way to connect different components of an LLM application into a single pipeline.

Instead of manually executing each step:

```python
prompt_output = prompt.invoke(...)
model_output = model.invoke(prompt_output)
final_output = parser.invoke(model_output)
````

LangChain allows us to compose them together:

```python
chain = prompt | model | parser
```

And execute the complete workflow with:

```python
result = chain.invoke("Machine Learning")
```

---

## ⚙️ Pipeline

The project follows this simple workflow:

```text
User Input
    ↓
ChatPromptTemplate
    ↓
Mistral AI Model
    ↓
StrOutputParser
    ↓
Final Response
```

Each component performs a specific task:

* **ChatPromptTemplate** → Creates the prompt
* **ChatMistralAI** → Sends the prompt to the Mistral LLM
* **StrOutputParser** → Converts the model response into a string
* **Runnable Chain** → Connects all components together

---

## 🛠️ Technologies Used

* Python
* LangChain
* LangChain Core
* Mistral AI
* python-dotenv

---

## 📂 Project Structure

```text
Runnable/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## 💻 Implementation

```python
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# Model
model = ChatMistralAI(
    model="mistral-small-2506"
)

# Output Parser
parser = StrOutputParser()

# Runnable Chain
chain = prompt | model | parser

# Invoke the chain
result = chain.invoke("Machine Learning")

print(result)
```

---

## 🧠 Key Concepts Learned

### 1. Runnable Composition

Multiple LangChain components can be connected using the pipe operator:

```python
prompt | model | parser
```

The output of one component automatically becomes the input of the next component.

### 2. `invoke()`

The complete chain can be executed using:

```python
chain.invoke(...)
```

This allows the entire pipeline to be executed through a single method call.

### 3. Output Parsing

`StrOutputParser` converts the model's response into a clean Python string that can easily be displayed or further processed.

---

## 🚀 Why Runnables?

Runnables make LLM applications:

* Cleaner
* More modular
* Easier to maintain
* Easier to extend
* Easier to combine into larger pipelines

The same concept can later be used to build more advanced applications such as **RAG systems, retrieval pipelines, structured-output workflows, and AI agents**.

---

## 🎯 Learning Goal

The goal of this project was to understand the fundamentals of **LangChain Runnable / LCEL-style composition** and how individual LLM components can be combined into a complete workflow.

---

## 🔮 Next Steps

After understanding Runnable fundamentals, the next concepts to explore are:

* LCEL
* RunnableLambda
* RunnablePassthrough
* RunnableParallel
* RAG Pipelines
* Retrievers
* Structured Output
* Agents

---

## 👨‍💻 Author

**Dharmesh Sharma**

AI Engineering | Machine Learning | Generative AI

GitHub: [dharmeshsharma8085](https://github.com/dharmeshsharma8085)

---

⭐ This repository is part of my journey toward becoming an **AI Engineer**.

```
```
