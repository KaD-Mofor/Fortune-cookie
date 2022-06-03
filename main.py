import random

luckyNum = random.randint(1,100)
fortune_Num = random.randint(1,5)
fortune_Text = ""

if fortune_Num == 1:
  fortune_Text = 'You will have a great day today'
elif fortune_Num == 2:
  fortune_Text = 'You will have a tough day ... but it will be worth it'
elif fortune_Num == 3:
  fortune_Text = 'You will get married this year :)'
elif fortune_Num == 4:
  fortune_Text = 'You will get a promotion at work'
else:
  fortune_Text = 'Your happiness is within. Joy and Peace will be yours this season.'


print(f"{fortune_Text}. Your lucky number is {luckyNum}.")
    