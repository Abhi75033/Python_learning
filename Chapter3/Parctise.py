# Q1

# hindi_to_english = {
#     "namste": "Hello",
#     "dhanyavaad": "Thank you",
#     "paani": "Water",
#     "ghar": "Home",
#     "dost": "Friend",
#     "kitab": "Book",
#     "accha": "Good"
# }

# word = input("Enter the word to translate: ")

# print(hindi_to_english[word])


# Q2

# s = set()

# for i in range(8):
#     number = int(input(f"Enter the number {i+1}: "))
#     s.add(number)

# for i in s:
#     print(i)


# Q3


# s = set()

# for i in range(18):
#      s.add(i+1)
#      s.add(str(i+1))

# print(s)

d = {}

for i in range(4):
    name = input("Enter Your name: ")
    lang = input("Enter your prefferd language: ")
    d.update({name:lang})

print(d)


