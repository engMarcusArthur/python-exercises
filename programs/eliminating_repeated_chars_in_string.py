print("Type something and I will eliminate the repeated characters", end="")
sentence=input("->")
sentence=sentence.strip()
j=0
sentence1=" "
for i in sentence:
    if sentence1[j]!=i:
        sentence1=sentence1+i
        j+=1
sentence1=sentence1[1:]
print(sentence1)
input() # Just a wating before exit. Press Enter.