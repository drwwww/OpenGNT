# This file is created for merging latest work on OpenGNTGloss and NET2Words into main database file OpenGNT.csv
# rename TANTT database to 'TANTT.csv'
# put 'TANTT.csv' and this script in the same folder
# locate the folder in terminal
# enter command in terminal 'python exportGNT_M.py'

import re

inputFile = 'TANTT.csv'
outputFile = 'GNT_M.csv'

# export latest glosses

f = open(inputFile,'r')
newData = f.read()
f.close()

# clean up
newData = re.sub('\n[\n]+?([^\n])', r'\n\1', newData, flags=re.M)
newData = re.sub(' [ ]+?([^ ])', r' \1', newData, flags=re.M)
newData = re.sub('^ ', '', newData, flags=re.M)
newData = re.sub('\t | \t', '\t', newData, flags=re.M)
newData = re.sub('\A[\d\D]*?\n41_Mat', '41_Mat', newData, flags=re.M)

# mark punctuations
newData = re.sub('^([^\n\t]*?\t[^\n\t]*?\t\t)', r'％\1', newData, flags=re.M)

# mark M variants
newData = re.sub('^([^\n\t]*?\t[^\n\t]*?M)', r'＊\1', newData, flags=re.M)
newData = re.sub('^(.*?\t[^\n\t]*?M[^\n\t\+;]*?=[^\n\t]*?\t)$', r'＠\1', newData, flags=re.M)
newData = re.sub('^[^＠＊].*?\n', '', newData, flags=re.M)

# export M variants
newData = re.sub('^＊(.*?\t).*?\t.*?\t(.*?)\t.*?$', r'\1\2', newData, flags=re.M)
newData = re.sub('^＠(.*?\t).*?[^\n\t]*?M[^\n\t\+;]*?=[<>].*?\n', '', newData, flags=re.M)
newData = re.sub('^＠(.*?\t).*?[^\n\t]*?M[^\n\t\+;]*?=([^\n\t=]*?)=[^\n\t]*?\t$', r'\1\2', newData, flags=re.M)

# tag punctuations
newData = re.sub('^％(.*?\t)(.*?)$', r'\1<punc>\2</punc>', newData, flags=re.M)

# BibleBento format

# book no
newData = re.sub('^41_', '40	', newData, flags=re.M)
newData = re.sub('^42_', '41	', newData, flags=re.M)
newData = re.sub('^43_', '42	', newData, flags=re.M)
newData = re.sub('^44_', '43	', newData, flags=re.M)
newData = re.sub('^45_', '44	', newData, flags=re.M)
newData = re.sub('^46_', '45	', newData, flags=re.M)
newData = re.sub('^47_', '46	', newData, flags=re.M)
newData = re.sub('^48_', '47	', newData, flags=re.M)
newData = re.sub('^49_', '48	', newData, flags=re.M)
newData = re.sub('^50_', '49	', newData, flags=re.M)
newData = re.sub('^51_', '50	', newData, flags=re.M)
newData = re.sub('^52_', '51	', newData, flags=re.M)
newData = re.sub('^53_', '52	', newData, flags=re.M)
newData = re.sub('^54_', '53	', newData, flags=re.M)
newData = re.sub('^55_', '54	', newData, flags=re.M)
newData = re.sub('^56_', '55	', newData, flags=re.M)
newData = re.sub('^57_', '56	', newData, flags=re.M)
newData = re.sub('^58_', '57	', newData, flags=re.M)
newData = re.sub('^59_', '58	', newData, flags=re.M)
newData = re.sub('^60_', '59	', newData, flags=re.M)
newData = re.sub('^61_', '60	', newData, flags=re.M)
newData = re.sub('^62_', '61	', newData, flags=re.M)
newData = re.sub('^63_', '62	', newData, flags=re.M)
newData = re.sub('^64_', '63	', newData, flags=re.M)
newData = re.sub('^65_', '64	', newData, flags=re.M)
newData = re.sub('^66_', '65	', newData, flags=re.M)
newData = re.sub('^67_', '66	', newData, flags=re.M)

# chapter no
newData = re.sub('\t...\.([0-9]+?)\.([0-9]+?)\t', r'\t\1\t\2\t', newData)
newData = re.sub('\t00', '\t', newData)
newData = re.sub('\t0', '\t', newData)

# Greek unicode characters
newData = re.sub('ά', 'ά', newData, flags=re.M)
newData = re.sub('ί', 'ί', newData, flags=re.M)
newData = re.sub('έ', 'έ', newData, flags=re.M)
newData = re.sub('ώ', 'ώ', newData, flags=re.M)
newData = re.sub('ή', 'ή', newData, flags=re.M)
newData = re.sub('ύ', 'ύ', newData, flags=re.M)
newData = re.sub('ό', 'ό', newData, flags=re.M)
newData = re.sub('̓͂Α', 'Ἆ', newData, flags=re.M)
newData = re.sub('̓͂Η', 'Ἦ', newData, flags=re.M)
newData = re.sub('̓͂Ω', 'Ὦ', newData, flags=re.M)
newData = re.sub('ί̈', 'ΐ', newData, flags=re.M)
newData = re.sub('ΐ', 'ΐ', newData, flags=re.M)
newData = re.sub('ΰ', 'ΰ', newData, flags=re.M)
newData = re.sub('[᾿ʼ]', '᾽', newData, flags=re.M)
newData = re.sub('ῇ', 'ῇ', newData, flags=re.M)

# punctuations
newData = re.sub('¶', '¶ ', newData)
newData = re.sub('¬', '‡', newData)

f = open(outputFile,'w')
f.write(newData)
f.close()
