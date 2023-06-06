# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from examples.chatgpt1.chatgpt import generate_question


def test_generate_question() -> None:
    question = generate_question()
    assert question == "What is the capital of France?"
