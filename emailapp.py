import streamlit as st
import openai
import os
from ml_backend import ml_backend

# Set Streamlit page configuration
st.set_page_config(
    page_title="Interactive Email Generator App",
    page_icon="✉️",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("Interactive Email Generator App")
st.text("""

    by 
    110550205 - 蕭朝
    112550028 - 何柏翰
    112550054 - 陳奕均

    """)

st.markdown(""" 

# About
 
### This application is designed to help university students generate emails with the perfect tone, tailored to different recipients. With the growing popularity of GPT-3.5-turbo- instruct, many users have turned to AI for drafting emails. However, AI-generated emails can often be easily identified. Our application leverages GPT-3.5-turbo-instruct to generate personalized emails that consider the recipient, ensuring a professional tone and natural flow. Users can configure their email settings directly within the app and generate emails formatted for easy sending via Gmail.

""")

st.markdown("# Generate Email")

backend = ml_backend()

with st.form(key="form"):
    init_prompt = st.text_input("Initial prompt.")
    st.text(f"(Example: Write an email from James to Professor Martinez regarding a missed assignment deadline.)")
    if not init_prompt:
        init_prompt = "Write an email from James to Professor Martinez regarding a missed assignment deadline."
    
    slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=750)
    st.text("(A typical email is usually 100-500 characters)")

    submit_button = st.form_submit_button(label='Generate Email')

    if submit_button:
        with st.spinner("Transfoming the prompt"):
            final_prompt = backend.transform_prompt(init_prompt)

        st.markdown("# Transformed prompt")
        st.subheader(final_prompt)

        st.markdown("____")

        with st.spinner("Generating Email..."):
            email_output = backend.generate_email(final_prompt, slider=slider)

        st.markdown("# Email Output:")
        st.subheader(email_output)

        st.markdown("____")
        st.markdown("# Send Your Email")
        st.subheader("You can press the Generate Email Button again if you're unhappy with the model's output")
        
        st.subheader("Otherwise send the letter")
        subject, body_text = backend.parse_email(email_output)
        url = f"https://mail.google.com/mail/?view=cm&fs=1&to=&su={backend.replace_spaces_with_pluses(subject)}&body={backend.replace_spaces_with_pluses(body_text)}"

        st.markdown("[Click me to send the email]({})".format(url))
