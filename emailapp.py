import streamlit as st
import openai
from ml_backend import ml_backend

st.title("Interactive Email Generator App")
st.text("""

    by 
    110550205 - 蕭朝
    112550028 - 何柏翰
    112550054 - 陳奕均

    """)

st.markdown(""" 

# About
 
### As a university student, it is very common for us to have to write emails to dozens of people every day, and it may be hard to use the perfect tone for each email. With gpt-4’s explosive popularity, many people have resorted to using it for generating emails. However, it is often easily identifiable whether an email is generated by chatgpt. Therefore, we create an application of gpt-4 where it can identify the receiver of the email and write it with the respective tone.

""")

st.markdown("# Generate Email")

backend = ml_backend()

with st.form(key="form"):
    init_prompt = st.text_input("Initial prompt.")
    st.text(f"(Example: Write an email to professor [Professor’s Last Name’] regarding on wanting to join course [Course Name] from [Your Name])")

    
    slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=750)
    st.text("(A typical email is usually 100-500 characters)")

    submit_button = st.form_submit_button(label='Generate Email')

    if submit_button:
        with st.spinner("Transfoming the prompt"):
            final_prompt = backend.transform_prompt(init_promt)

        st.markdown("# Transsformed prompt")
        st.subheader(final_prompt)

        with st.spinner("Generating Email..."):
            email_output = backend.generate_email(final_prompt, slider)

        st.markdown("# Email Output:")
        st.subheader(email_output)

        st.markdown("____")
        st.markdown("# Send Your Email")
        st.subheader("You can press the Generate Email Button again if you're unhappy with the model's output")
        
        st.subheader("Otherwise:")
        st.text(email_output)
        url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + backend.replace_spaces_with_pluses(email_output)

        st.markdown("[Click me to send the email]({})".format(url))
