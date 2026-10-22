# Gemini AI MCQ Generator and Python Quiz Application

## 1. Project Overview

This project is a Python-based Multiple-Choice Question (MCQ) Generator and Quiz Application powered by Google's Gemini API.

The project consists of two Python programs:

1. **MCQ JSON Generator (`MCQ JSON Generator.py`)** — Uses Gemini AI to generate multiple-choice questions on a user-specified topic and saves them in a JSON file.
2. **Python Quiz Application (`MCQ Question Tester.py`)** — Reads the generated questions from the JSON file, presents them interactively, checks the user's answers, and calculates the final score.

The two programs work together to create a simple AI-powered quiz system.

### Key Features

- Generate MCQs on any topic using Gemini AI.
- Specify the number of questions to generate.
- Generate four options for each question.
- Store questions and correct answers in JSON format.
- Load questions automatically from the generated JSON file.
- Validate user input and handle invalid answers.
- Display the correct answer when the user answers incorrectly.
- Calculate correct answers, incorrect answers, and percentage.
- Provide performance feedback based on the final score.
- Keep the Gemini API key outside the source code using environment variables.

### Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | AI-powered question generation |
| Google Gen AI SDK | Connects Python to Gemini |
| JSON | Stores and transfers quiz questions |
| `python-dotenv` | Loads the API key from a `.env` file |
| `pathlib` | Handles file paths reliably |

---

## 2. How the Project Works

The project follows a two-stage workflow.

**Stage 1: Generate questions**

The user enters a topic and the number of questions required. The Python program sends a prompt to Gemini, receives the generated questions in JSON format, validates the response, and saves it to `python_mcqs.json`.

**Stage 2: Conduct the quiz**

The quiz program reads `python_mcqs.json`, displays the questions and options, accepts the user's answers, checks each answer, and displays the final result.

### Project Workflow

```text
                 USER
                   |
                   v
       Enter Topic and Question Count
                   |
                   v
          MCQ JSON Generator.py
                   |
                   v
            Gemini API Request
                   |
                   v
           Gemini Generates MCQs
                   |
                   v
          Parse and Validate JSON
                   |
                   v
            python_mcqs.json
                   |
                   v
             MCQ Question Tester.py
                   |
                   v
       Display Questions and Options
                   |
                   v
           Accept User Answers
                   |
                   v
           Check Correct Answers
                   |
                   v
         Calculate Final Percentage
                   |
                   v
            Display Quiz Result
```

---

# 3. Installation and Setup

Follow these steps in order to run the project successfully.

## Step 1: Install Python

Install Python if it is not already installed.

Download it from the official website:

https://www.python.org/downloads/

Verify the installation using the VS Code terminal:

```powershell
python --version
```

If your system uses the Python launcher, you can also try:

```powershell
py --version
```

Make sure you use the same Python interpreter when installing packages and running the scripts.

## Step 2: Create the Project Folder

Create a folder for the project. For example:

```text
GEN_AI/
└── MCQ_Quiz_Project/
```

Open this folder in Visual Studio Code.

## Step 3: Create the Required Files

Inside the project folder, create the following files:

```text
MCQ_Quiz_Project/
│
├── MCQ JSON Generator.py
├── MCQ Question Tester.py
├── .env
└── .gitignore
```

Copy the MCQ Generator code into `MCQ JSON Generator.py`.

Copy the Quiz Application code into `MCQ Question Tester.py`.

The `python_mcqs.json` file will be created automatically when the generator runs successfully.

## Step 4: Create a `.env` File

The `.env` file stores your Gemini API key separately from your Python code.

In VS Code:

1. Open the Explorer panel.
2. Select your project folder.
3. Create a new file named `.env`.
4. Add the following line:

