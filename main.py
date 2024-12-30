import streamlit as st
import random
import time


LIST_OF_WORDS = [
    'Pru.',
    'Pruuu!',
    'Pru, pru, pru.',
    'Pru, pr...',
    'Cruuu',
    'Cruu, cruu',
    '*Arrulhando*',
    '*Arrolando*',
    '...',
    '🍿',
    '💩',
    '💩',
    '💩💩💩',
    '🕊️',
    ''
]


# Streamed response emulator
def response_generator():
    response = random.choice(LIST_OF_WORDS)
        
    for word in response.split():
        yield word + " "
        time.sleep(0.15)


st.set_page_config(
    page_title="Bem-vindo ao PomboGPT",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Bem-vindo... pruu... ao PomboGPT")

with st.sidebar:
    st.image('logo.png')
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = "🕊️" if message["role"] == "pigeon" else None
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Pruu?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
     # Display assistant response in chat message container
    with st.chat_message("pigeon", avatar="🕊️"):
        response = st.write_stream(response_generator())
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "pigeon", "content": response})
