from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

from PIL import Image
import numpy as np

def create_word_cloud(words):
    text = " ".join(jieba.cut(words,cut_all=False,HMM=True))
    wc = WordCloud(
        font_path = "C:\Windows\Fonts\msyhl.ttc",
        max_words=100,
        width=2000,
        height=1200
    )
    wordcloud = wc.generate(text)
    wordcloud.to_file("wordcloud.jpg")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

s = '''
  fff
'''

create_word_cloud(s)
