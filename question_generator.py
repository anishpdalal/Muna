#!/usr/bin/python
import random
import time
from textblob import TextBlob


def generate_cloze_question(sentence, noun_phrase):
    """

     :param sentence: a TextBlob sentence object
     :param noun_phrase: a noun phrase parsed that belongs to a TextBlob sentence object
     :return: A string converted from TextBlob sentence object with the noun phrase missing and the missing noun phrase.
    """
    return clean_up_sentence(sentence).replace(noun_phrase, '_' * len(noun_phrase)), noun_phrase


def clean_up_sentence(sentence):
    """

    :param sentence: a TextBlob Sentence Object
    :return: A processed string a TextBlob sentence object.
    """
    return sentence.dict['raw'].lower().replace('\n', ' ').strip()


def generate_cloze_questions(text):
    """

     :param text: raw string
     :return: A list of tuples that each contain a sentence with a noun_phrase missing and the noun_phrase itself.
    """
    return [generate_cloze_question(sentence, noun_phrase) for sentence in TextBlob(text).sentences for noun_phrase in
            sentence.noun_phrases]


def select_random_cloze_question(cloze_questions):
    """

    :param cloze_questions: list of cloze questions.
    :return: A random cloze_question from the list of cloze questions and the list of cloze questions.
    """
    cloze_question = random.choice(cloze_questions)
    cloze_questions.pop(cloze_questions.index(cloze_question))
    return cloze_question, cloze_questions


if __name__ == "__main__":
    text = input()
    cloze_questions = generate_cloze_questions(text)
    while cloze_questions:
        print("Generating question...")
        time.sleep(10)
        cloze_question, cloze_questions = select_random_cloze_question(cloze_questions)
        time.sleep(10)
        print(cloze_question[0])
        input()
        time.sleep(10)
        print(cloze_question[1])
    print("End of questioning!")