```text
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

Replace `your_actual_gemini_api_key_here` with your own API key.

For example, the line should follow this format:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

The example above is only a placeholder. Do not use it as an actual key.

**Important:** Do not add quotation marks around the value unless your specific configuration requires them. Do not add the API key directly to your Python source code.

## Step 5: Get Your Gemini API Key

The MCQ Generator uses the Gemini API to generate questions. You need an API key to authenticate your requests.

### How to obtain the key

1. Open Google AI Studio: https://aistudio.google.com/
2. Sign in with your Google account.
3. Open the API Keys section.
4. Create an API key using an available Google Cloud project, following the instructions displayed by AI Studio.
5. Copy the key and paste it into your `.env` file.
6. Save the `.env` file.

Official documentation:

- Gemini API key guide: https://ai.google.dev/gemini-api/docs/api-key
- Google AI Studio: https://aistudio.google.com/

API access, available models, quotas, and billing requirements depend on Google's current policies and your project configuration.

**Security warning:** Never publish your API key on GitHub, include it in screenshots, or commit your `.env` file. If a key is exposed, revoke or rotate it through the provider's key-management interface.

## Step 6: Install the Required Packages

Open the VS Code terminal:

**Terminal → New Terminal**

Run:

```powershell
python -m pip install --upgrade google-genai python-dotenv
```

The packages are:

- `google-genai` — Google's Gen AI SDK for Python.
- `python-dotenv` — Loads environment variables from `.env`.

The `json`, `os`, and `pathlib` modules are included with Python, so they do not need separate installation.

If the `python` command does not use the correct interpreter, run the installation command with the full path to your Python executable.

For example, on Windows:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" -m pip install --upgrade google-genai python-dotenv
```

## Step 7: Run the MCQ Generator

Run the following command from the project folder:

```powershell
python "MCQ JSON Generator.py"
```

The program will ask for a topic and the number of questions.

Example:

```text
Enter MCQ topic: Python Programming
How many questions do you want (1-100)? 5

Generating MCQs using Gemini...
```

Gemini generates the questions. The program then parses and validates the response and saves the output.

After a successful run, the terminal displays a confirmation similar to:

```text
==================================================
MCQ JSON GENERATED SUCCESSFULLY
==================================================
Topic           : Python Programming
Total Questions : 5
File Created    : .../python_mcqs.json
```

The exact path and generated questions will depend on your system and input.

### Output File

The generator creates:

```text
python_mcqs.json
```

This file contains the questions, their four options, and the correct answer for each question.

## Step 8: Run the Quiz Application

Once `python_mcqs.json` has been generated, run:

```powershell
python "MCQ Question Tester.py"
```

The quiz program reads the JSON file and begins displaying questions.

Example:

```text
==================================================
                  PYTHON QUIZ
==================================================

Question 1:
Which keyword is used to define a function in Python?

1. function
2. def
3. define
4. fun

Enter your answer (1-4): 2
Correct!
```

The displayed questions and options will be generated by Gemini, so your actual output may differ from this example.

After answering all questions, the program displays a summary similar to:

```text
==================================================
                  QUIZ RESULT
==================================================
Total Questions : 5
Correct Answers : 4
Wrong Answers   : 1
Score           : 80.00%
Excellent!
==================================================
```

Your result depends on your answers.

### Important Execution Order

Always run the scripts in this order:

1. `MCQ JSON Generator.py`
2. `MCQ Question Tester.py`

The generator creates the JSON file that the quiz application needs.

If you already have a valid `python_mcqs.json` file, you can run the quiz application directly without generating new questions.

---

# 4. Project File Structure

After generating questions, your project folder will look like this:

```text
MCQ_Quiz_Project/
│
├── MCQ JSON Generator.py
├── MCQ Question Tester.py
├── python_mcqs.json
├── .env
└── .gitignore
```

| File | Description |
|---|---|
| `MCQ JSON Generator.py` | Generates MCQs using Gemini AI |
| `MCQ Question Tester.py` | Runs the interactive quiz |
| `python_mcqs.json` | Stores generated questions and answers |
| `.env` | Stores the Gemini API key locally |
| `.gitignore` | Excludes sensitive and unnecessary files from Git |

---

# 5. Code Explanation: MCQ JSON Generator

The first program generates questions using Gemini AI and stores them in a structured JSON file.

## 5.1 Import Required Libraries

```python
import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
```

Each import has a specific purpose.

- `os` reads environment variables.
- `json` converts between JSON and Python data.
- `Path` handles file and directory paths.
- `load_dotenv` loads variables from `.env`.
- `genai` provides access to the Gemini API.
- `types` provides configuration classes for API requests.

The `os`, `json`, and `pathlib` modules are part of Python's standard library. The other packages must be installed.

## 5.2 Load the Environment Variables

```python
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        f"GEMINI_API_KEY was not found. Check: {ENV_PATH}"
    )
```

This section securely loads the API key.

### Understanding the path

- `__file__` refers to the current Python script.
- `.resolve()` obtains its absolute path.
- `.parent` identifies the directory containing the script.
- `BASE_DIR / ".env"` constructs the path to `.env`.

