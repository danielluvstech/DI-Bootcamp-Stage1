# Exercise 1 : What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.


# display_message = "Hi Everyone, I'm learning Python!"
# print(display_message)

# Exercise 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

# def favorite_book(title):
#     print(f"One of my favorite books is {title}.")

# favorite_book("Holes")

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

# def describe_city(city, country="South Africa"):
#     print(f"{city} is in {country}.")

# describe_city("Johannesburg")
# describe_city("Jerusalem", "Israel")
# describe_city("Rome", "Italy")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and 
# generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, 
# display a success message, otherwise show a fail message and display both numbers.

# import random

# def review_random_num():
#     print("Pick a number between 1 and 100.")
    
#     # Get user input and validate it
#     try:
#         chosen_num = int(input("Enter your number: "))  # Ask the user for input
#     except ValueError:
#         print("Invalid! Please enter a number.")
#         return
    
#     if not (1 <= chosen_num <= 100):
#         print("NO! Please choose a number between 1 and 100.")
#         return  # Stop the function if the input is out of range
    
#     random_num = random.randint(1, 100)  # Generate a random number inside the function
    
#     if chosen_num == random_num:
#         print(f"WOW! Look at that! They are both {chosen_num}! 🎉")
#     else:
#         print(f"You lose! You chose {chosen_num}, but the random number was {random_num}. Better luck next time! 😞")

# review_random_num()

# Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size="Large", text="I love Python!"):
#     print(f"The size of the shirt is {size}, and the text of the shirt is {text}")

# make_shirt()
# make_shirt("Medium")
# make_shirt("X-Large", "Gotta get coding!")
# make_shirt(size="X-Small", text="Do you C me?")
# make_shirt(text="Python is awesome!", size="Small")

# Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     for i in range(len(magicians)):
#         magicians[i] = magicians[i] + " the Great"

# make_great(magician_names)

# show_magicians(magician_names)

# import random

# def get_random_temp(season=None):
#     if season == None:
#         return random.randint(-10, 40)
#     elif season.lower() == 'winter':
#         return random.randint(-10, 16)
#     elif season.lower() == 'spring':
#         return random.randint(0, 23)
#     elif season.lower() == 'summer':
#         return random.randint(16, 40)
#     elif season.lower() in ['autumn', 'fall']:
#         return random.randint(8, 24)
#     else:
#         return random.randint(-10, 40)
    
# def main():
#     season = input("Please enter a season (summer, autumn/fall, winter, or spring): ")
#     temperature = get_random_temp(season)
#     print(f"Right now, the temperatue is currently {temperature} degrees celcius.")

#     if temperature < 0:
#         print("Brrr, that's freezing! Wear some extra layers today.")
#     elif 0 <= temperature < 16:
#         print("Quite chilly! Don't forget your coat.")
#     elif 16 <= temperature < 23:
#         print("The weather is pretty nice. Maybe wear a light jacket.")
#     elif 23 <= temperature < 32:
#         print("Warm today. Go outside and have fun!")
#     else:  
#         print("Very hot today! Drink lots of water.")

# if __name__ == "__main__":
#     main()

# Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

# def quiz_user(data):
#     correct = 0
#     incorrect = 0
#     wrong_answers = []

#     print("Star Wars Quiz!")
#     print("Let's test your knowledge of the galaxy far, far away...\n")
    
#     for question_data in data:
#         question = question_data["question"]
#         correct_answer = question_data["answer"]

#         user_answer = input(f"{question} ")
            
#         if user_answer.lower() == correct_answer.lower():
#             print("Correct!\n")
#             correct += 1
#         else:
#             print("Incorrect!\n")
#             incorrect += 1
#             wrong_answers.append({
#                 "question": question,
#                 "user_answer": user_answer,
#                 "correct_answer": correct_answer
#                 })
    
#     return correct, incorrect, wrong_answers

# def display_results(correct, incorrect, wrong_answers):
#     total = correct + incorrect
    
#     print("\n===== QUIZ RESULTS =====")
#     print(f"You got {correct} out of {total} questions correct!")
#     print(f"Correct answers: {correct}")
#     print(f"Incorrect answers: {incorrect}")
    
#     percentage = (correct / total) * 100
    
#     if percentage == 100:
#         print("Perfect score! The Force flows through you like a true Jedi Master!")
#     elif percentage >= 80:
#         print("Impressive! Most impressive! You could be on the Jedi Council someday.")
#     elif percentage >= 60:
#         print("Not bad, young Padawan. Keep studying those Jedi texts.")
#     else:
#         print("Your Jedi training has barely begun. Study more, you must.")
    
#     if wrong_answers:
#         print("\nQUESTIONS YOU MISSED")
#         for i, wrong in enumerate(wrong_answers, 1):
#             print(f"{i}. {wrong['question']}")
#             print(f"   Your answer: {wrong['user_answer']}")
#             print(f"   Correct answer: {wrong['correct_answer']}")
        
#         if len(wrong_answers) > 3:
#             play_again = input("\nYou had more than 3 wrong answers. Want to try again? (yes/no) ")
#             if play_again.lower() == "yes":
#                 main()

# def main():
#     data = [
#         {
#             "question": "What is Baby Yoda's real name?",
#             "answer": "Grogu"
#         },
#         {
#             "question": "Where did Obi-Wan take Luke after his birth?",
#             "answer": "Tatooine"
#         },
#         {
#             "question": "What year did the first Star Wars movie come out?",
#             "answer": "1977"
#         },
#         {
#             "question": "Who built C-3PO?",
#             "answer": "Anakin Skywalker"
#         },
#         {
#             "question": "Anakin Skywalker grew up to be who?",
#             "answer": "Darth Vader"
#         },
#         {
#             "question": "What species is Chewbacca?",
#             "answer": "Wookiee"
#         }
#     ]
    
#     correct, incorrect, wrong_answers = quiz_user(data)
    
#     display_results(correct, incorrect, wrong_answers)

# if __name__ == "__main__":
#     main()
