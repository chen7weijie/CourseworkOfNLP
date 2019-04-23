from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
myText="is upset that he can't update his Facebook by texting it... and might cry as a result  School today also. Blah!"
#将句子切分为单词
wordToken=word_tokenize(myText)
#获取停用词
stop_words=stopwords.words('english')
#删除停用词
filtered_words=[w for w in wordToken if not w in stop_words]
#标点符号
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-']
#删除标点符号
filtered2_words=[w for w in filtered_words if not w in english_punctuations]
#输出
print(filtered2_words)

##输出结果：
# ['upset', 'ca', "n't", 'update', 'Facebook', 'texting', '...', 'might', 'cry', 'result', 'School', 'today', 'also', 'Blah']