!pip install gensim

# Gensim: It is an open source library in python written by Radim Rehurek which is used in unsupervised topic modelling and natural language processing. It is designed to extract semantic topics from documents. It can handle large text collections.

import gensim
import os


from nltk import sent_tokenize
from gensim.utils import simple_preprocess

story=[]
for filename in os.listdir('C:\\Users\\PARUL\\OneDrive\\Desktop\\gameofthrons'):
    f= open(os.path.join("C:\\Users\\PARUL\\OneDrive\\Desktop\\gameofthrons" , filename))
    corpus = f.read()
    raw_sent= sent_tokenize(corpus)
    for sent in raw_sent:
        story.append(simple_preprocess(sent))


len(story)

model=gensim.models.Word2Vec(
    window=10,
    min_count=2)

model.build_vocab(story)


model.train(story ,total_examples= model.corpus_count ,epochs =model.epochs)

model.wv.most_similar('daenerys')

model.wv.doesnt_match(['jon','rikon','arya','sansa','bran'])

model.wv.doesnt_match(['cersei','jaime','bronn','tyrion'])

model.wv['jon']

model.wv['king'].shape

model.wv.similarity('arya','sansa')

model.wv.similarity('tywin','sansa')

model.wv.get_normed_vectors().shape

y=model.wv.index_to_key

from sklearn.decomposition import PCA

pca= PCA(n_components=3)

x=pca.fit_transform(model.wv.get_normed_vectors())

x[:5]

import plotly.express as px 
fig =px.scatter_3d(x[:500],x=0,y=1,z=2,color =y[:500])
fig.show()

