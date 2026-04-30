import math

# lines, organization, article, world
docs = [
    "world",
    "world",
    "world",
    "lines organization world",
    "lines organization world",
    "article lines organization world",
    "article organization world",
    "world",
    "world",
    "world"
    "",
    "article world",
    "lines world",
    "world",
    "lines world",
    "article world",
    "world",
    "article world",
    "world",
    "world",
    ""
]

n = len(docs)
print(n)
def ppmi(x, y):
    global docs, n
    cxy = len([d for d in docs if (x in d and y in d)])
    cx = len([d for d in docs if (x in d)])
    cy = len([d for d in docs if (y in d)])
    print(cx, cy, cxy)
    return math.log2(n*cxy/(cx*cy))

print(ppmi("lines", "organization"))
print(ppmi("article", "world"))
print(ppmi("world", "organization"))
