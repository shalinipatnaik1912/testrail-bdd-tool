import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_test_cases(user_story):
    prompt = f"""
Convert the following user story into a single BDD-style test case using the Gherkin format:

User story: "{user_story}"

Output format:
Feature: <feature title>
  Scenario: <test scenario>
    Given <precondition>
    When <action>
    Then <expected result>
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
