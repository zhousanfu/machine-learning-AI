from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json, os



# sentences = [
#     'I love my dog',
#     'I love my cat',
#     'You love my dog!',
#     'Do you think my dog is amazing'
# ]

# # 1.令牌生成器，为单词编号；
# tokenizer = Tokenizer(num_words = 100, oov_token="<oov>")
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index
# sequces = tokenizer.texts_to_sequences(sentences)

# # 2.填充器
# padded = pad_sequences(sequces, padding='post', maxlen=5)

# print(word_index)
# print(sequces)
# print(padded)

with open(os.path.join('data', 'sarcasm.json'), 'r') as f:
    datastore = json.load(f)


sentences = []
labels = []
urls = []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

# 1.令牌生成器，为单词编号；
tokenizer = Tokenizer(oov_token="<oov>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequces = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequces, padding='post')
print('word_index len = ', len(word_index))
print(sentences[2], '\n', padded[2], '\n', padded.shape)
