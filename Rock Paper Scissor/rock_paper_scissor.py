def rock_paper_scissor(player1,player2,score):
  import random
  import time
  from IPython.display import clear_output

  a=['rock','scissor','paper']
  n1=n2=turn=0
  print("\nLet's play!")

  while(True):
    turn=turn+1
    p1=random.choice(a)
    print(end='',flush=True)
    p2=input(f"\nTurn no {turn}: Enter 1(rock) or 2(paper) or 3(scissor): ")
    clear_output(wait=True)

    #Assigning respective definition to input(p2) given by user
    p2_mapping = {'1': 'rock', '2': 'paper', '3': 'scissor'}
    p2 = p2_mapping.get(p2,p2)

    #Displaying what players put among rock, paper & scissor
    if p2 not in a:
      print('''⚠️Oops! Seems like you put the wrong input.
    Give it correctly in this turn.⚠️''',flush=True)
    elif(p1==p2):
      print(f"👉Haha, We both put {p1}. So score remains the same.👈",flush=True)
    else:
      print(f"👉You put {p2}. I put {p1}.👈",flush=True)
    time.sleep(1)
    print()

    #Giving scores to players based on conditions
    if (p2 not in a) or (p1==p2):
      pass
    elif(p1=='rock' and p2=='scissor'):
      print('👉I got one point👈')
      n1+=1
    elif(p1=='scissor' and p2=='rock'):
      print('👉You got one point👈')
      n2+=1
    elif(p1=='scissor' and p2=='paper'):
      print('👉I got one point👈')
      n1+=1
    elif(p1=='paper' and p2=='scissor'):
      print('👉You got one point👈')
      n2+=1
    elif(p1=='rock' and p2=='paper'):
      print('👉You got one point👈')
      n2+=1
    elif(p1=='paper' and p2=='rock'):
      print('👉I got one point👈')
      n1+=1
    print(f"👉Your score: {n2}, My score: {n1}.👈")

    if(n1==score or n2==score):
      print(f"\n⚠️Winning score i.e., {score} is reached.⚠️")
      break
  return player1 if n1>n2 else player2


#  MAIN PROGRAM
from IPython.display import clear_output
import time

player1="AI"
player2=input("Hey buddy!\nEnter your name: ")
clear_output(wait=True)

print(f"👋 Hi {player2}.👋\nReady to play ROCK-PAPER-SCISSOR with me?!😉")
input(("\nClick enter-button to continue."))
clear_output(wait=True)

print('''⚠️Read instruction carefully⚠️

⚠️ Now you are going to fix the winning score.
For example, if you're fixing the winning score as 𝟑,
The one who first gets 𝟑 𝐩𝐨𝐢𝐧𝐭𝐬 will 𝐰𝐢𝐧 this game.

Note: ⚠️ Maximum winning score is 𝟏𝟎. If you exceed it,
          It'll be considered as 𝟏𝟎 by default.
      ⚠️ Minimum score is 𝟏. It will be considered as 𝟏 by default
          if you put a zero or negative number.
      ⚠️ If you input winning score in 𝐰𝐫𝐨𝐧𝐠 𝐟𝐨𝐫𝐦𝐚𝐭(other than integer),
          It'll be considered as 𝟱 by default.''', flush=True)

while(True):
  try:
    print(end='',flush=True)
    score=int(input("\n\nFix the winning score as integer (number):"))
  except:
    score=5
    print('''
    ⚠️Since you input the winning score in 𝐰𝐫𝐨𝐧𝐠 𝐟𝐨𝐫𝐦𝐚𝐭.
    It's been fixed as 𝟱 by default.⚠️''', flush=True)
    input(("\nClick enter-button to continue."))

  if score>10:
    score=10
    print('''
    ⚠️Since you input the winning score as more than 10.
    It's been fixed as 𝟏𝟎 by default.⚠️''', flush=True)
    input(("\nClick enter-button to continue."))
  elif score<=0:
    score=1
    print('''
    ⚠️Since you input the winning score as less than 1.
    It's been fixed as 𝟏 by default.⚠️''', flush=True)
    input(("\nClick enter-button to continue."))
  clear_output(wait=True)

  print(f'''𝑨𝑻𝑻𝑬𝑵𝑻𝑰𝑶𝑵
  ⚠️𝘕𝘰𝘵𝘦: The one who first get '{score}' points will win this game.⚠️
  ⚠️𝘐𝘯𝘴𝘵𝘳𝘶𝘤𝘵𝘪𝘰𝘯: Enter 𝟏 for '𝐫𝐨𝐜𝐤', 𝟐 for '𝐩𝐚𝐩𝐞𝐫', 𝟑 for '𝐬𝐜𝐢𝐬𝐬𝐨𝐫'.⚠️''', flush=True)

  a=rock_paper_scissor(player1,player2,score) #function call

  print('\nLoading',end=' ')
  for i in range(5):
    print('*',end='')
    time.sleep(1)
  clear_output(wait=True)

  if a==player1:
    print("\nOops! You failed this game. ☹")
  elif a==player2:
    print(f"\n👉Congrats {player2}, You won this game! 😄")
  time.sleep(1)

  temp=input("\nEnter 𝟏 to 𝐩𝐥𝐚𝐲 𝐚𝐠𝐚𝐢𝐧 or any other key to leave: ")
  if temp=='1':
    # Playing again
    clear_output(wait=True)
    print()
  else:
    clear_output(wait=True)
    print(f"Thank you for choosing this game.\nHave a nice day, {player2} :)")
    break # Ending the game
