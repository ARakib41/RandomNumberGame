import random
num=0

def generate_random_number():
  return(random.randint(0,1000))

generate_random_number()

def difference_from_answer(guess,answer = generate_random_number()):
  
  if guess == answer:
    print ("Guessed Correctly")
  elif guess > answer:
    print ("Too high")
  else:
    print ("Too low")

difference_from_answer(10)