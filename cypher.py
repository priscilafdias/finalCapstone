# This code changes the letters of a message by a key using the Caesar Cypher

key = 15
message = "What if I say I will never surrender ?"

# Letters in the alphabet, upper and lower case
nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')

cypher = ""
for caracter in message:
    # find at which position in the alphabet is the letter
    ind = ord(caracter)
    # If its in the interval of letters (now) upper case
    if nA <= ind <= nZ:
        new_letter = chr((ind + key)%(nZ+1) + ((ind + key)//(nZ+1))*nA)
        # change the letter by the one in the key position
        cypher = cypher + new_letter
    # If its in the interval of letters (now) lower case
    elif ind in range(na, nz + 1):
        new_letter = chr((ind + key)%(nz+1) + ((ind + key)//(nz+1))*na)
        cypher = cypher + new_letter
    # If its not a letter
    else:
        cypher = cypher + caracter


print("Original: ", message)
print("Cypher: ", cypher)


