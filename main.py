import art
import random
import game_data

def generate_user(user):
    user_dictionary = random.choice(game_data.data)
    while user_dictionary == user:
        user_dictionary = random.choice(game_data.data)
    else:
        return user_dictionary

def compare(user_a_followers2, user_b_followers2):
    if choice == "A":
        if user_a_followers2 > user_b_followers2:
            correct_answer_user2 = True
            return correct_answer_user2
        else:
            correct_answer_user2 = False
            return correct_answer_user2
    else:
        if user_b_followers2 > user_a_followers2:
            correct_answer_user2 = True
            return correct_answer_user2
        else:
            correct_answer_user2 = False
            return correct_answer_user2

def user_sentence(user):
    return f"{user["name"]}, a {user["description"]}, from {user["country"]}"

score_user = 0
correct_answer_user = True
user_b = generate_user(None)
print("\n" * 20)
print(art.logo)
while correct_answer_user:
    user_a = user_b
    user_b = generate_user(user_a)
    print(user_sentence(user_a))
    print(art.vs)
    print(user_sentence(user_b))
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    correct_answer_user = compare(user_a["follower_count"], user_b["follower_count"])
    print("\n" * 20)
    print(art.logo)
    if correct_answer_user is True:
        score_user += 1
        print(f"You're right! Current score: {score_user}")
else:
    print(f"Sorry, that's wrong. Final score: {score_user}")
