from groq import Groq
import yaml

api_key = None
CONFIG_PATH = r"config.yaml"

with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['GROQ_API_KEY']

def prompt_result(resume_data):

    prompt = '''
    You are an AI bot designed to act as a professional for parsing resumes. You are given a resume and your job is to extract the following information from the resume:
    1. full name
    2. email id
    3. github portfolio
    4. linkedin id
    5. employment details
    6. technical skills
    7. soft skills
    Give the extracted information in json format only
    '''

    user_content = resume_data

    client = Groq(
        api_key = api_key
    )

    # messages = [
    #     {
    #         "role": "system",
    #         "content": prompt
    #     },
    #     {
    #         "role": "user",
    #         "content": user_content
    #     }
    # ]

    response = client.chat.completions.create(
        messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": user_content
        }
    ],
        model = "llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
    )

    data = response.choices[0].message.content

    return data
