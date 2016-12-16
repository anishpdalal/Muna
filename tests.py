import time
from textblob import TextBlob
from text import Text

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

    text = Text(TEXT, "Anish")
    assert text.reader == "Anish"
    assert text.text == TEXT
    assert text.recorded_at == time.strftime("%m-%d-%Y %I:%M %p", time.localtime())
    assert "\n" not in text._clean_sentence(SENTENCE)
    assert "--" in text._clean_sentence(SENTENCE)
    assert text._create_cloze_question(SENTENCE, "titular threat") == (
        'the ______________ of the blob has always struck me as the ultimate movie monster: an insatiably hungry, '
        'amoeba-like mass able to penetrate virtually any safeguard, capable of--as a doomed doctor chillingly '
        'describes it--"assimilating flesh on contact.',
        'titular threat')
    assert text.cloze_questions[-1] == (
        "snide comparisons to gelatin be damned, it's a concept with the most devastating of potential consequences, "
        "not unlike the grey goo scenario proposed by technological theorists fearful of"
        " ___________________________________.",
        'artificial intelligence run rampant')

    print("Tests pass!")


run_tests()
