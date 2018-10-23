words = ['cat', 'window', 'defenestrate']

for w in words[:]:
    if len(w) > 6:
        words.append(w)
        print(words)

# nieskonczenie wiele appendów :P
# for w in words:
#     if len(w) > 6:
#         words.append(w)
#         print(words)