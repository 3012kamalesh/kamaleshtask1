string1=str(input('enter the words'))
vowel="aeiou"
count=0
for i in string1:
    if i not in vowel:
        count+=1
print("consontant are",count)
