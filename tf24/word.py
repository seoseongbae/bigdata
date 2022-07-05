import random
words=["coffee", "apple","banana"]
word=random.choice(words)
print("answer:"+word)
letters=""
while True:
    suceed=True
    print()
    for w in word:
        if w in letters:
            print(w, end="")
        else:
            print("_",end="")
            suceed=False
    print()
    
    if suceed:
        print("success")
        break
    letter =input("input your letter:")
    if letter not in letters:
        letters+=letter
    if letter in word:
        print("correct")
    else: 
        print("wrong")
