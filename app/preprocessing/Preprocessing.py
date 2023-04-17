'''Import Libraries'''
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class PreProcessing():
    def __init__(self) -> None:
        nltk.download('punkt')
        self.lemma = WordNetLemmatizer()
        self.stop_words = stopwords.words('english')

    def regular_expression_removal(self, text: str) -> str:
        '''We will not remove other numbers, punctuation marks and special characters from the original text 
        since we will use this original text to create summaries and weighted word frequencies which will then be replaced in this statement.'''
        # Removing Square Brackets and Extra Spaces
        original_statement = re.sub(r'[\[0-9\]]', ' ', text)
        original_statement = re.sub(r'\s+', ' ', text)

        '''To clean the text and calculate weighted frequences, we will create another object.'''
        formatted_statement = re.sub('[^a-zA-Z]',' ', text)
        formatted_statement = re.sub(r'\s+', ' ', text)

        return original_statement, formatted_statement
    
    def lower_case_conversion(self, formated: str) -> str:
        formated_statement = formated.lower()

        return formated_statement
    
    def sentence_conversion(self, original_text: str) -> list:
        sentence_list = nltk.sent_tokenize(original_text)

        return sentence_list
    
    def word_lemmatisation(self, formated: str) -> list:
        formated_statement = [self.lemma.lemmatize(word) for word in formated]

        return ''.join(words for words in formated_statement)

    def sentence_processing(self, text: str) -> str:
        original_text, formatted_text = self.regular_expression_removal(text=text)
        formatted_text = self.lower_case_conversion(formated=formatted_text)
        formatted_text = self.word_lemmatisation(formated=formatted_text)
        original_text_list = self.sentence_conversion(original_text=original_text)

        return original_text_list, formatted_text