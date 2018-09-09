#!/usr/bin/python

import pdftotext


class PdfReader(object):



    def __init__(self):
        pass


    def extract2Text(self, fileName):
        texts=[]
        with open(fileName, "rb") as f:
            pdf = pdftotext.PDF(f)
             # Iterate over all the pages
        for page in pdf:
            texts.append(page)
        return texts