Using this approach ensures that the program searches for `.env` next to the Python script rather than relying on the terminal's current working directory.

### Load the key

```python
load_dotenv(ENV_PATH)
API_KEY = os.getenv("GEMINI_API_KEY")
```

`load_dotenv()` reads the environment file. `os.getenv()` retrieves the value associated with the specified variable name.

The following check stops execution if the key is missing:

```python
if not API_KEY:
    raise ValueError(...)
```

This prevents the program from proceeding without a configured key.

## 5.3 Define the Configuration

```python
MODEL_NAME = "gemini-3.5-flash-lite"
OUTPUT_PATH = BASE_DIR / "python_mcqs.json"

MIN_QUESTIONS = 1
MAX_QUESTIONS = 100
```

These variables centralize the settings used throughout the script.

- `MODEL_NAME` identifies the Gemini model.
- `OUTPUT_PATH` specifies where the generated JSON file will be saved.
- `MIN_QUESTIONS` defines the minimum allowed question count.
- `MAX_QUESTIONS` defines the maximum allowed question count.

**Model availability:** Model names and availability can change. If Gemini returns a model-not-found error, replace `MODEL_NAME` with a model currently available to your API key. Consult https://ai.google.dev/gemini-api/docs/models.

## 5.4 Create the Gemini Client

```python
client = genai.Client(api_key=API_KEY)
```

The client provides the connection between your Python program and Gemini.

The API key authenticates requests. The program uses the client to send a prompt and receive generated content.

## 5.5 Get Input from the User

```python
topic = input("Enter MCQ topic: ").strip()
```

`input()` waits for the user to enter a value.

`.strip()` removes unnecessary whitespace from the beginning and end of the input.

For example:

```python
topic = "   Python Loops   "
print(topic.strip())
```

Output:

```text
Python Loops
```

The code rejects an empty topic:

```python
if not topic:
    raise ValueError("Topic cannot be empty.")
```

### Convert the question count into an integer

```python
count_input = input(
    f"How many questions do you want ({MIN_QUESTIONS}-{MAX_QUESTIONS})? "
).strip()

try:
    count = int(count_input)
except ValueError:
    raise ValueError("Please enter a valid whole number.")
```

`input()` always returns a string. `int()` converts a valid whole-number string into an integer.

The `try`/`except` block handles invalid input such as `five`.

The range validation then checks that the number is between 1 and 100.

## 5.6 Create the Prompt

```python
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
"""
```

A prompt is the instruction sent to the AI model.

The `f` before the triple-quoted string makes this an f-string. It allows Python to insert variables into the text.

For example, if:

```python
topic = "Python Functions"
count = 5
```

the prompt requests five questions about Python functions.

The prompt also defines the output structure, so that the generated questions can be processed by the quiz program.

### Expected JSON Structure

```json
[
    {
        "id": 1,
        "question": "What is the purpose of a Python function?",
        "options": [
            "To group reusable instructions",
            "To install Python",
            "To delete a file automatically",
            "To create a database by default"
        ],
        "answer": 1
    }
]
```

The `answer` field uses 1-based numbering. An answer of `1` indicates that the first option is correct.

A prompt is not an absolute guarantee of correctness. Gemini may still generate a wrong answer or a question with more than one plausible answer, so factual review may be necessary.

## 5.7 Call the Gemini API

```python
response = client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=0.3,
    ),
)
```

This is the API request that generates the questions.

- `model=MODEL_NAME` selects the model.
- `contents=prompt` provides the instructions.
- `response_mime_type="application/json"` requests JSON-formatted output.
- `temperature=0.3` encourages relatively consistent output.

The request is wrapped in a `try`/`except` block in the complete program so API failures can be reported clearly.

Possible problems include an invalid model name, authentication issues, quota restrictions, or network errors.

## 5.8 Extract the Response Text

```python
response_text = response.text

if not response_text:
    raise ValueError(
        "Gemini returned an empty response."
    )
```

The API response is an object. Its `text` property contains the generated text when available.

The empty-response check prevents the program from attempting to parse a missing response as JSON.

## 5.9 Convert JSON into Python Data

```python
questions = json.loads(response_text)
```

`json.loads()` converts a JSON string into native Python objects.

For example:

```python
import json

text = '[{"id": 1, "question": "Example?", "answer": 2}]'

data = json.loads(text)

print(type(data))
```

