# bert_weibo_two_classification
Bert model solve WeiBo(social platform in China) emotion anaylsis task by fine-tuning.

# data_set
Two classification data set, label is 0(negative) and 1(positive):
https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k/intro.ipynb

# pretrain_model
https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip

# running
Before running, you should be care for your path of data set and model files, then change 
these params in weibo_bert.sh
```sh weibo_bert.sh``` 
