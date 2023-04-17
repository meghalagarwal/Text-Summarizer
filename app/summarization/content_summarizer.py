'''Import Libraries'''
import pandas as pd
import nltk
import heapq
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Summarizer():
    def __init__(self) -> None:
        self.lemma = WordNetLemmatizer()
        self.stop_words = stopwords.words('english')
        self.word_freq = {}
        self.sent_score = {}

    def weighted_frequency(self, formated_text: str) -> dict:
        '''This function will calculate the weighted frequency of all the words in the content'''
        for word in nltk.word_tokenize(formated_text):
            if word not in self.stop_words:
                if word not in self.word_freq.keys():
                    self.word_freq[word] = 1
                else:
                    self.word_freq[word] += 1
        
        max_freq = max(self.word_freq.values())

        for word in self.word_freq.keys():
            self.word_freq[word] = (self.word_freq[word]/max_freq)

        return self.word_freq
    
    def sentence_scoring(self, original_list: list, word_frequency: dict) -> dict:
        '''This function will calculate the scores of individual snetences in the content'''
        for sentence in original_list:
            for word in nltk.word_tokenize(sentence.lower()):
                if self.lemma.lemmatize(word) in word_frequency.keys():
                    if len(sentence.split(' ')) < 50:
                        if sentence in self.sent_score.keys():
                            self.sent_score[sentence] += word_frequency[self.lemma.lemmatize(word)]
                        else:
                            self.sent_score[sentence] = word_frequency[self.lemma.lemmatize(word)]

        return self.sent_score
    
    def summary(self, original_list: list, formated_text: str) -> None:
        '''This function will print the summary of the provided content'''
        word_freqency = self.weighted_frequency(formated_text=formated_text)
        sentence_scores = self.sentence_scoring(original_list=original_list, word_frequency=word_freqency)
        sentence_summary = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

        print(''.join(sentence_summary))