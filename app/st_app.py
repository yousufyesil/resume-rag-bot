import streamlit as st
import os, sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
# --------------------------------------------------
from llm.model import ask
st.set_page_config(layout="wide")


def set_lang():
    options = ["DE", "EN"]
    selection = st.segmented_control(
        "", options, selection_mode="single",default="EN"
    )
with st.container(horizontal_alignment="right"):
    set_lang()

st.title("Yousuf Yesil")
st.markdown("<h3 style='margin-top:-37px;'><em>Student of Computer Science</em></h3>", unsafe_allow_html=True)
st.header("Work Experience", divider="blue")

col1, col2 = st.columns([1, 4])  # linke Spalte schmaler, rechte breiter

with col1:
    st.markdown("**since 02.2024**")

with col2:
    st.markdown("**Student Research – University of Applied Sciences Brandenburg**")
    st.markdown("""
    - Building knowledge base for RAG-System  
    - Optimization and evaluation of training data quality 
    - Development with Python
    """)

col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("""
    **01.2024 –**  
    **06.2025**
    """)
with col2:
    st.markdown("**Student Assistant – University of Applied Sciences Brandenburg**")
    st.markdown("""
    - Planning and implementation of workshops
    - Study counselling  
    """)

col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("""
    **06.2023 –**  
    **01.2024**
    """)
with col2:
    st.markdown("**Lecture – Barbarossa Learning Studio**")
    st.markdown("""
       - Subject-specific tutoring for STEM subjects, especially computer science, for all grade levels   
    """)
def create_education_sec() -> None:
    st.header("Education", divider="blue")

    col1, col2 = st.columns([1, 4])

    with col1:
        st.markdown("""
        **09.2023 –**  
        **07.2026**
        """)
    with col2:
        st.markdown("**Bachelor of Science – University of Applied Sciences Brandenburg**")
        st.markdown("""
           - Specialization in intelligent systems 
        - Scholarship from the University Foundation of Brandenburg University of Applied Sciences
        """)

    col1, col2 = st.columns([1, 4])

    with col1:
        st.markdown("""
        **09.2021 –**  
        **07.2023**
        """)
    with col2:
        st.markdown("**High school diploma –Heinrich Böll High School**")
        st.markdown("""
           - Involvement as student representative, district student representative, state student committee
        """)
create_education_sec()
def create_project_sec() -> None:
    st.header("Projects", divider="blue")

    col1, col2 = st.columns([1, 4])

    with col1:
        st.markdown("""
        since 09.2025
        """)
    with col2:
        st.markdown("**Anomaly detection in technical systems with LVMs**")
        st.markdown("""
           
        """)

#create_project_sec()
with st.sidebar:
    st.title("Chat with Yousuf")
    messages = st.container(height=700, horizontal_alignment="right")
    if prompt := st.chat_input("Ask me anything!"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Yousuf: {ask(prompt)}")

