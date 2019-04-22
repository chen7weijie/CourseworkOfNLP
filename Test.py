from nltk.corpus import wordnet as wn
cat = wn.synset('cat.n.01')
dog = wn.synset('dog.n.01')
i=dog.path_similarity(cat)
#计算单词cat与dog之间的语义相似度
print(i)