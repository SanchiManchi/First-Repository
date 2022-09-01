Week = {'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}
WD = input('What day of the week are you parking your car?')
while WD not in Week:
  WD = input('Please enter valid day:')
if WD in {'Monday','Tuesday','Wednesday','Thursday','Friday'}:
  Day=1
  Rate = 10
if WD in {'Saturday'}:
  Day=2
  Rate = 3
if WD in {'Sunday'}:
  Day=3
  Rate = 2
Hrs = int(input('How many hours are you leaving your car?'))
if Day == 1:
  while Hrs>2:
    Hrs = int(input('Cannot park for so long, input lower number:'))
if Day == 2:
  while Hrs>4:
    Hrs = int(input('Cannot park for so long, input lower number:'))
if Day == 3:
  while Hrs>10:
    Hrs = int(input('Cannot park for so long, input lower number:'))
Arv = int(input('Hour of arrival:'))
while Arv > 23:
  Arv = int(input('Enter valid hour. No minutes. Two digits only:'))
while Arv + Hrs > 24:
  Arv = int(input('Cannot park so late, please pick earlier time:'))
while Arv < 8:
  Arv = int(input('Cannot park so early, please pick a later time:'))
if Day == 1 and Arv > 16:
  Rate = 2
else:
  if Day == 2 and Arv < 16:
    Rate = 3
price = Hrs*Rate
print(price,':Here is your price.')
yn = input("Do you have a code?")
loop = 1
code = []
while loop < 6:
  a = int(input('Input '+ str(loop) +' digit of the code:'))
  code.append(a)
  loop = loop + 1
check = 11-(((code[0]*5) + (code[1]*4) + (code[2]*3) + (code[3]*2))%11)
if check == code[4]:
  price = price/50
  print('Valid code. Discount applied:',price)
else:
  print('Invalid code. Discount not applied')
