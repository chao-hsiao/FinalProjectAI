# Interactive Email Generator App

## Description

As a university student, it is very common to write emails to dozens of people every day, and it may be hard to use the perfect tone for each email. With GPT-4’s explosive popularity, many people have resorted to using it for generating emails. However, it is often easily identifiable whether an email is generated by ChatGPT. Therefore, we created an application of GPT-4 where it can identify the receiver of the email and write it with the respective tone.

## Authors

- 110550205 - 蕭朝
- 112550028 - 何柏翰
- 112550054 - 陳奕均

## Features

- Configure Streamlit email settings directly within the app.
- Generate personalized emails with a professional tone using gpt-3.5-turbo-instruct.
- Automatically format emails for sending via Gmail.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository:**

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install required packages:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the setup script:**

   Ensure that the script `setup.sh` is executable. If not, make it executable:

   ```sh
   chmod +x setup.sh
   ```

   Execute the setup script with your email address:

   ```sh
   ./setup.sh your_email@example.com
   ```

### Running the Application

To start the Streamlit application, execute the following command:

```sh
streamlit run emailapp.py
```

### Using the Application

1. **Configure Email:**

   - Enter your email address in the provided input field and click "Set Email Configuration."

2. **Generate Email:**

   - Provide the initial prompt for the email.
   - Use the slider to specify the desired length of the email.
   - Click "Generate Email" to create a personalized email.

3. **Send Email:**

   - Review the generated email.
   - If satisfied, click the provided link to send the email via Gmail.

## Example Usage

1. Start the application:

   ```sh
   streamlit run emailapp.py
   ```

2. In your browser, enter

   your email address in the "Configure Email" section and click "Set Email Configuration."

3. Provide the initial prompt, for example:
   
   ```
   Write an email to professor [Professor’s Last Name] regarding wanting to join course [Course Name] from [Your Name]
   ```

4. Adjust the slider to your preferred email length and click "Generate Email."

5. Review the generated email. If you are satisfied with the content, click the "Click me to send the email" link to open Gmail with the email pre-filled.

## Troubleshooting

- **Port Issues:** If you encounter issues with the application running on port 80, ensure you have the necessary permissions. You may need to run the application with `sudo`:
  
  ```sh
  sudo streamlit run emailapp.py
  ```

- **Dependencies:** Ensure all dependencies are installed correctly. If you encounter any missing packages, try reinstalling them using:
  
  ```sh
  pip install -r requirements.txt
  ```

## Contribution

Feel free to fork this repository, make modifications, and submit pull requests. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
