#convert into lower case
from textblob import TextBlob
from nltk import word_tokenize, WordNetLemmatizer, ne_chunk, pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

input_str="The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil."
input_str=input_str.lower()
print(input_str)
#removing numbers
#tokenization
stop_words=set(stopwords.words('english'))
tokens=word_tokenize(input_str)
result=[i for i in tokens if not i in stop_words]
print(result)
#stemming
stemming=PorterStemmer()
for word in tokens:
    print(stemming.stem(word))
#lemmatizer
lemmatizer=WordNetLemmatizer()
for word in tokens:
    print(lemmatizer.lemmatize(word))
#parts of speech
result=TextBlob(input_str)
print(result.tags)
#named entity
result=ne_chunk(pos_tag(word_tokenize(input_str)))
print(result)

