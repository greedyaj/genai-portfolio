import streamlit as st
from llama_index.core.llms import ChatMessage
from llama_index.llms.ollama import Ollama
import logging
import time

logging.basicConfig(level=logging.INFO)

if 'messages' not in st.session_state:
    st.session_state.messages = []

def stream_chat(model, messages):   
    try:
        llm = Ollama(model=model, request_timeout=120.0)
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
 
        # Stream the response
        for chunk in resp:
            response += chunk.delta
            response_placeholder.write(response)
        
        logging.info(f"Model: {model}, Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error during streaming: {e}")
        raise e

def main():
    st.title("Ollama Streamlit App")
    logging.info("Ollama Streamlit App started")

    model = st.sidebar.selectbox("Choose a model", ["llama3", "phi4", "mistral"])
    logging.info(f"Selected model: {model}")

    if prompt := st.chat_input("Enter your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        logging.info(f"User message: {prompt}")

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                start_time = time.time()
                logging.info(f"Starting streaming for model: {model}")

                with st.spinner("Generating..."):
                    try:
                        messages = [ChatMessage(role=msg["role"], content=msg["content"]) for msg in st.session_state.messages]
                        response_message = stream_chat(model, messages)
                        duration = time.time() - start_time

                        response_message_with_duration = f"{response_message} (took {duration:.2f} seconds)"
                        st.session_state.messages.append({"role": "assistant", "content": response_message_with_duration})
                        st.write(response_message_with_duration)
                        logging.info(f"Assistant response: {response_message_with_duration}")
                    except Exception as e:
                        st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})
                        st.error(f"An Error occurred while generating response: {e}")
                        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()