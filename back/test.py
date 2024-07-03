import re
from collections import Counter
import math
from pprint import pprint
from celery import shared_task
from files.models import File, Word


def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text


def calculate_tf(text, file_instance):
    text = preprocess_text(text)
    words = text.split()
    words_count = len(text.split())
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        tf = count/words_count
        obj = File.objects.create(word=word, tf=tf)
        obj.it_is_found_in.add(file_instance)
    


def calculate_df(text):
    pass


def calculate_idf(text):
    pass


@shared_task
def mod_file(file_id):
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = True
    file_path = file_instance.file.path
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tf = calculate_tf(text)
    file_instance.save()
