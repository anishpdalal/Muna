from textblob import TextBlob


def generate_cloze_question(sentence, noun_phrase):
    """
     :param sentence: a TextBlob sentence object
     :param noun_phrase: a noun phrase parsed that belongs to a TextBlob sentence object
     Returns a string converted from TextBlob sentence object with the noun phrase missing and the missing noun phrase.
    """
    return clean_up_sentence(sentence).replace(noun_phrase, '_' * len(noun_phrase)), noun_phrase


def clean_up_sentence(sentence):
    """
    :param sentence: a TextBlob sentence object
    Returns a processed string a TextBlob sentence object.
    """
    return sentence.dict['raw'].lower().replace('\n', ' ').strip()


def generate_cloze_questions(text):
    """
     :param text: raw string
     Returns a list of tuples that each contain a sentence with a noun_phrase missing and the noun_phrase itself.
    """
    return [generate_cloze_question(sentence, noun_phrase) for sentence in TextBlob(text).sentences for noun_phrase in
            sentence.noun_phrases]