Output:

```text
<class 'list'>
```

A JSON array becomes a Python list, and each JSON object becomes a Python dictionary.

The program handles `json.JSONDecodeError` if the returned text is not valid JSON.

### Useful JSON Functions

| Function | Purpose |
|---|---|
| `json.loads()` | Converts JSON text into Python data |
| `json.dumps()` | Converts Python data into JSON text |
| `json.load()` | Reads JSON from a file |
| `json.dump()` | Writes Python data to a JSON file |

## 5.10 Validate the Generated Questions

AI-generated output should be checked before it is saved.

### Check the overall structure

```python
if not isinstance(questions, list):
    raise ValueError("The response must be a JSON array.")

if len(questions) != count:
    raise ValueError(...)
```

The first check ensures that the response is a list.

The second check verifies that the number of questions matches the requested count.

### Check required fields

```python
required_keys = {"id", "question", "options", "answer"}

if not required_keys.issubset(question.keys()):
    raise ValueError(...)
```

Every question must contain the required keys.

The program also checks that:

- Each question is a dictionary.
- The ID is the expected sequential integer.
- The question text is a non-empty string.
- There are exactly four options.
- Every option is a non-empty string.
- The answer is an integer from 1 to 4.

For example:

```python
if type(answer) is not int or answer not in [1, 2, 3, 4]:
    raise ValueError(...)
```

This rejects invalid answer values such as `0`, `5`, `"2"`, or `True`.

**Important limitation:** These checks validate the structure and value types, not whether the answer is factually correct. That requires separate verification or human review.

## 5.11 Save the JSON File

```python
with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
    json.dump(
        questions,
        file,
        indent=4,
        ensure_ascii=False,
    )
```

This saves the validated questions to `python_mcqs.json`.

- `open()` opens the output file.
- `"w"` means write mode.
- `encoding="utf-8"` supports Unicode characters.
- `json.dump()` writes the Python list into JSON format.
- `indent=4` makes the file easier to read.
- `ensure_ascii=False` preserves Unicode characters directly.
- `with` ensures that the file is closed automatically.

If the file already exists, write mode overwrites it with the newly generated questions.

## 5.12 Display the Success Message

```python
print("MCQ JSON GENERATED SUCCESSFULLY")
print("Topic           :", topic)
print("Total Questions :", len(questions))
print("File Created    :", OUTPUT_PATH)
```

These statements display a confirmation message and the location of the generated file.

The success message is printed only after the file has been written.

---

# 6. Code Explanation: Python Quiz Application

The second program reads the generated JSON file and turns it into an interactive quiz.

## 6.1 Import the Required Libraries

```python
import json
from pathlib import Path
```

- `json` reads the questions from the file.
- `Path` constructs a reliable path to the JSON file.

No additional third-party packages are needed for the quiz program.

## 6.2 Load Questions from the JSON File

```python
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "python_mcqs.json"

with open(JSON_PATH, "r", encoding="utf-8") as file:
    questions = json.load(file)
```

This code locates and reads the generated JSON file.

Using `BASE_DIR` ensures that the file is searched for beside the script, regardless of the terminal's current working directory.

The complete version also handles two errors:

- `FileNotFoundError` — the file cannot be found.
- `json.JSONDecodeError` — the file contains invalid JSON.

The program checks that the loaded data is a non-empty list before starting the quiz.

This is important because an empty list would result in division by zero when calculating the final percentage.

## 6.3 Initialize the Score

```python
score = 0
total = len(questions)
```

`score` records the number of correct answers.

`total` records the total number of questions.

For example, if there are ten questions:

```python
score = 0
total = 10
```

The score starts at zero because the user has not answered any questions yet.

## 6.4 Loop Through the Questions

```python
for question in questions:

    print(f"\nQuestion {question['id']}:")
    print(question["question"])
```

The `for` loop processes each question in the list.

Each `question` is a dictionary, so the program accesses its values using dictionary keys.

For example:

```python
question["id"]
question["question"]
question["options"]
question["answer"]
```

These expressions retrieve the question ID, question text, options, and correct answer.

## 6.5 Display the Options

```python
options = question["options"]
option_count = len(options)

for index, option in enumerate(options, start=1):
    print(f"{index}. {option}")
```

`options` stores the list of choices for the current question.

`len(options)` returns the number of available options.

`enumerate()` provides both the option number and the option text.

For example:

```python
options = ["Integer", "String", "List", "Dictionary"]
```

The output is:

```text
1. Integer
2. String
3. List
4. Dictionary
```

`start=1` is used because users select options numbered from 1.

## 6.6 Accept and Validate the User's Answer

```python
while True:

    user_input = input(
        f"\nEnter your answer (1-{option_count}): "
    ).strip()

    try:
        answer = int(user_input)

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if 1 <= answer <= option_count:
        break

    print(
        f"Please enter a number between 1 and {option_count}."
    )
```

This section prevents invalid input from breaking the quiz.

### Why use a `while True` loop?

The loop keeps running until the user enters a valid option number.

For example, the following inputs are rejected:

```text
hello
0
8
```

If there are four options, only `1`, `2`, `3`, or `4` are accepted.

### Why use `try` and `except`?

The expression `int(user_input)` converts the entered text into an integer.

If the user enters `hello`, Python raises `ValueError`.

The `except` block catches the error and displays a helpful message instead of terminating the program.

### Understanding `continue` and `break`

- `continue` skips the remaining statements in the current loop iteration and starts another iteration.
- `break` exits the loop when the answer is valid.

This creates a repeated input-validation process.

## 6.7 Retrieve the Correct Answer

```python
correct_option = question["answer"]
```

This retrieves the correct option number from the current question dictionary.

For example:

```python
"answer": 2
```

means the second option is correct.

The quiz uses the same answer convention as the generator, so both programs remain compatible.

## 6.8 Compare the Answer and Update the Score

```python
if answer == correct_option:
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

    correct_answer = options[correct_option - 1]

    print("Correct answer:", correct_answer)
```

The `==` operator compares the user's answer with the correct option number.

If both values match, the answer is correct.

```python
score += 1
```

is shorthand for:

```python
score = score + 1
```

It increases the score by one.

If the answer is incorrect, the program retrieves and displays the correct option.

### Why subtract one from the correct option?

JSON answers use 1-based numbering, but Python list indexes start at zero.

| Correct answer number | Python list index |
|---:|---:|
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |

For example:

```python
options = ["Integer", "String", "List", "Dictionary"]
correct_option = 3

correct_answer = options[correct_option - 1]
```

The result is:

```text
List
```

Without subtracting one, the program would select the wrong list element.

## 6.9 Calculate the Final Result

```python
wrong = total - score
percentage = (score / total) * 100
```

The number of incorrect answers is the total number of questions minus the number of correct answers.

The percentage is calculated using:

**Percentage = (Correct Answers / Total Questions) × 100**

For example, if the user answers eight out of ten questions correctly:

```text
Total Questions = 10
Correct Answers = 8
Wrong Answers   = 2
Percentage      = 80%
```

The code uses:

```python
percentage = (score / total) * 100
```

The empty-list validation earlier prevents `total` from being zero.

## 6.10 Display the Final Result

```python
print(f"Total Questions : {total}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {wrong}")
print(f"Score           : {percentage:.2f}%")
```

These lines display the quiz summary.

The expression:

```python
{percentage:.2f}
```

formats the percentage to two decimal places.

For example:

```text
80.00%
66.67%
33.33%
```

## 6.11 Provide Performance Feedback

```python
if percentage >= 80:
    print("Excellent!")

elif percentage >= 60:
    print("Good job!")

elif percentage >= 40:
    print("Keep practicing!")

else:
    print("You need more practice.")
```

The program evaluates the percentage and displays appropriate feedback.

| Percentage | Feedback |
|---:|---|
| 80% or above | Excellent! |
| 60% to below 80% | Good job! |
| 40% to below 60% | Keep practicing! |
| Below 40% | You need more practice. |

Python checks each condition from top to bottom. Once a condition is true, its corresponding block executes and the remaining branches are skipped.

---

# 7. Important Python Concepts Learned

This project combines several foundational Python concepts.

| Concept | Where It Is Used |
|---|---|
| Variables | `topic`, `count`, `score`, `total`, `percentage` |
| Data types | Strings, integers, lists, dictionaries |
| User input | `input()` |
| Type conversion | `int()` |
| Conditions | `if`, `elif`, `else` |
| Loops | `for` and `while` |
| Exception handling | `try`, `except`, `raise` |
| Lists | Storing questions and options |
| Dictionaries | Storing each question's fields |
| List indexing | Retrieving the correct option |
| String formatting | f-strings |
| Functions from libraries | `json.load()`, `json.dump()`, `os.getenv()` |
| File handling | `open()` and `with` |
| Path handling | `Path(__file__).resolve().parent` |
| Environment variables | `.env` and `load_dotenv()` |
| API integration | Gemini client and `generate_content()` |
| Data validation | Checking types, lengths, keys, and values |

