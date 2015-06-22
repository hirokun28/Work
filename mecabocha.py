#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ababa

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import CaboCha, MeCab, re, pprint
from nltk.corpus import PlaintextCorpusReader

def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

data = {
    u"スクリプト言語":
        {u"Perl": u"パール",
        u"Python": u"パイソン",
        u"Ruby": u"ルビー"},
    u"関数型言語":
        {u"Erlang": u"アーラング",
        u"Haskell": u"ハスケル",
        u"Lisp": u"リスプ"}
    }

# print data # \u30cf\u30b9とか出る

# print pp(data) # Unicode文字をきちんと表示させる用

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

import jptokenizer

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')


reader = PlaintextCorpusReader("./", r'gingatetsudono_yoru.txt',
        encoding='utf-8',
        para_block_reader=read_line_block,
        sent_tokenizer=jp_sent_tokenizer,
        word_tokenizer=jptokenizer.JPMeCabTokenizer())

print ' '.join(reader.words()[220:280])

# print ginga.raw() # 平文表示

# print '/'.join( ginga.words()[0:300] ) # トークン列挙

# ginga_t = Text( w.encode('utf-8') for w in ginga.words() )
# ginga_t.concordance("川") # テキストオブジェクトに変換した後検索する

mecab = MeCab.Tagger('-Ochasen')
sent = u"かれのくるまでまつ".encode('utf-8')
print mecab.parse(sent)

node = mecab.parseToNode(sent)
node = node.next

while node:
    print node.surface, node.feature
    node = node.next

cabocha = CaboCha.Parser('--charset=UTF8')
sent = u"太郎はこの本を二郎を見た女性に渡した".encode('utf-8')
print "\n" + cabocha.parseToString(sent)

