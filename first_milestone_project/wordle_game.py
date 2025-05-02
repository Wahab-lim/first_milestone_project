import random
import sys
from termcolor import colored
from tabulate import tabulate

def random_word():
    wordle_bank = ["About", "Alert", "Argue", "Beach", "Above", "Alike", "Arise", "Began", "Abuse", "Alive", "Array", "Begin", 
               "Actor", "Allow", "Aside", "Begun", "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below", 
               "Adopt", "Alter", "Audit", "Bench", "Adult", "Among", "Avoid", "Billy", "After", "Anger", "Award", "Birth", 
               "Again", "Angle", "Aware", "Black", "Agent", "Angry", "Badly", "Blame", "Agree", "Apart", "Baker", "Blind", 
               "Ahead", "Apple", "Bases", "Block", "Alarm", "Apply", "Basic", "Blood", "Album", "Arena", "Basis", "Board", 
               "Boost", "Buyer", "China", "Cover", "Booth", "Cable", "Chose", "Craft", "Bound", "Calif", "Civil", "Crash", 
               "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime", "Bread", "Cause", "Clean", "Cross", 
               "Break", "Chain", "Clear", "Crowd", "Breed", "Chair", "Click", "Crown", "Brief", "Chart", "Clock", "Curve", 
               "Bring", "Chase", "Close", "Cycle", "Broad", "Cheap", "Coach", "Daily", "Broke", "Check", "Coast", "Dance", 
               "Brown", "Chest", "Could", "Dated", "Build", "Chief", "Count", "Dealt", "Built", "Child", "Court", "Death", 
               "Debut", "Entry", "Forth", "Group", "Delay", "Equal", "Forty", "Grown", "Depth", "Error", "Forum", "Guard", 
               "Doing", "Event", "Found", "Guess", "Doubt", "Every", "Frame", "Guest", "Dozen", "Exact", "Frank", "Guide", 
               "Draft", "Exist", "Fraud", "Happy", "Drama", "Extra", "Fresh", "Harry", "Drawn", "Faith", "Front", "Heart", 
               "Dream", "False", "Fruit", "Heavy", "Dress", "Fault", "Fully", "Hence", "Drill", "Fibre", "Funny", "Night", 
               "Drink", "Field", "Giant", "Horse", "Drive", "Fifth", "Given", "Hotel", "Drove", "Fifty", "Glass", "House", 
               "Dying", "Fight", "Globe", "Human", "Eager", "Final", "Going", "Ideal", "Early", "First", "Grace", "Image", 
               "Earth", "Fixed", "Grade", "Index", "Eight", "Flash", "Grand", "Inner", "Elite", "Fleet", "Grant", "Input", 
               "Empty", "Floor", "Grass", "Issue", "Enemy", "Fluid", "Great", "Irony", "Enjoy", "Focus", "Green", "Juice", 
               "Enter", "Force", "Gross", "Joint", "Judge", "Metal", "Media", "Newly", "Known", "Local", "Might", "Noise", 
               "Label", "Logic", "Minor", "North", "Large", "Loose", "Minus", "Noted", "Laser", "Lower", "Mixed", "Novel", 
               "Later", "Lucky", "Model", "Nurse", "Laugh", "Lunch", "Money", "Occur", "Layer", "Lying", "Month", "Ocean", 
               "Learn", "Magic", "Moral", "Offer", "Lease", "Major", "Motor", "Often", "Least", "Maker", "Mount", "Order", 
               "Leave", "March", "Mouse", "Other", "Legal", "Music", "Mouth", "Ought", "Level", "Match", "Movie", "Paint", 
               "Light", "Mayor", "Needs", "Paper", "Limit", "Meant", "Never", "Party", "Peace", "Power", "Radio", "Round", 
               "Panel", "Press", "Raise", "Route", "Phase", "Price", "Range", "Royal", "Phone", "Pride", "Rapid", "Rural", 
               "Photo", "Prime", "Ratio", "Scale", "Piece", "Print", "Reach", "Scene", "Pilot", "Prior", "Ready", "Scope",
               "Pitch", "Prize", "Refer", "Score", "Place", "Proof", "Right", "Sense", "Plain", "Proud", "Rival", "Serve", 
               "Plane", "Prove", "River", "Seven", "Plant", "Queen", "Quick", "Shall", "Plate", "Sixth", "Stand", "Shape", 
               "Point", "Quiet", "Roman", "Share", "Pound", "Quite", "Rough", "Sharp", "Sheet", "Spare", "Style", "Times", 
               "Shelf", "Speak", "Sugar", "Tired", "Shell", "Speed", "Suite", "Title", "Shift", "Spend", "Super", "Today", 
               "Shirt", "Spent", "Sweet", "Topic", "Shock", "Split", "Table", "Total", "Shoot", "Spoke", "Taken", "Touch", 
               "Short", "Sport", "Taste", "Tough", "Shown", "Staff", "Taxes", "Tower", "Sight", "Stage", "Teach", "Track", 
               "Since", "Stake", "Teeth", "Trade", "Sixty", "Start", "Texas", "Treat", "Sized", "State", "Thank", "Trend", 
               "Skill", "Steam", "Theft", "Trial", "Sleep", "Steel", "Their", "Tried", "Slide", "Stick", "Theme", "Tries", 
               "Small", "Still", "There", "Truck", "Smart", "Stock", "These", "Truly", "Smile", "Stone", "Thick", "Trust", 
               "Smith", "Stood", "Thing", "Truth", "Smoke", "Store", "Think", "Twice", "Solid", "Storm", "Third", "Under", 
               "Solve", "Story", "Those", "Undue", "Sorry", "Strip", "Three", "Union", "Sound", "Stuck", "Threw", "Unity", 
               "South", "Study", "Throw", "Until", "Space", "Stuff", "Tight", "Upper", "Upset", "Whole", "Waste", "Wound", 
               "Urban", "Whose", "Watch", "Write", "Usage", "Woman", "Water", "Wrong", "Usual", "Train", "Wheel", "Wrote", 
               "Valid", "World", "Where", "Yield", "Value", "Worry", "Which", "Young", "Video", "Worse", "While", "Youth",
               "Virus", "Worst", "White", "Worth", "Visit", "Would", "Vital", "Voice"]
    wordle_bank = [item.lower() for item in wordle_bank]
    return random.choice(wordle_bank)


    


