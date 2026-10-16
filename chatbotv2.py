import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load API keys
load_dotenv()

DEVELOPER_NAME = "Jashwanthi.K"

# 2. Page Configuration
st.set_page_config(
    page_title="Chatbot J",
    page_icon="🤖",
    layout="centered"
)

# 3. Track state
if "conversation_started" not in st.session_state:
    st.session_state.conversation_started = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==========================================
# SCREEN 1: WELCOME PAGE (Brick Red & Wine)
# ==========================================
if not st.session_state.conversation_started:
    st.markdown(
        """
        <style>
        /* Welcome screen background: Brick Red #8B2218 */
        [data-testid="stAppViewContainer"] {
            background-color: #8B2218;
            color: #FFFFFF;
        }
        [data-testid="stHeader"] {
            background-color: transparent;
        }
        h1, h2, h3, p, span, div {
            color: #FFFFFF !important;
        }
        /* Start Button: Deep Wine #3B0702 with Ruby #770F05 hover */
        div.stButton > button {
            background-color: #3B0702 !important;
            color: #FFFFFF !important;
            border: 1px solid #9E3A31 !important;
            border-radius: 10px !important;
            font-size: 17px !important;
            font-weight: 600 !important;
            padding: 12px 24px !important;
            transition: all 0.25s ease-in-out !important;
        }
        div.stButton > button:hover {
            background-color: #770F05 !important;
            border-color: #FFFFFF !important;
            transform: scale(1.02);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("👋 Welcome!")
    st.header(f"Hi, I am {DEVELOPER_NAME}")
    st.subheader('This is my "Chatbot J"')
    st.write("An interactive conversational AI assistant powered by Groq and Streamlit.")
    
    st.write("") # Spacing
    if st.button("🚀 Start Conversation", use_container_width=True):
        st.session_state.conversation_started = True
        st.rerun()

# ==========================================
# SCREEN 2: CONVERSATION PAGE (Burgundy & Wine)
# ==========================================
else:
    st.markdown(
        """
        <style>
        /* Chat screen background: Dark Burgundy #590A03 */
        [data-testid="stAppViewContainer"] {
            background-color: #590A03;
            color: #FFFFFF;
        }
        [data-testid="stHeader"] {
            background-color: transparent;
        }
        h1, h2, h3, p, span, label, div {
            color: #FFFFFF !important;
        }
        /* Sidebar: Deep Espresso Wine #3B0702 */
        [data-testid="stSidebar"] {
            background-color: #3B0702 !important;
        }
        /* Sidebar action buttons: Terracotta #9E3A31 */
        div.stButton > button {
            background-color: #9E3A31 !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
        }
        div.stButton > button:hover {
            background-color: #770F05 !important;
            border-color: #FFFFFF !important;
        }
        /* Chat bubble styling for dark background */
        [data-testid="stChatMessage"] {
            background-color: rgba(158, 58, 49, 0.25) !important;
            border: 1px solid rgba(158, 58, 49, 0.4) !important;
            border-radius: 10px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar with your name and greetings
    with st.sidebar:
        st.title(f"👋 Hello from {DEVELOPER_NAME}!")
        st.write("Welcome to **Chatbot J**. Feel free to ask any question!")
        st.divider()
        
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.conversation_started = False
            st.rerun()
            
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    # Main Chat Interface
    st.title("🤖 Chatbot J")
    st.caption(f"Developed by {DEVELOPER_NAME}")

    # Display past messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Initialize Groq LLM
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7
    )

    # Chat Input Box
    user_prompt = st.chat_input("Ask Chatbot J anything...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        response = llm.invoke(
            input=[
                {
                    "role": "system",
                    "content": f"You are Chatbot J, an intelligent assistant created by {DEVELOPER_NAME}. Be polite, helpful, and concise."
                },
                *st.session_state.chat_history
            ]
        )

        assistant_response = response.content or response.additional_kwargs.get("reasoning_content", "No response received.")
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        with st.chat_message("assistant"):
            st.markdown(assistant_response)