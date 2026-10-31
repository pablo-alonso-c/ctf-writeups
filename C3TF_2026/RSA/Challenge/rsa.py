import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime
import base64

flag = b"C3TF{---CENSURADO---}"

p = getPrime(128)
q = getPrime(128)
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)
n = p * q

enc = pow(int.from_bytes(flag, "big"), e, n)

print(f"n: {n}")
print(f"e: {e}")
print(f"enc: {enc}")