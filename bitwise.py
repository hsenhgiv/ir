import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['this is the first document',
        'this document is second document',
        'and this is third one',
        'is this first document']
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(corpus)
print("fit transform is")
print(x.toarray())

df=pd.DataFrame(x.toarray(),columns=vectorizer.get_feature_names_out())
print("the generated data frame is")
print(df)

alldata=df[(df['this']==1)&(df['first']==1)]
print("indices where this and first term are present in ", alldata.index.tolist())

ordata=df[(df['this']==1)|(df['first']==1)]
print("indices where either this and first term are present in ", ordata.index.tolist())

notdata=df[(df['and']!=1)]
print("indices where not and present in ", notdata.index.tolist())
