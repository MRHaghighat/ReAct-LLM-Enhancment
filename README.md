# ReAct-LLM-Enhancment
ReAct-LLM-Enhancment is a project focused on generating updated results from Language Models (LLMs) using a reasoning-based approach combined with action-taking capabilities. The project aims to improve the integration of reasoning and acting components within LLMs to enhance language understanding and interactive decision making.

## Overview

ReAct-LLM-Update-Information is a project focused on enhancing language understanding and interactive decision making by seamlessly integrating reasoning and acting capabilities within Large Language Models (LLMs). The project aims to improve the model's ability to generate reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between reasoning and acting components.

## Abstract

While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g., chain-of-thought prompting) and acting (e.g., action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. For more details, you can read the full paper [here](https://react-lm.github.io/).

## Installation

To set up the project, follow these installation steps:

    ```bash
    pip install -r requirements.txt


## Usage
To use the project, run the `Streamlit` app and input your question to generate an updated result from the Language Model:

    ```bash
    streamlit run app.py

## Configuration
For configuration settings, refer to the code and update the environment variables for your `OpenAI` and SERPER API keys:

    ```bash
    os.environ["OPENAI_API_KEY"] = "<YOUR-OPENAI-API-KEY>"
    os.environ["SERPER_API_KEY"] = "<YOUR-SERPER-API-KEY>"

## License
This project is licensed under the MIT License.

## Acknowledgements
We would like to acknowledge the following for their contributions and inspiration to this project:

> `OpenAI` for their Language Models
> `SERPER` for their APIs
> Contributors of the `langchain` and `streamlit` libraries

