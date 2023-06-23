# # string concatenation 

# youtuber = "Jake hope" #some string variable

# #different ways to do it 
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adjective = input("Adjective:")
typeofbird = input("Name of a bird:")
room = input("type of room:")
verbpast = input("Verb (past tense):")
verb = input("verb:")

madlib = f"It was a {adjective}, cold November day.\nI woke up to the {adjective} smell of {typeofbird} roasting in {room}\
the downstairs. \nI {verbpast} down the stairs to see if I could help {verb}"

print(madlib)