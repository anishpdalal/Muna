#!/usr/bin/python
import random
import time
from text import Text

TEXT = """J.J. Barea is expected to miss several games after straining his left calf for the third time this season.
         "Same calf, different area," Mavs coach Rick Carlisle said. "Just unlucky. It's going to be a while.
          It's going to be likely weeks and not days."
       """

if __name__ == "__main__":
    text = Text(TEXT, "Anish")
    cloze_questions = text.cloze_questions
    while cloze_questions:
        print("Generating question...")
        cloze_question = random.choice(cloze_questions)
        time.sleep(3)
        print(cloze_question[0])
        time.sleep(5)
        print(cloze_question[1])
        cloze_questions.pop(cloze_questions.index(cloze_question))
    print("End of questioning!")
