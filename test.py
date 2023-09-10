#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : test.py
# @Time    : 9/10/23 10:04
# @Author  : zlhhh
# @Description :

from llama_index import download_loader

WikipediaReader = download_loader("WikipediaReader")

from llama_index import WikipediaReader
loader = WikipediaReader()

documents = loader.load_data(
    pages=["歼-16"], auto_suggest=False
)


for document in documents:
    print(document.text)