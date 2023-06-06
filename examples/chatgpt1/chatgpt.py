# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import os

import openai
from dotenv import find_dotenv, load_dotenv


def get_completion(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def generate_question() -> str:
    return "What is the capital of France?"


def main():
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ["OPENAI_API_KEY"]

    response = get_completion(generate_question())
    print(response)


if __name__ == "__main__":
    main()
