from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Replace with your details
FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class RequestModel(BaseModel):
    data: List[str]

def is_number(s: str) -> bool:
    return s.isdigit()

def is_alphabet(s: str) -> bool:
    return s.isalpha()

@app.post("/bfhl")
def process_data(req: RequestModel):
    data = req.data
    even_numbers, odd_numbers, alphabets, special_characters = [], [], [], []
    total_sum = 0
    concat_chars = []

    for item in data:
        if is_number(item):
            num = int(item)
            total_sum += num
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif is_alphabet(item):
            alphabets.append(item.upper())
            concat_chars.append(item)  # collect for concat_string
        else:
            special_characters.append(item)

    # ✅ Corrected concat_string logic
    # Flatten all alphabet strings into one long string
    all_alpha_chars = "".join(concat_chars)
    reversed_chars = all_alpha_chars[::-1]

    concat_string = "".join(
        ch.upper() if i % 2 == 0 else ch.lower()
        for i, ch in enumerate(reversed_chars)
    )

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }

# Optional: Add GET route so browser shows a message instead of 405
@app.get("/")
def home():
    return {"message": "API is live. Use POST /bfhl with JSON body."}
