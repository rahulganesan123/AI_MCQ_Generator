
# ============================================================
# GEMINI AI - MCQ JSON GENERATOR
# ============================================================

import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

# Get the folder where this Python file is located.
BASE_DIR = Path(__file__).resolve().parent

# Locate the .env file in the same folder.
ENV_PATH = BASE_DIR / ".env"

# Load variables from the .env file.
load_dotenv(ENV_PATH)

# Read the Gemini API key.
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        f"GEMINI_API_KEY was not found. Check: {ENV_PATH}"
    )


# ============================================================
# 2. CONFIGURATION
# ============================================================

MODEL_NAME = "gemini-3.5-flash-lite"
OUTPUT_PATH = BASE_DIR / "python_mcqs.json"

MIN_QUESTIONS = 1
MAX_QUESTIONS = 100


# ============================================================
# 3. CREATE GEMINI CLIENT
# ============================================================

client = genai.Client(api_key=API_KEY)


# ============================================================
# 4. GET USER INPUT
# ============================================================

topic = input("Enter MCQ topic: ").strip()

if not topic:
    raise ValueError("Topic cannot be empty.")

count_input = input(
    f"How many questions do you want ({MIN_QUESTIONS}-{MAX_QUESTIONS})? "
).strip()

try:
    count = int(count_input)
except ValueError:
    raise ValueError("Please enter a valid whole number.")

if count < MIN_QUESTIONS or count > MAX_QUESTIONS:
    raise ValueError(
        f"Enter a number between {MIN_QUESTIONS} and {MAX_QUESTIONS}."
    )


# ============================================================
# 5. CREATE THE PROMPT
# ============================================================

prompt = f"""
Generate exactly {count} multiple-choice questions
about this topic: {topic}

Rules:
1. Generate exactly {count} questions.
2. Every question must have exactly four options.
3. Only one option must be correct.
4. The answer must be an integer from 1 to 4.
5. Answers use 1-based numbering.
6. Question IDs must be unique integers from 1 to {count}.
7. Question text and options must not be empty.
8. Return a JSON array only.
9. Do not include Markdown or explanations outside the JSON.

Required structure:
[
    {{
        "id": 1,
        "question": "Question text",
        "options": [
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        ],
        "answer": 2
    }}
]
"""


# ============================================================
# 6. CALL GEMINI
# ============================================================

print("\nGenerating MCQs using Gemini...\n")

try:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.3,
        ),
    )

except Exception as error:
    raise RuntimeError(
        f"Gemini API request failed: {error}"
    ) from error


# ============================================================
# 7. EXTRACT THE RESPONSE TEXT
# ============================================================

response_text = response.text

if not response_text:
    raise ValueError(
        "Gemini returned an empty response. "
        "Check whether the request was blocked or incomplete."
    )


# ============================================================
# 8. PARSE THE JSON RESPONSE
# ============================================================

try:
    questions = json.loads(response_text)

except json.JSONDecodeError as error:
    raise ValueError(
        "Gemini returned a response that could not be parsed as JSON."
    ) from error


# ============================================================
# 9. VALIDATE THE GENERATED QUESTIONS
# ============================================================

if not isinstance(questions, list):
    raise ValueError("The response must be a JSON array.")

if len(questions) != count:
    raise ValueError(
        f"Expected {count} questions, but received {len(questions)}."
    )

required_keys = {"id", "question", "options", "answer"}

for index, question in enumerate(questions, start=1):

    # Each question must be a JSON object.
    if not isinstance(question, dict):
        raise ValueError(
            f"Question {index} must be a JSON object."
        )

    # Check for missing fields.
    if not required_keys.issubset(question.keys()):
        raise ValueError(
            f"Question {index} is missing one or more required fields."
        )

    # Validate the question ID.
    question_id = question["id"]

    if type(question_id) is not int or question_id != index:
        raise ValueError(
            f"Question {index} must have ID {index}."
        )

    # Validate the question text.
    question_text = question["question"]

    if not isinstance(question_text, str) or not question_text.strip():
        raise ValueError(
            f"Question {index} has empty or invalid question text."
        )

    # Validate the options.
    options = question["options"]

    if not isinstance(options, list) or len(options) != 4:
        raise ValueError(
            f"Question {index} must have exactly four options."
        )

    for option_number, option in enumerate(options, start=1):

        if not isinstance(option, str) or not option.strip():
            raise ValueError(
                f"Question {index}, option {option_number} is empty or invalid."
            )

    # Validate the answer.
    answer = question["answer"]

    if type(answer) is not int or answer not in [1, 2, 3, 4]:
        raise ValueError(
            f"Question {index} answer must be an integer from 1 to 4."
        )


# ============================================================
# 10. SAVE THE JSON FILE
# ============================================================

with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
    json.dump(
        questions,
        file,
        indent=4,
        ensure_ascii=False,
    )


# ============================================================
# 11. DISPLAY THE RESULT
# ============================================================

print("=" * 50)
print("MCQ JSON GENERATED SUCCESSFULLY")
print("=" * 50)

print("Topic           :", topic)
print("Total Questions :", len(questions))
print("File Created    :", OUTPUT_PATH)
