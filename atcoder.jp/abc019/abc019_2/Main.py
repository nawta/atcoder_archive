"""
s = 'abc'
t = 'def'

# カンマやタブの前後に空白が入る
print(s, ',', t) # -> abc , def
print(s, '¥t', t) # -> abc ¥t def

# カンマやタブの前後に空白を入れたくない場合はsepに空の文字列を指定
print(s, ',', t, sep='') # -> abc,def
print(s, '¥t', t, sep='') # -> abc¥tdef

# 改行したくない場合はendに空の文字列を指定
print(s, ',', t, sep='', end='') # -> abc,def（改行なし）
print(s, '¥t', t, sep='', end='') # -> abc¥tdef（改行なし）
"""
s = list(input())
count_char=0
head_char=s[0]
for i in range(len(s)):
    if s[i] == head_char:
        count_char +=1
    else:
        print("{}{}".format(head_char, count_char), end = "")
        count_char = 1
        head_char = s[i]
print("{}{}".format(head_char, count_char))