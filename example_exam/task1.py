import math

docs = [
    "ca cfaehl chris depression faehl obesity reasonable towards towards trend trend writes",
    "cfaehl chris clark ednclark faehl jeffrey kraken writes writes",
    "article chris concerning herringshaw newsgroup personally proposed split tdawson writes",
    "anyone article chris herringshaw know repeat request sorry tdawson writes",
    "article behanna behanna chris get kryptonite money writes",
    "article behanna behanna chris dos ftpnuz says",
    "article article chris chriss silvester wharfie wrat writes",
    "article chris crichmon lines organization richmond seattle university washington writes",
    "apps article chris chudel hudel ps right run servers writes",
    "article behanna behanna chris lmcstst stamos stamos writes",
    "article cfaehl chris darice faehl fred rice writes",
    "brother chris designed egerter graphics graphics library programming toolkit truly wgt wordup",
    "also article best cab chris cosine effect got lines manual writes",
    "article article behanna behanna chris tcora writes",
    "attempt chris close dave dfuller fuller nice verrry writes",
    "article behanna behanna chris completely different eventual outcome tack writes",
    "article chris distribution lines rec sci smith writes",
    "cah chris huey jamie jamie managers people recommended scuglia thanks workspace writes wrote",
    "article best cab chris expert said something ups writes",
    "ago best cab chris gadget got idea least little new wrote years"
]
n = len(docs)
ppmi = lambda x, y: max(math.log2(n*(len([d for d in docs if (x in d and y in d)])/(len([d for d in docs if (x in d)])*len([d for d in docs if (y in d)])))), 0)
print(ppmi("cab", "best"))
print(ppmi("article", "cab"))
print(ppmi("article", "lines"))
