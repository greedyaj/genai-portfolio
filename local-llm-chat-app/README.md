# Chat with AI Models Using Streamlit and Ollama

This repository contains the code for a chat application that leverages Streamlit and the Ollama language model (LLM) to interact with users in real-time. This application allows users to select different AI models and receive instant responses to their queries.

## Features

- Real-time chat interface using Streamlit.
- Integration with Ollama LLM for generating responses.
- Model selection from the sidebar (supports Llama3, Phi3, and Mistral7b).
- Logging for debugging and monitoring.

## Installation

### Prerequisites

- Python >=3.7
- Streamlit
- Ollama

If running the app on macOS requires:
- llama-index-llms-ollama

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/greedyaj/genai-portfolio
   cd genai-portfolio/local-llm-chat-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   streamlit run ollama-streamlit-app.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Select a model from the sidebar (`Llama3`, `Phi4`, `Mistral`).
3. Enter your question in the chat input box and press Enter.
4. View the model's response in real-time.

## License

This project is open-sourced. 

## Acknowledgements

This project uses the following libraries:
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)

Feel free to reach out if you have any questions or need further assistance. Happy coding!
