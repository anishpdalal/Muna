#!/usr/bin/python
import random
import time
from text import Text

if __name__ == "__main__":
    user_input = input()
    text = Text(user_input, "Anish")
    cloze_questions = text.cloze_questions
    while cloze_questions:
        print("Generating question...")
        time.sleep(10)
        cloze_question = random.choice(cloze_questions)
        time.sleep(10)
        print(cloze_question[0])
        input()
        time.sleep(10)
        print(cloze_question[1])
        cloze_questions.pop(cloze_questions.index(cloze_question))
    print("End of questioning!")




