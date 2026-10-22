
# ============================================================
# PYTHON QUIZ APPLICATION
# Reads MCQs from a JSON file and calculates the final score.
# ============================================================

import json
from pathlib import Path


# ============================================================
# 1. LOAD QUESTIONS FROM JSON
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "python_mcqs.json"

try:
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        questions = json.load(file)

except FileNotFoundError:
    raise FileNotFoundError(
        f"Questions file not found: {JSON_PATH}"
    )

except json.JSONDecodeError as error:
    raise ValueError(
        f"The questions file contains invalid JSON: {JSON_PATH}"
    ) from error


# Validate the loaded data.
if not isinstance(questions, list) or len(questions) == 0:
    raise ValueError(
        "The JSON file must contain a non-empty list of questions."
    )


# ============================================================
# 2. INITIALIZE QUIZ
# ============================================================

score = 0
total = len(questions)

print("=" * 50)
print("                  PYTHON QUIZ")
print("=" * 50)


# ============================================================
# 3. LOOP THROUGH QUESTIONS
# ============================================================

for question in questions:

    print(f"\nQuestion {question['id']}:")
    print(question["question"])

    options = question["options"]
    option_count = len(options)

    # Display all available options.
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    # ========================================================
    # 4. GET AND VALIDATE USER ANSWER
    # ========================================================

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

    # ========================================================
    # 5. CHECK THE ANSWER
    # ========================================================

    correct_option = question["answer"]

    if answer == correct_option:
        print("Correct!")
        score += 1

    else:
        print("Incorrect!")

        correct_answer = options[correct_option - 1]

        print("Correct answer:", correct_answer)


# ============================================================
# 6. CALCULATE FINAL RESULT
# ============================================================

wrong = total - score
percentage = (score / total) * 100


# ============================================================
# 7. DISPLAY FINAL RESULT
# ============================================================

print("\n" + "=" * 50)
print("                  QUIZ RESULT")
print("=" * 50)

print(f"Total Questions : {total}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {wrong}")
print(f"Score           : {percentage:.2f}%")


# ============================================================
# 8. DISPLAY PERFORMANCE FEEDBACK
# ============================================================

if percentage >= 80:
    print("Excellent!")

elif percentage >= 60:
    print("Good job!")

elif percentage >= 40:
    print("Keep practicing!")

else:
    print("You need more practice.")

print("=" * 50)
