from nltk import word_tokenize,WordNetLemmatizer,ne_chunk, pos_tag
from nltk.stem import PorterStemmer
input="Former President Brack Obama will speak to young people at the University of Chicago on Monday.returning to the city for what will be his first public event since leaving the White house"
tokens=word_tokenize(input)
print(tokens)
stemmer=PorterStemmer()
lemmatizer=WordNetLemmatizer()
print(stemmer.stem(input))
print(lemmatizer.lemmatize(input))
print("pos")
result=print(pos_tag(tokens))
print("ne")
print(ne_chunk(pos_tag(tokens)))
