# Random Fact Joke Generator
## Demo Video

To see the Random Fact Joke Generator in action, check out our demo video:

![Random Fact Joke Generator Demo](https://github.com/MAdhavbhatia222/llm_projects/blob/main/Joke_Generator/Fact_Joke__Project.gif)


- **Live Demo:** [www.factsdrive.net](http://www.factsdrive.net)

Welcome to the Random Fact Joke Generator project! This fun and engaging web application serves up jokes based on random facts, combining humor with the power of Large Language Models (LLMs).

## Project Overview

Madness begins with LLMs for us! Dive into a delightful mix of technology and humor with our Random Fact Joke Generator. 
No need for fancy models; our project thrives on the simplicity and efficiency of `llama.cpp` and the vicuna model, powered by an unassuming CPU-based Ubuntu server.

### Features

- **Fact-based Joke Generation:** Enjoy a fresh joke with every click, generated from random facts.
- **Simple and Responsive UI:** Built with HTML, CSS, and JavaScript, ensuring a smooth user experience.
- **Powered by LLMs:** Utilizes custom models without relying on GPT-4, maintaining both uniqueness and performance.

### Technology Stack

- **Server:** Ubuntu
- **Backend:** Python Flask
- **Frontend:** HTML, CSS, JavaScript
- **Models:** [vicuna 7B quantized model](https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF/blob/main/vicuna-7b-v1.5.Q4_K_S.gguf)
- **Hosting:** The Oracle Cloud
- **Utilities:** text-generation-webui for a rich feature set and easy model switching

## Getting Started

### Prerequisites

Ensure you have Python and Flask installed on your system. Our setup runs on an Ubuntu server, but it should be compatible with other environments that support Python.

### Installation

1. Clone these repository to your local machine.
    - [Text generation web UI](https://github.com/oobabooga/text-generation-webui)
    - [LLM_project_Joke_Generator](https://github.com/MAdhavbhatia222/llm_projects/Joke_Generator)
2. Navigate to the project directory.
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```

Your Random Fact Joke Generator is now running! Access it via `http://localhost:9696` in your browser.

### Usage

1. **A Random Fact:** Click on "Show me a fact" to fetch a random fact.
2. **Joke Generation:** After a fact is displayed, click on "Generate Joke on fact" to see a joke based on the fact presented.

## Project Structure

- `app.py`: The Flask server script.
- `templates/`: Contains the HTML files for the web UI.
  - `index.html`: The main webpage of the application.

## Contributions

Feel free to fork the project, submit pull requests, or suggest features by opening an issue. We're excited to see how you can replicate this project!

## Acknowledgments

- Special thanks to text-generation-webui for their platform.

## Stay Connected

- **GitHub Repository :** [Text generation web UI](https://github.com/oobabooga/text-generation-webui)


Enjoy generating jokes, and don't forget to share the laughter! For any queries or suggestions, reach out through our GitHub repository.

---

This draft aligns with the details you've shared. Feel free to adjust or provide additional information if you'd like any modifications.
