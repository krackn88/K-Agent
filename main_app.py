import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="K-Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Sidebar
    with st.sidebar:
        st.title("K-Agent 🤖")
        st.markdown("---")
        st.markdown("### Navigation")
        page = st.radio("", ["Chat", "Tools", "Settings"])
    
    # Main content
    st.title("K-Agent: Your AI Assistant 🤖")
    st.markdown("""
    Welcome to K-Agent! This is your intelligent assistant powered by advanced AI.
    
    ### Features:
    - 🧠 Intelligent conversation
    - 📝 Task automation
    - 🔍 Information retrieval
    - 🛠️ Tool integration
    """)
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What can I help you with?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add assistant response
        with st.chat_message("assistant"):
            response = "I'm here to help! This is a placeholder response."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()