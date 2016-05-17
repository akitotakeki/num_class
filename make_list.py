#!/usr/bin/python
# coding: UTF-8
import os

train_list = './train'
test_list = './test'

f1 = open('train.txt','w')

for dirpath, _, filenames in os.walk('./train'):
  for idx, filename in enumerate(filenames):
    f1.write(filename + " " + filename[0] + '\n')

f1.close()

f2 = open('test.txt','w')

for dirpath, _, filenames in os.walk('./test'):
  for idx, filename in enumerate(filenames):
    f2.write(filename + " " + filename[0] + '\n')

f2.close()
