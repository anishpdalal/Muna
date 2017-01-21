import time
from textblob import TextBlob


class Text(object):
    """
    A representation of a single unit of text a reader inputs into Muna. This includes methods for automatic cloze
    question generation.
    """

    def __init__(self, text, reader):
        self.text = text
        self.reader = reader
        self.recorded_at = time.strftime("%m-%d-%Y %I:%M %p", time.localtime())

    @staticmethod
    def _clean_sentence(sentence):
        """
        :param sentence: a TextBlob Sentence Object
        :return: A processed string a TextBlob sentence object.
        """
        return sentence.dict['raw'].lower().replace('\n', ' ').strip()

    def _create_cloze_question(self, sentence, noun_phrase):
        """
         :param sentence: a TextBlob sentence object
         :param noun_phrase: a noun phrase parsed that belongs to a TextBlob sentence object
         :return: A string converted from TextBlob sentence object with the noun phrase missing and the missing noun
         phrase.
        """
        return self._clean_sentence(sentence).replace(noun_phrase, '_' * len(noun_phrase)), noun_phrase

    @property
    def cloze_questions(self):
        """
         :return: A list of tuples that each contain a sentence with a noun_phrase missing and the noun_phrase itself.
        """
        return [self._create_cloze_question(sentence, noun_phrase) for sentence in TextBlob(self.text).sentences for
                noun_phrase in sentence.noun_phrases]