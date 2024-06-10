import openai

class ml_backend:
    def __init__(self):
        openai.api_key = 'sk-proj-JRUnxXSKBb0TWMJ4m7Q8T3BlbkFJvxqvMjBdcvCKqC3lrT9t'  # Replace with your actual API key
        # Ensure to use the correct base URL if you are using a custom API gateway
        # openai.api_base = 'https://api.pawan.krd/v1'  # Uncomment if needed

    def generate_email(self, userPrompt="Write an email to professor [Professor’s Last Name] regarding on wanting to join course [Course Name] from [Your Name]", start="Dear", slider=64):
        """Returns a generated email using GPT-3.5 with a certain prompt and starting sentence"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-instruct",  # Use the correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{userPrompt}\n\n{start}"}
            ],
            temperature=0.71,
            max_tokens=800,
            top_p=1,
            frequency_penalty=0.36,
            presence_penalty=0.75
        )


    def replace_spaces_with_pluses(self, sample):
        """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
        if sample is None:
            return ""
        return '+'.join(sample.split())

    def transform_prompt(self, init_prompt):
        return init_prompt
