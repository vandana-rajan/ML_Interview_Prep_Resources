# 1. Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

x = [1234, 3241, 45678, 78456, 87654]
y = [l*-1 for l in x]

def rev_digit(inp):
    # convert inp to string
    inp_str = str(inp)
    # if positive number
    if inp > 0:
        print("positive")
        return int(inp_str[::-1])
    # if negative number
    elif inp < 0:
        print("negative")
        inp_str = inp_str[1:]
        return -1*int(inp_str[::-1])

# 2. For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.


sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def avg_wrd_len(s):
    for p in ",:.!?''":
        s = s.replace(p," ")
    words = s.split()    
    return round(sum(len(word) for word in words)/len(words),2)

out = avg_wrd_len(sentence1)
print(out)

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

num1 = '1234'
num2 = '100'

eval(num1) + eval(num2)

# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

strng = "mmy name is Vandana"

def solution(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1
