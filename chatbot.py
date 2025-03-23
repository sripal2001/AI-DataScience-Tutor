import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI  # Google AI Chatbot
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
import time

# 🎨 Streamlit Page Config
st.set_page_config(page_title="AI Data Science Tutor", page_icon="🎓", layout="wide")

# 💡 Custom CSS for Modern Look
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
        }
        .stTextInput input {
            background-color: #1f2c3b !important;
            color: white !important;
        }
        .stButton>button {
            background: #009FFD !important;
            color: white !important;
            border-radius: 10px !important;
            padding: 8px 20px !important;
            font-size: 16px !important;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: #00CFFD !important;
        }
        .user-msg {
            background: #0078FF;
            padding: 10px 15px;
            border-radius: 10px;
            width: fit-content;
            color: white;
            margin-bottom: 5px;
        }
        .ai-msg {
            background: #222;
            padding: 10px 15px;
            border-radius: 10px;
            width: fit-content;
            color: white;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# 🤖 Set up Google AI (Replace with your API key)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key="AIzaSyDr2vLKo30a9WliW_j0j3sbnUx1QM1Da2o")

# 📌 Sidebar with Tutor Info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3308/3308393.png", width=150)
    st.title("📚 AI Tutor Bot")
    st.write("Your AI-powered **Data Science Tutor**. Ask me anything about Machine Learning, Python, AI, and more! 🚀")
    st.markdown("---")
    st.write("🔹 **Powered by Google AI (Gemini Pro)**")  
    st.write("🔹 Developed using **LangChain + Streamlit**")  
    st.write("🔹 Built for students & professionals 👨‍🎓")  

# 📝 Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a friendly and knowledgeable AI Data Science Tutor.")
    ]

# 🎤 UI Title
st.markdown("<h1 style='text-align: center;'>🎓 AI Data Science Tutor</h1>", unsafe_allow_html=True)
st.write("👋 **Hello! I'm here to help you with Data Science, Python, AI, and more. Ask me anything!**")

# 🟢 User Input Field
user_input = st.text_input("💬 Type your question here and press Enter:")

# 🧠 Memory + AI Response
if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))  # Save user message

    # Simulate Typing Effect
    with st.spinner("Thinking..."):
        time.sleep(1)  # Simulating delay for realism
        response = llm.invoke(st.session_state.messages)
    
    st.session_state.messages.append(AIMessage(content=response.content))  # Save AI reply

# 📜 Display Chat Messages
st.markdown("### 📢 Chat History:")

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f"<div class='user-msg'>👤 {msg.content}</div>", unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"<div class='ai-msg'>🤖 {msg.content}</div>", unsafe_allow_html=True)
