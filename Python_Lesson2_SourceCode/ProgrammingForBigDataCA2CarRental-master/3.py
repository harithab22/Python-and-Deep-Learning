filename=input("Enter the filename: ")
word_count={}
file=open(filename, 'r')
readfile=file.read().lower()
des = readfile.strip("!()-[]{};:'\,<>./?@#$%^&*_~ ")
desired=des.split()
print (desired)
for i in desired:
    count=word_count.get(i,0)
    word_count[i]=count+1
    print(word_count)
frequency_words=word_count.keys()
print(frequency_words)
for words in frequency_words:
    print(words,word_count[words])
