#Checking  for prime numbers

def is_prime(prime):
    if prime % 2 == 0: #checks if the number is prime
     return "false"
    else: 
     return "true"

print(is_prime(3))