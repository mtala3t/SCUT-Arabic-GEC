# coding=utf-8

import random
from random import randint
import re
import textwrap
import re
import nltk
import csv


def genarate_data(filname):
    output_data = []
    with open("../data/" + filname, "r", encoding="utf-8") as input_file:
        for line in input_file:
            for sen in nltk.sent_tokenize(line):
                output_data.append(sen)

    return output_data

# Data source file
output_data = genarate_data("alkhaleej.txt")

# Clean and split the sentences using NLTK
file = open("../data/cleandataset.txt", "w", encoding="utf-8")
for listitem in output_data:
    file.write("%s\n" % listitem)

# Delete a character in the word
def del_char(c_word):
    wrd_list = []
    wrd_list = list(c_word)
    if len(wrd_list) > 2:
        wrd_list.remove(random.choice(wrd_list))

    NewWord = ''.join(wrd_list)

    return NewWord


# Duplicate a character in the word
def add_char(c_word):
    wrd_list = []
    wrd_list = list(c_word)
    if len(wrd_list) > 2:
        rnd_letter = random.choice(wrd_list)
        wrd_list.insert(randint(0, len(wrd_list)), rnd_letter)

    NewWord = ''.join(wrd_list)

    return NewWord

# Delete a word in the sentence
def del_word(sentense):
    sent_list_d = re.sub("[^\w]", " ", ''.join(sentense)).split()

    word_list = list(sent_list_d)

    sent_list_d.remove(random.choice(word_list))

    New_dSentence = ' '.join(sent_list_d)

    sent_list_d = 0

    return New_dSentence

# Delete a word in the sentence
def add_word(sentense):
    sent_2list = re.sub("[^\w]", " ", ''.join(sentense)).split()

    rnd_word_ = random.choice(sent_2list)
    intarr = sent_2list.index(rnd_word_)

    sent_2list.insert(intarr + 1, rnd_word_)

    NewaddwSentence = ' '.join(sent_2list)

    sent_2list = 0

    return NewaddwSentence


# Generate less fluent training set
def less_fluent(sentense):
    main_sent_list = re.sub("[^\w]", " ", ''.join(sentense)).split()

    for x in range(4):
        rnd_2word = random.choice(main_sent_list)
        itmidex = main_sent_list.index(rnd_2word)
        main_sent_list[itmidex] = add_char(rnd_2word)

    for x in range(4):
        rnd_2word = random.choice(main_sent_list)
        itmidex = main_sent_list.index(rnd_2word)
        main_sent_list[itmidex] = del_char(rnd_2word)

    main_newsentence = ' '.join(main_sent_list)
    main_sent_list = 0
    sentense = add_word(main_newsentence)
    sentense = del_word(sentense)

    return sentense

input_data_path = "../data/cleandataset.txt"


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


x = file_len(input_data_path)


def GetFileData(input_path):
    output_src = []
    output_tgt = []
    output_src_ = []
    output_tgt_ = []
    i = 0

    with open(input_path, "r", encoding="utf-8") as input_file:
        x = file_len(input_path)
        x1 = int(0.9 * x)
        y1 = int(x - x1)

        for line in input_file:
            line = line.strip()

            if i > y1:
                if len(line) > 100:
                    wrap_list = textwrap.wrap(line, 100)
                    output_src.append(less_fluent(wrap_list))
                    wrap_list = ' '.join(wrap_list)
                    output_tgt.append(wrap_list)
            else:
                if len(line) > 100:
                    wrap_list = textwrap.wrap(line, 100)
                    output_src_.append(less_fluent(wrap_list))
                    wrap_list = ' '.join(wrap_list)
                    output_tgt_.append(wrap_list)

            i = i + 1

    return output_src, output_tgt, output_src_, output_tgt_


output_train_src, output_train_tgt, output_val_src, output_val_tgt = GetFileData(input_data_path)


# Generate CSV training file
with open("../data/SCUT_train_V3.csv", "w", encoding="utf-8", newline='') as f:
    fieldnames = ['src', 'trg']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(0, len(output_train_src)):
        thewriter.writerow({'src':  output_train_src[i], 'trg': output_train_tgt[i]})


# Generate CSV validation file
with open("../data/SCUT_vali_V3.csv", "w", encoding="utf-8", newline='') as f:
    fieldnames = ['src', 'trg']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(0, len(output_val_src)):
        thewriter.writerow({'src':  output_val_src[i], 'trg': output_val_tgt[i]})

