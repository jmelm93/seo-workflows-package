from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
import pandas as pd

import sys
sys.path.insert(0, '..')

from seoworkflows_lib import UrlCleaning


def run_ngrams(characters, input_list):
    my_additional_stop_words = ['does', 'gets', 'like', 'got']
    characters = characters
    word_vectorizer = CountVectorizer(ngram_range=(characters, characters), analyzer='word',strip_accents = 'unicode' , stop_words=text.ENGLISH_STOP_WORDS.union(my_additional_stop_words))
    sparse_matrix = word_vectorizer.fit_transform(input_list['inputs'])
    frequencies = sum(sparse_matrix).toarray()[0]
    df = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names_out(), columns=['frequency'])
    return df

def url_ngrams(input_list, ngram_type, characters):
    num_of_inputs_allowed = 1000
    try:
        ### Convert series to frame + extracts paths using `data_cleaning` module
        ### Strip URL paths to be singular words - `\.[^.]*$` at the end removes everything aftere the last '.' (e.g., '.html')
        input_list = input_list.drop_duplicates()
        df = input_list.to_frame('inputs')
        df = UrlCleaning(url_list=df['inputs']).get_url_path()
        df["inputs"] = df["paths"].str.replace('.*.com/|/|-|\.[^.]*$', ' ', regex=True)

        all_ngrams = run_ngrams(characters=characters, input_list=df.head(num_of_inputs_allowed))

        all_ngrams = (all_ngrams.reset_index()
                                .sort_values(by=['frequency'], ascending=[False])
                                .rename(columns={'index': 'ngram'}))
        all_ngrams.assign(
            Type= ngram_type,
            ngram_cleaned= all_ngrams["ngram"].str.replace(' ', '-', regex=False)
            )

        all_ngrams = all_ngrams.loc[all_ngrams['frequency'] > int(5)]

        return all_ngrams
    
    except BaseException as e:
        print("UnidentifiedError: {0}".format(e)) 


def query_ngrams(input_list, ngram_type, characters):
    num_of_inputs_allowed = 1000
    try:
        ### Convert series to frame + extracts paths using `data_cleaning` module
        ### Strip URL paths to be singular words - `\.[^.]*$` at the end removes everything aftere the last '.' (e.g., '.html')
        input_list = input_list.drop_duplicates()
        df = input_list.to_frame('inputs')
        # df = UrlCleaning(url_list=df['inputs']).get_url_path()
        # df["stripped"] = df["paths"].str.replace('.*.com/|/|-|\.[^.]*$', ' ', regex=True)

        all_ngrams = run_ngrams(characters=characters, input_list=df.head(num_of_inputs_allowed))
        
        all_ngrams = (all_ngrams.reset_index()
                                .sort_values(by=['frequency'], ascending=[False])
                                .rename(columns={'index': 'ngram'}))
        all_ngrams.assign(
            Type= ngram_type,
            ngram_cleaned= all_ngrams["ngram"].str.replace(' ', '-', regex=False)
            )

        all_ngrams = all_ngrams.loc[all_ngrams['frequency'] > int(5)]

        return all_ngrams
    
    
    except BaseException as e:
        print("UnidentifiedError: {0}".format(e)) 


