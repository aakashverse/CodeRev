import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# generate review - !!! aa simple version baad me or accha !!!
def generate_review(files):
    collected_code = ""

    for file in files:
        collected_code += f"\n\n File: {file.path}\n{file.content[:2000]}"       # limit size ???

        prompt = """
            You're a senior software engineer doing a code review.
            Analyze the following code & provide:
            1. Target File.
            2. Line number.
            3. Overall review.
            4. Severity ('High', 'Med', 'Low')
            5. Issues (bugs, bad practices, security vulnerabilities)
            6. Fix (improvements, performance, readability)

            code: {collected_code}

            Response in  Json format:
            {{
                "target file": "...",
                "line No.": __ , 
                "review": "...",
                "severity": "...",
                "issues": "...",
                "fix": "..."
            }}
        """

        response =  client.chat.completions.create(
            model="gpt-4.1-mini",
            messages = [
                {"role": "ai", "content": "You are a strict code reviewer." },
                {"role": "user", "content": prompt},
            ],
        )

        print(response.text)
