import random

numbers = [
  '0',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
]
num_list = []

for char in range(0, 4):
  num_list += random.choice(numbers)
print(num_list)

random.shuffle(num_list)
otp = ""
for char in num_list:
  otp += char

print(f"Your OTP is {otp}.")