def display_board(guess, secret_word):
    # global colored_wordle
    # wordle = [
    # [guess[0]],
    # [guess[1]],
    # [guess[2]],
    # [guess[3]],
    # [guess[4]]
    # ]
    colored_wordle = []
    secret_word_list = list(secret_word)
    guess_list = list(guess)

    
    for i in range(len(guess_list)):
        if guess_list[i] == secret_word_list[i]:
            colored_wordle.append(colored(guess_list[i], 'green')) 
            secret_word_list[i] = None 
        else:
            colored_wordle.append(guess_list[i])  
    for i in range(len(guess_list)):
        if colored_wordle[i] != colored(guess_list[i], 'green'):
            if guess_list[i] in secret_word_list:
                colored_wordle[i] = colored(guess_list[i], 'yellow')  # Correct letter, wrong position
                secret_word_list[secret_word_list.index(guess_list[i])] = None        
    return colored_wordle
# wordle = display_board(guess)
def play_wordle():
    global secret_word
    global guess
    # secret_word = random.choice(wordle_bank)
    attempts = 6
    guesses = []
    
    secret_word = random_word()

    print(colored("Let's play Wordle!", "blue"))
    print(colored("Guess by typing a 5 letter word!\n", "cyan"))

    while attempts > 0:
        guess = input("Enter your 5-letter guess: ").lower()
        # guesses.append(guess)
        
        
        wordle = display_board(guess, secret_word)
        guesses.append(wordle)

        print(tabulate(guesses, tablefmt="fancy_grid"))
        
        if guess == secret_word:
            print(colored(f"Congratulations! You've guessed the secret word: {secret_word}", "green"))
            break
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The secret word was: {secret_word}")
    
play_wordle()

# play_again = ""
# while play_again != "q":
#     play_wordle()
# play_again = input("Want to play again? Type q to exit the game >")
