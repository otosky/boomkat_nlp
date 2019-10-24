# NLP on Boomkat Product Descriptions
or "Exploring Sub-Genres in House/Techno through NLP"

## Overview

Writing about the qualities of music is hard. It requires a familiarity with stylistic 
idiosyncrasies but also a knack for translating the *the way one feels* when hearing
a piece of music. 

This project aims to demonstrate an exploratory way to develop 
a descriptive vocabulary for different musical styles - specifically, sub-genres
of House & Techno music - by performing Topic-Modeling and Parts-of-Speech tagging
on product descriptions of albums sold on [Boomkat.com](https://www.boomkat.com).

## Use-Case

The end-user could be a copy-writer, trying to gain inspiration for how to describe
these various sub-genres.  The framework outputs could also be the basis of a recommendation
system *e.g. show me more music that's descriptively "metallic" or "grinding", etc.*  It 
could also make a helpful ear-training tool for those looking to map words to music.

My inspiration really just stemmed from having released half an EP on a 
friend's record label and feeling like we were lacking a nuanced vocab when we
were writing the press release. :sweat_smile:

## Data

I scraped every release under the House/Techno section of [Boomkat.com](https://www.boomkat.com) in August 2019.

Of the 800,000+ releases, only around 11,000 or so had text product descriptions.  Their 
knack for humor and really-long-hyphenated-compound-words made them a good candidate as 
a datasource.  I think they write pretty exemplary and vivid blurbs.

image example

Other metadata like 'title', 'artist', 'catalog number, and 'release-date' were also 
collected.

## Modeling

Topic-modeling was fairly straightforward:

- run the corpus through a TF-IDF vectorizer
- decompose the document-term matrix with NMF using 13 topics

Choosing NMF and hyper-parameters was an iterative process, guided predominantly
by my own interpretation of topic coherence.  The finesse of the results actually
had less to do with finding the right number of topics as it did with continually
building a bigger stop-word list and setting a maximum document frequency of 20%
to the TF-IDF Vectorizer. It was a pretty hands-on rinse and repeat situation.

To provide an example, words like "reissue", "remastered", "vinyl", and "exclusive" 
have little to do with my use-case - musical style - so I could safely strip them out from my
corpus vocabulary.

## Post-Processing

Accurate Parts-of-Speech (POS) tagging requires your documents to retain their original 
grammatical structure, i.e. not a bag-of-words.  So before filtering the top-words per 
topic, I created a subset of my vocabulary by passing the original corpus to 
TextBlob for POS tagging and tokenization.

From there I was able to easily filter the top-words per topic to just contain 
adjectives and adverbs, specifying even further that they only end in:
- "-ic"
- "-ing"
- "-ed"
- "-y".

## Results
Of the 13 topics that I factored the doc-term matrix on, 10 were pretty clear-cut 
styles to me:

- "INDUSTRIAL/EBM/NOISE"
- "CHICAGO/JACKING/ACID"
- "CLASSIC DETROIT"
- "DISCO/FUNK/ITALO"
- "ELECTRO/SCI-FI"
- "MINIMAL/TECH-HOUSE"
- "DEEP/SOULFUL-HOUSE"
- "DUB/BASIC CHANNEL"  
- "UKG/BREAKBEAT"
- "BIG ROOM"

There were 3 that were more like guess-timates:
- "TRAX-IN-TITLE"
- "maybe boring?"
- "UNSURE/generic"

Here's a sample of some of the descriptive differences between 3 sub-genres:

Industrial | Classic/Detroit | UKG/Breakbeat
--------|--------------------|---
dry     |  classy            | swing
metallic|  funked            | rolling
heavy   |  sophisticated     | swinging
hypnotic|  stripped          | rugged    
stripped|  booty             | clipped
droning |  tracky            | heavy
pounding|  influenced        | percolating
roiling |  uplifting         | gritty

Additionally, the notebook details the top releases for each topic, so that you can 
visit the URLs and get a preview of the audio for these sub-genres and learn to 
associate word to sound!