## 8. Common Errors and Solutions

### Error: `GEMINI_API_KEY was not found`

**Possible cause:** The `.env` file is missing, the variable name is incorrect, or the key is empty.

**Solution:**

- Ensure `.env` is beside `MCQ JSON Generator.py`.
- Confirm that the variable is named `GEMINI_API_KEY`.
- Save the file and run the program again.

### Error: Gemini API request failed

**Possible causes:**

- Invalid or revoked API key.
- Model name unavailable to your API key.
- Network issue.
- API quota or access restrictions.

**Solution:** Check the key configuration, internet connection, API usage, and the current model documentation.

### Error: Questions file not found

**Possible cause:** `python_mcqs.json` has not been generated or is not in the expected project folder.

**Solution:** Run `MCQ JSON Generator.py` first and verify that the JSON file is created.

### Error: Invalid JSON

**Possible cause:** The JSON file is incomplete, manually edited incorrectly, or contains invalid syntax.

**Solution:** Generate the file again or correct the JSON syntax.

### Error: Invalid number entered

**Possible cause:** The user entered text or an option number outside the permitted range.

**Solution:** Enter a whole number within the displayed range.

---

# 9. Limitations and Future Improvements

This project is a learning implementation and can be extended in several ways.

### Current Limitations

- The quiz runs in the terminal rather than a graphical interface.
- The quiz assumes that each question has valid fields and a valid answer.
- Structural validation cannot guarantee that Gemini's questions and answers are factually correct.
- Running the generator again overwrites the previous JSON file.
- The quiz does not currently save a history of attempts or scores.
- API access and model availability depend on the provider's configuration and policies.

### Possible Improvements

1. Add a retry mechanism when Gemini returns an invalid response.
2. Add stronger JSON validation in the quiz application.
3. Add a question difficulty option: Easy, Medium, or Hard.
4. Let users select the number of options per question.
5. Save quiz results and timestamps to a CSV file or SQLite database.
6. Add categories and difficulty levels to each question.
7. Build a graphical user interface using Streamlit.
8. Add a timer for each question.
9. Shuffle the questions and answer options.
10. Add a review mode that displays incorrect answers at the end.
11. Add automated tests for JSON validation and score calculations.

---

# 10. GitHub Upload Guide

Before uploading the project, confirm that your `.gitignore` contains:

```text
.env
__pycache__/
.venv/
venv/
```

Do not upload your real API key. You can include a `.env.example` file containing a placeholder to show other developers how to configure the project:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

An example file is safe only if it contains a placeholder rather than a real secret.

Suggested repository structure:

```text
Gemini-MCQ-Generator-Quiz/
│
├── README.md
├── MCQ JSON Generator.py
├── MCQ Question Tester.py
├── .env.example
├── .gitignore
└── python_mcqs.json
```

The sample `python_mcqs.json` is optional. Including a small sample allows people to run the quiz without using the Gemini API first.

### Suggested GitHub Description

**AI-powered MCQ generator and interactive Python quiz application using Google's Gemini API, JSON, and Python.**

### Suggested Repository Topics

`python` `generative-ai` `gemini-api` `quiz-application` `json` `prompt-engineering` `beginner-project`

---

# 11. Conclusion

This project demonstrates how generative AI can be integrated into a practical Python application.

The first program uses the Gemini API to generate multiple-choice questions, validates the response, and stores the questions in JSON format. The second program reads that data, conducts an interactive quiz, evaluates the user's answers, and calculates the final score.

Together, these programs demonstrate practical skills in Python programming, API integration, prompt engineering, JSON processing, input validation, exception handling, and file management.

The project provides a foundation for building more advanced AI-powered learning applications and is a useful addition to a beginner GenAI portfolio.

## Official References

- Google AI Studio: https://aistudio.google.com/
- Gemini API key documentation: https://ai.google.dev/gemini-api/docs/api-key
- Gemini API documentation: https://ai.google.dev/gemini-api/docs
- Gemini model documentation: https://ai.google.dev/gemini-api/docs/models
- Python documentation: https://docs.python.org/3/
