import pandas as pd
import project4 as pro
import spacy
from spacy.tokenizer import Tokenizer
import re
from nltk.stem import PorterStemmer

ps = PorterStemmer()

data = pd.DataFrame(pro.play.start())
data.columns  = ['title','detail']
detail_list = [i for i in data['detail']]
nlp = spacy.load("en_core_web_sm")
tokenizer = Tokenizer(nlp.vocab)
all_tokens = []
for doc in tokenizer.pipe(data['detail']):
    tokens = []
    for token in doc:
        if (token.is_stop == False) & (token.is_punct == False):
            doc_tokens = re.sub(r"[^a-z0-9]", "", token.text.lower().strip())
            tokens.append(ps.stem(doc_tokens))
        
    all_tokens.append([i for i in tokens if (i!='') and (len(i)>2)])

breakpoint()
print('data')
