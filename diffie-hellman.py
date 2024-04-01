import random
import math 

n = int(input("Enter a big prime number: "))
g = int(input("Enter a small prime number: "))

# Generate random values for a and b within the range of 1 to n
a = random.randint(1, n)
b = random.randint(1, n)

print("a =", a)
print("b =", b)

a_public = math.pow(g, a) % n
b_public = math.pow(g, b) % n

print("Alice's public variable is: ", a_public)
print("Bob's public variable is: ", b_public)

alice_shared_key = math.pow(b_public, a) % n
bob_shared_key = math.pow(a_public, b) % n

print("Alice's shared key:", alice_shared_key)
print("Bob's shared key:", bob_shared_key)

what_we_know_publicly = math.pow(g, a+b) % n
print("This is what we know publicly: ", what_we_know_publicly)
print("Thus, there is no way we can know the shared keys.")