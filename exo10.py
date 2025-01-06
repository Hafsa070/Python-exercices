word=input('please type in a word : ')
is_palind=True

for i in range(len(word)//2):
   if word[i]!=word[-(i+1)]:
       is_palind=False
       break


if is_palind==True :
    print('the word is palind')
else:
    print('the word is not palind')