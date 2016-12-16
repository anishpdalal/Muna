from textblob import TextBlob
import question_generator

TEXT = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

SENTENCE = TextBlob(TEXT).sentences[0]


def run_tests():
    """ Need to refactor tests """
    assert "\n" not in question_generator.clean_up_sentence(SENTENCE)
    assert "--" in question_generator.clean_up_sentence(SENTENCE)
    assert question_generator.generate_cloze_question(SENTENCE, "titular threat") == (
        'the ______________ of the blob has always struck me as the ultimate movie monster: an insatiably hungry, '
        'amoeba-like mass able to penetrate virtually any safeguard, capable of--as a doomed doctor chillingly '
        'describes it--"assimilating flesh on contact.',
        'titular threat')
    assert question_generator.generate_cloze_questions(TEXT)[-1] == (
        "snide comparisons to gelatin be damned, it's a concept with the most devastating of potential consequences, "
        "not unlike the grey goo scenario proposed by technological theorists fearful of"
        " ___________________________________.",
        'artificial intelligence run rampant')
    cloze_questions = question_generator.generate_cloze_questions(TEXT)
    assert len(cloze_questions) == 9
    cloze_question, cloze_questions = question_generator.select_random_cloze_question(cloze_questions)
    assert len(cloze_question) == 2
    assert len(cloze_questions) == 8

    print("Tests pass!")


run_tests()
