#Reverse Word Order

def reverse_string(sentence):
    b = sentence.split()
    return " ".join(b[::-1])

user_sentence = str(input("Enter a sentence: "))
print(reverse_string(user_sentence))