'''Import Libraries'''
import numpy as np
import pandas as pd
import pprint as pp
import bs4 as bs
import urllib.request
from preprocessing.Preprocessing import PreProcessing
from summarization.content_summarizer import Summarizer

class Text_Summarizer():
    def __init__(self) -> None:
        self.preprocess = PreProcessing()
        self.summary = Summarizer()

    def data_download(self, topic_name: str) -> str:
        try:
            wikipedia_cotent = urllib.request.urlopen(f"https://en.wikipedia.org/wiki/{topic_name.replace(' ', '_')}")
            content = wikipedia_cotent.read()

            parsed_article = bs.BeautifulSoup(content, 'lxml')
            paragraph = parsed_article.findAll('p')
            article = ''
            for content in paragraph:
                article += content.text

            return article
        except Exception as e:
            print(f'Topic {topic_name} cannot be found on wikipedia.')

    def data_pre_processing(self, article: str):
        original_text_list, formatted_text = self.preprocess.sentence_processing(text=article)

        return original_text_list, formatted_text
    
    def final_summary(self, original_content_list: list, formatted_content_text: str) -> None:
        self.summary.summary(original_list=original_content_list, formated_text=formatted_content_text)

if __name__ == "__main__":
    start_app = Text_Summarizer()

    topic = input('Kindly provide the topic name of whose summary you would like to know?\n')
    content = start_app.data_download(topic)

    original_content_list, formatted_content = start_app.data_pre_processing(content)

    start_app.final_summary(original_content_list=original_content_list, formatted_content_text=formatted_content)