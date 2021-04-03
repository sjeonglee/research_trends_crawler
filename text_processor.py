# import nltk tools (natural language processing)
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from collections import Counter


class text_processor():
    def __init__(self):
        self.gram = 1                            # default
        self.stops = stopwords.words('english')  # default

    # def set_stops(self, stop:str):
    #     return
    
    # functions to set variables
    def set_gram(self, gram:int):
        self.gram = gram
    
    # clean the text (tokenize, lower the case, remove the punctuations and stopwords)
    def clean_text(self, text) -> list:
        text_ = text.replace("Open access", "")
        tk = word_tokenize(text_)                     # tokenize the words
        tk = [w.lower() for w in tk]             # lower the case
        tk = [w for w in tk if w.isalpha()]      # remove the punctuations
        tk = [w for w in tk if not w in self.stops]   # remove stopwords
        # tk = self.stemming_the_tokens(tk)               # stemming the tokens
        
        if self.gram == 2:
            return self.tokens_to_2_gram(tk)
        elif self.gram == 3:
            return self.tokens_to_3_gram(tk)
        else:
            return tk

    def stemming_the_tokens(self, tk: list) -> list:     # stemming the tokens if needed
        snowball = SnowballStemmer("english")
        return [snowball.stem(w) for w in tk]

    def tokens_to_2_gram(self, tk) -> list:
        two_gram_tokens = []
        for i in range(len(tk)):
            if i == 0:
                continue
            two_gram_tokens.append(tk[i - 1] + " " + tk[i])
        return two_gram_tokens

    def tokens_to_3_gram(self, tk) -> list:
        three_gram_tokens = []
        for i in range(len(tk)):
            if i == 0 or i == 1:
                continue
            three_gram_tokens.append(tk[i - 2] + " " + tk[i - 1] + " " + tk[i])
        return three_gram_tokens

    # count the frequency and find duplicates
    def word_list_to_frequency(self, word_list: list) -> dict:
        word_freq = [word_list.count(w) for w in word_list]
        return dict(list(zip(word_list, word_freq)))

    # would be the columns of the dataframe
    def word_list_remove_duplicates(self, word_list: list) -> list:
        word_set = set(word_list)
        word_list = list(word_set)
        return word_list