import pandas as pd
from wordcloud import WordCloud
import random
import matplotlib.pyplot as plt

def m():
    rand=[]
    while len(rand)<3:
        x = random.randint(0, 58)
        if x not in rand:
            rand.append(x)

    s=pd.read_csv('food.csv')
    today=s.iloc[rand,:]

    text=''
    for i in today["all"]:
        text=text+''.join(i)
    text=text.replace('、',',')


    w=WordCloud(max_words=200,font_path=r'vv.otf'
                ,scale=4
                ,height=100
                ,width=400
                ,prefer_horizontal=0.5
                ,min_font_size=18
                ,max_font_size=30
              ).generate(text)

    return  today,w
if __name__ == '__main__':
    m()