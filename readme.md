# word2vec测试


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

这个跟数据量有关，很慢很慢。。。

```sh
python3 train_word2vec_model.py wiki.zh.seg.txt wiki.zh.text.model wiki.zh.text.vector
```


## 参考

- http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C
- http://www.cnblogs.com/Newsteinwell/p/6034747.html

