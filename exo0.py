peopleneedaride=int(input('how many people need a ride ?'))
peoplefitinthecar=int(input('how many people fit in one car ?'))

nbroftaxis=peopleneedaride//peoplefitinthecar 

if peopleneedaride%peoplefitinthecar==0 :
   print('number of taxis needed',nbroftaxis)
else:
  print('number of taxis needed',nbroftaxis+1)
 