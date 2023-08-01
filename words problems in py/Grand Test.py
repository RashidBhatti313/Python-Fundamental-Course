# def find_big_words (n):
#     for word in n:
#         if len(word) > 5:
#             print(word)
            
# random_words1 = ["nation", "night", "news", "negotiation", "newspaper", "nature"]
# find_big_words(random_words1, )

# no = [1,2,3,4,5,6,7,8,9,10]
# def evenodd (no):
#     even = []
#     odd = []
#     for n in no:
#         if n%2 == 0:
#             even.append(n)
#         else:
#             odd.append(n)
#     return even,odd
# print(evenodd(no))

# def find_big_words (n):
#     big_word = []
#     for word in n:
#         if len(word) > 5:
#             big_word.append(word)
#     return big_word
# random_words1 = find_big_words (["nation", "night", "news", "negotiation", "newspaper", "nature"])
# print(random_words1)

# def find_big_words (n):
#     big_word = []
#     for word in n:
#         if len(word) > 5:
#             big_word.append(word)
#     return big_word
# random_words1 = find_big_words(["nation", "night", "news", "negotiation", "newspaper", "nature"])
# print(random_words1)
        
   

# def find_small_words (n):
#     small_words = []
#     for word in n:
#         if len(word) < 6:
#             small_words.append(word)
#     return small_words
# random_words1 = find_small_words(["nation", "night", "news", "negotiation", "newspaper", "nature"])
# print(random_words1)


# def find_two_words (n):
#     two_words = []
#     for word in n:
#         if len(word) <= 2:
#             two_words.append(word)
#     return two_words
# random_words1 = find_two_words(["n", "ni", "ne", "negotiation", "newspaper", "nature"])
# print(random_words1)

# def find_four_words (n):
#     four_words = []
#     for word in n:
#         if len(word) <= 4:
#             four_words.append(word)
#     return four_words
# random_words1 = find_four_words(["nation", "night", "news", "negotiation", "newspaper", "nature"])
# print(random_words1)

# Question 3

def factor_check(n):
    if n%3 == 0 and n%5 == 0:
        return "Perfect"
    elif n%3 == 0:
        return "Trio"
    elif n%5 == 0:
        return "Pent"
    else:
        return "Zip"
print(factor_check(10))
print(factor_check(9))
print(factor_check(15))
print(factor_check(8))

# question 4:

distance_walked = 0
workoutday = 1
ask_distance = "Enter how many kilometer you walked: "
while workoutday <= 5:
    walked_today = int(input(ask_distance))
    distance_walked += walked_today
    print(distance_walked)

    workoutday +=1


