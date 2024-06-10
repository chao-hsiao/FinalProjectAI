import openai
import urllib.parse

import torch
from transformers import DistilBertForQuestionAnswering
from transformers import AutoTokenizer
import warnings
warnings.simplefilter("ignore")

weight_path = "mymodel_2"

class ml_backend:
    def __init__(self):
        openai.api_key = 'sk-proj-JRUnxXSKBb0TWMJ4m7Q8T3BlbkFJvxqvMjBdcvCKqC3lrT9t'  # Replace with your actual API key
        # Ensure to use the correct base URL if you are using a custom API gateway
        # openai.api_base = 'https://api.pawan.krd/v1'  # Uncomment if needed

    def generate_email(self, userPrompt="Write an email to professor [Professor’s Last Name] regarding on wanting to join course [Course Name] from [Your Name]", start="", slider=64):
        """Returns a generated email using GPT-3.5 with a certain prompt and starting sentence"""
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",  # Use the correct model name
            prompt=f"{userPrompt}\nIt should less then {slider} words in email and first line should be the subject of the email with this format, Subject: XXX\n\n{start}",
            temperature=0.71,
            max_tokens=800,
            top_p=1,
            frequency_penalty=0.36,
            presence_penalty=0.75
        )
        return response.choices[0].text

    def replace_spaces_with_pluses(self, sample):
        """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
        if sample is None:
            return ""
        return urllib.parse.quote(sample)

    def transform_prompt(self, init_prompt):
        # loading tokenizer
        trained_checkpoint = "distilbert-base-uncased"
        tokenizer = AutoTokenizer.from_pretrained(trained_checkpoint)
        #loading the model

        model = DistilBertForQuestionAnswering.from_pretrained(trained_checkpoint)
        model.load_state_dict(torch.load(weight_path, map_location=torch.device('cpu')))
        model.to(torch.device('cpu'))
        model.eval()

        questions=["who is writing this letter","who is going to receive this letter","what is the email about"]
        # context = 'Write an email from James to Professor Martinez regarding a missed assignment deadline.'
        answers = []
        for i in range(3):
            inputs = tokenizer(questions[i], init_prompt, return_tensors="pt")
            with torch.no_grad():
                outputs = model(**inputs)
            start_logits,end_logits = outputs['start_logits'],outputs['end_logits']
            # Find the tokens with the highest `start` and `end` scores.
            answer_start = torch.argmax(start_logits)
            answer_end = torch.argmax(end_logits)

            predict_answer_tokens = inputs.input_ids[0, answer_start : answer_end + 1]
            answers.append(tokenizer.decode(predict_answer_tokens) )

        result_prompt_intention = "Craft an email from "+ answers[0] + " to "+ answers[1] + " regarding " + answers[2]

        key_role = ['student','TA','school','professor']
        role_spec = { 'student':"use a tone with some respect, but less formal and without the use of emotes. Exaggeration is acceptable.",
                      'TA':"use a tone with some respect,  formal , but using weaker vocabulary. Emotes and Exaggeration is not acceptable.",
                      'professor':"use a tone of great respect, very formal. Emotes and Exaggeration is not acceptable.",
                      'school':"use a tone with some respect, formal, with precise and less wording. Emotes and Exaggeration is not acceptable."
                      }
        the_role = ""

        for role in key_role:
          if role in answers[1]:
            the_role = role
            break

        result_prompt_spec = role_spec.get(the_role)
        if(result_prompt_spec == None):
          result_prompt_spec = "use a tone with some respect, formal, with precise and less wording. Emotes and Exaggeration is not acceptable."
        result_prompt = result_prompt_intention + " " + result_prompt_spec
        # print(result_prompt)

        return result_prompt

    def parse_email(self, email_text):
        """Parses the email text to extract the subject and body"""
        lines = email_text.split('\n')
        subject = ""
        body = []
        for line in lines:
            if line.startswith("Subject:"):
                subject = line[len("Subject:"):].strip()
            else:
                body.append(line)
        body_text = "\n".join(body).strip()
        return subject, body_text

