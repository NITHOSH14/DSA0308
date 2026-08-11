def isvowel(w, i):
    c = w[i].lower()
    if c in "aeiou":
        return True
    if c == 'y':
        if i == 0:
            return False
        return not isvowel(w, i - 1)
    return False
def m(s):
    cnt = 0
    pv = False
    for i in range(len(s)):
        if isvowel(s, i):
            pv = True
        else:
            if pv:
                cnt = cnt + 1
            pv = False
    return cnt
def hasvowel(w):
    for i in range(len(w)):
        if isvowel(w, i):
            return True
    return False
def dbc(w):
    if len(w) < 2:
        return False
    a = w[-1]
    b = w[-2]
    if a != b:
        return False
    return not isvowel(w, len(w) - 1)
def cvc(w):
    if len(w) < 3:
        return False
    n = len(w)
    if not isvowel(w, n - 3) and isvowel(w, n - 2) and not isvowel(w, n - 1):
        c = w[-1]
        if c == 'w' or c == 'x' or c == 'y':
            return False
        return True
    return False
def step1a(w):
    if w.endswith("sses"):
        w = w[:-2]
    elif w.endswith("ies"):
        w = w[:-2]
    elif w.endswith("ss"):
        w = w
    elif w.endswith("s"):
        w = w[:-1]
    return w
def step1b(w):
    if w.endswith("eed"):
        s = w[:-1]
        if m(s) > 0:
            w = s + "ee"
            return w
    if w.endswith("ed"):
        s = w[:-2]
        if hasvowel(s):
            w = s
    elif w.endswith("ing"):
        s = w[:-3]
        if hasvowel(s):
            w = s
    if w.endswith("at") or w.endswith("bl") or w.endswith("iz"):
        w = w + "e"
    elif dbc(w) and w[-1] not in "lsz":
        w = w[:-1]
    elif m(w) == 1 and cvc(w):
        w = w + "e"
    return w
def step1c(w):
    if w.endswith("y"):
        s = w[:-1]
        if isvowel(s, len(s) - 1):
            return s + "i"
    return w
def step2(w):
    rules = [
        ("ational", "ate"), ("tional", "tion"), ("enci", "ence"),
        ("anci", "ance"), ("izer", "ize"), ("abli", "able"),
        ("alli", "al"), ("entli", "ent"), ("eli", "e"),
        ("ousli", "ous"), ("ization", "ize"), ("ation", "ate"),
        ("ator", "ate"), ("alism", "al"), ("iveness", "ive"),
        ("fulness", "ful"), ("ousness", "ous"), ("aliti", "al"),
        ("iviti", "ive"), ("biliti", "ble"), ("logi", "log")
    ]
    for old, new in rules:
        if w.endswith(old):
            s = w[:len(w) - len(old)]
            if m(s) > 0:
                w = s + new
            break
    return w
def step3(w):
    rules = [
        ("icate", "ic"), ("ative", ""), ("alize", "al"),
        ("iciti", "ic"), ("ical", "ic"), ("ful", ""), ("ness", "")
    ]
    for old, new in rules:
        if w.endswith(old):
            s = w[:len(w) - len(old)]
            if m(w) > 0:
                s = s + new
            break
    return w
def step4(w):
    suf_list = ["al", "ance", "ence", "er", "ic", "able", "ible",
                "ant", "ement", "ment", "ent", "ion", "ou", "ism",
                "ate", "iti", "ous", "ive", "ize"]
    for suf in suf_list:
        if w.endswith(suf):
            s = w[:len(w) - len(suf)]
            if suf == "ion":
                if m(s) > 1 and (s.endswith("s") or s.endswith("t")):
                    return s
            else:
                if m(s) > 1:
                    return s
    return w
def step5a(w):
    if w.endswith("e"):
        s = w[:-1]
        if m(s) > 1:
            return s
        if m(s) == 1 and not cvc(s):
            return s
    return w
def step5b(w):
    if m(w) > 1 and w.endswith("ll"):
        return w[:-1]
    return w
def stem(word):
    word = word.lower()
    word = step1a(word)
    word = step1b(word)
    word = step1c(word)
    word = step2(word)
    word = step3(word)
    word = step4(word)
    word = step5a(word)
    word = step5b(word)
    return word
word = input("Enter a Word\n")
print("Stemmed Word: " + stem(word))