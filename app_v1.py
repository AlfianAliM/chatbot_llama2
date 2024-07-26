import streamlit as st
import replicate
import os
from googlesearch import search

# App title
st.set_page_config(page_title="Ask Anything")

# Enter API token
replicate_api = "YOUR_API_TOKEN"
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Replicate Credentials
with st.sidebar:
    st.title('Ask Anything')

# Additional Data Input Tab
data_input = st.sidebar.text_area("Additional Data", "", height=200)

# Language Selection
output_language = "English"  # Set the output language to English only

# Function to perform Google search
def perform_google_search(query):
    results = []
    for j in search(query):  # Perform the search without num argument
        results.append(j)
        if len(results) >= 5:  # Limit results to the first 5
            break
    return results

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How can I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How can I assist you today?"}]
st.sidebar.button('Clear history', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input, additional_data, file_data, output_lang):
    string_dialogue = f"You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    string_dialogue += f"\n\nAdditional Data from file:\n{file_data}\n\n"
    string_dialogue += f"Additional Data from input:\n{additional_data}\n\n"
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    
    string_dialogue += f"Please respond in {output_lang}."
    
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature": 0.1, "top_p": 0.9, "repetition_penalty": 1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            search_results = perform_google_search(prompt)
            data_from_search = "\n".join(search_results)  # Combine search results into a string
            response = generate_llama2_response(prompt, data_input, data_from_search, output_language)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
