import streamlit as st
import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

# Set OpenAI and SERPER API keys
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "8631659495e9df4ad17a9e0e2687f84197af5227"

# Initializing a ChatOpenAI instance with the specified model and temperature
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Loading tools for the agent, including "google-serper" and "llm-math"
tools = load_tools(["google-serper", "llm-math"], llm=llm)

# Initializing an agent using the loaded tools, language model (llm), and agent type ("zero-shot-react-description")
# Setting verbose=True for verbose output during initialization
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Streamlit interface
st.title("ReAct LLM Update Information")

# User input for the question
user_question = st.text_input("Enter your question:", "What is the best stock portfolio in 2023 September?")

# Generate answer when user clicks the "Generate Answer" button
if st.button("Generate Answer"):
    answer = agent.run(user_question)
    st.write("Answer:")
    st.write(answer)
