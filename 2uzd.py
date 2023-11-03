""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

kas ir RSS?

"""
import feedparser

# URL uz RSS plūsmu 

rss_url='https://lv.wikipedia.org/wiki/RSS_protokols'

# iegūsim RSS plūsmas datus
kkk=feedparser.parse(rss_url)

# parāda un jānoformē 

for entry in kkk.entries:
    print("Virsraksts: ", entry.title)
    print("Saite: ", entry.link)
    print('\n')