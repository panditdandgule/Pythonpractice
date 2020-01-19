# Caesar's Cipher is a very famous encryption technique used in cryptography. It is a type of substitution
# cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down
# the alphabet. For example, with a shift of 3, D would be replaced by G, E would become H, X would become A
# and so on.
#
# Encryption of a letter X by a shift K can be described mathematically as
# EK(X)=(X+K) % 26.
#
# Given a plaintext and it's corresponding ciphertext, output the minimum non-negative value of shift that was
# used to encrypt the plaintext or else output −1 if it is not possible to obtain the given ciphertext from
# the given plaintext using Caesar's Cipher technique.
#
# Input:
#
# The first line of the input contains Q, denoting the number of queries.
#
# The next Q lines contain two strings S and T consisting of only upper-case letters.
#
# Output:
#
# For each test-case, output a single non-negative integer denoting the minimum value of shift that was used
# to encrypt the plaintext or else print −1 if the answer doesn't exist.
#
# Constraints:
# 1≤Q≤5
# 1≤|S|≤10^5
# 1≤|T|≤10^5
# |S| = |T|
#
# SAMPLE INPUT
# 2
# ABC
# DEF
# AAA
# PQR
#
# SAMPLE OUTPUT
# 3
# -1

tests = int(input().strip())
for i in range(tests):
    plain = input().strip()
    cipher = input().strip()
    shift = (ord(cipher[0])-ord(plain[0])+26)%26
    valid = True
    for j in range(len(plain)):
        if (ord(cipher[j])-ord(plain[j])+26)%26 != shift:
            valid = False
            break
    print(shift) if valid else print("-1")