import ciphers
from collections import Counter
#scipy chi^2 test

cipher_text = ciphers.caesar_cipher_encrypt("hello world", "a")
print(Counter(cipher_text))