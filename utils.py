import re
import string
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot

# Global Variables
sent_length= 5000
voc_size = 10000

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

def get_encoded_text(articletext):
    corpus = articletext
    corpus = wordopt(articletext)
    corpus = " ".join(corpus.split())
    ans = []
    ans.append(corpus)
    onehot_repr=[tf.keras.preprocessing.text.one_hot(words, voc_size) for words in ans] 
    embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
    return embedded_docs

# corpus = "My Text of Article"
# print(corpus)
# corpus = wordopt(corpus)
# corpus = " ".join(corpus.split())
# print(corpus)
# ans = []
# ans.append(corpus)
# print(ans)


# onehot_repr=[tf.keras.preprocessing.text.one_hot(
#     words, voc_size) for words in ans] 
# onehot_repr

# embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
# print(embedded_docs)

# predict = loaded_model.predict_classes(embedded_docs)
# print(predict)