#!/usr/bin/env python3

import wordsiv
import en_markov_gutenberg
import en_wordcount_web

GLYPHS = 'HAMBURGERFONTSIVhamburgerfontsiv'
LOWERS = ''.join(l for l in GLYPHS if l.islower())
UPPERS = ''.join(l for l in GLYPHS if l.isupper())
EN_MK = 'en_markov_gutenberg'
EN_WC = 'en_wordcount_web'
SIZE = (792, 612)
W, H = SIZE
MARGIN = 36
GUTTER = 36
LEFT = MARGIN
RIGHT = W - MARGIN
TOP = MARGIN
BOTTOM = H - MARGIN
# X, Y, W, H format
INNER = (MARGIN, MARGIN, W - MARGIN * 2, H - MARGIN * 2)

# LEFT COLUMN
# X, Y, W, H format
CL = (MARGIN, MARGIN, INNER[2] / 2 - GUTTER / 2, INNER[3])

# RIGHT COLUMN
CR = (MARGIN + INNER[2] / 2 + GUTTER / 2, MARGIN, CL[2], CL[3])

wsv = wordsiv.WordSiv(font_file='noto-sans-subset.ttf')

def spacing_strings_uc(letters):
    """Given a string, return an uppercase spacing string for each character"""
    strings = []
    for l in letters:
        strings.append(f'HH{l}HO{l}OO')
    return '\n'.join(strings)
    
def spacing_strings_lc(letters):
    """Given a string, return a lowercase spacing string for each character"""
    return ''

# This is an uncommon thing: passing modules to functions.
# inside Drawbot package entrypoints don't seem to work correctly,
#    so this is a workaround
# normally the source modules are discovered automatically and don't
#    need to be added
wsv.add_source_module(en_markov_gutenberg)
wsv.add_source_module(en_wordcount_web)

# This allows us to make a call like wsv.paragraph() without specifying a source
wsv.set_default_source(EN_WC)

# PAGE 1
size(SIZE)
font('noto-sans-subset.ttf')
fontSize(100)
lineHeight(100)
textBox(UPPERS + '\n' + LOWERS, INNER)
#textBox(wsv.paragraph(), (10, 10, 400, 400))

# PAGE 2
newPage()
fontSize(20)
lineHeight(24)
txt = spacing_strings_uc(UPPERS)
textBox(txt, CL)

# Modify spacing_strings_lc and print it in the second column

# PAGE 3
newPage()
fontSize(12)
lineHeight(14)
textBox(wsv.text(num_paras=6), CL)

fontSize(10)
lineHeight(12)
txt = wsv.text(max_sent_len=20, num_paras=8)
textBox(txt, CR)

