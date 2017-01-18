# word2vec测试（结合结巴分词）


## 下载并预处理wiki数据

下载地址：https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

1.3G, 2017-01-18

```sh
python3 process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.text
```

## 使用结巴分词

```sh
# 转化为简体
opencc -i wiki.zh.text -o wiki.zh.jian.text -c zht2zhs.ini

# 分词
python3 -m jieba wiki.zh.jian.text > wiki.zh.seg.txt
```

## 训练

训练时间跟数据量有关，在4核4G的个人电脑上花了40分钟。

```sh
python3 train_word2vec_model.py wiki.zh.seg.txt wiki.zh.text.model wiki.zh.text.vector
```

## 应用

```sh
In [1]: import gensim

In [2]: model = gensim.models.Word2Vec.load("wiki.zh.text.model")

In [7]: result = model.most_similar(u"华南理工大学")

In [8]: for e in result:
   ...:     print(e[0], e[1])
   ...:     
华南农业大学 0.8276891708374023
武汉理工大学 0.7900615930557251
华中科技大学 0.7779588103294373
南京师范大学 0.7716870307922363
天津大学 0.7613962292671204
哈尔滨工程大学 0.7611604928970337
大连理工大学 0.7537891864776611
北京航空航天大学 0.7535535097122192
北京科技大学 0.7528501749038696
北京邮电大学 0.7520782351493835

In [9]: result = model.most_similar(u"成龙")

In [10]: for e in result:
    ...:     print(e[0], e[1])
    ...:     
洪金宝 0.6827408075332642
袁和平 0.6666039228439331
李连杰 0.6663515567779541
甄子丹 0.6468013525009155
元华 0.6431161165237427
吴京 0.636760413646698
元彪 0.6305180788040161
周润发 0.6282232403755188
石天 0.6262528896331787
杨紫琼 0.6252658367156982

In [11]: result = model.most_similar(u"广州")

In [12]: for e in result:
    ...:     print(e[0], e[1])
    ...:     
广东 0.673917829990387
广州市 0.631218433380127
佛山 0.6200505495071411
东莞 0.6045597791671753
惠州 0.5955774784088135
番禺 0.594780445098877
深圳 0.5912451148033142
武汉 0.5812212228775024
韶关 0.5760599970817566
广东省 0.5727173089981079

In [13]: model.similarity(u"女人", u"男人")
Out[13]: 0.75362733685219918

In [18]: result = model.most_similar(positive=u"大学", negative=u"广东")

In [19]: for e in result:
    ...:     print(e[0], e[1])
    ...:     
思考 0.27563929557800293
看大 0.27144569158554077
神经病 0.2705303430557251
学习 0.2633955478668213
社会学 0.25695136189460754
界大 0.255343496799469
心理学 0.2538605332374573
犯罪学 0.2534201145172119
断法 0.25285470485687256
学与 0.24832656979560852

In [20]: result = model.most_similar(u"大学")

In [21]: for e in result:
    ...:     print(e[0], e[1])
    ...:     
大学教授 0.6946241855621338
大学校园 0.5735024213790894
理工大学 0.5640472173690796
大学部 0.5624325275421143
国立大学 0.5553818345069885
大学校长 0.5471609830856323
州立大学 0.5435115098953247
学院 0.5330567359924316
综合大学 0.5301772356033325
理工学院 0.5294097661972046
```

## 参考

- http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C
- http://www.cnblogs.com/Newsteinwell/p/6034747.html
- https://github.com/paristsai/word2vec

