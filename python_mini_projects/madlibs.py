# string concatenation(putting strings  togethor)

# youtuber ="mani" # empty string

# print(youtuber)

# # few ways to handle it

# print("please subscribe to "+ youtuber)
# print("please subscribe to {}".format(youtuber))
# print(f"please subscribe to {youtuber}") 

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")


madlib = "Computer programming is so {adj}! It makes me so excited all \
the time because I love to {verb1}. Stay hydrated and {verb2} like you are \
{famous_person}".format(adj=adj, verb1=verb1, verb2=verb2, famous_person=famous_person)
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)