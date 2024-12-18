# The Number Guessing Game 🎮
# Introduction to Python Control Flow and Random Numbers

## Welcome Game Developer! 

In this lesson, we'll create an exciting number guessing game using Python. You'll learn how to make the computer think of a random number and give players hints to find it. Let's build this game step by step!

### What We'll Learn:
1. How to generate random numbers
2. How to use while loops for game logic
3. How to make decisions using if statements
4. How to handle user input

## Step 1: Random Numbers 🎲

First, let's learn how to make the computer choose random numbers:

```python
import random  # This lets us use random numbers

# Generate a random number between 1 and 10
secret = random.randint(1, 10)
print(f"The computer chose: {secret}")

# Let's generate a few more random numbers
print("\nGenerating 5 random numbers between 1 and 10:")
for i in range(5):
    number = random.randint(1, 10)
    print(f"Random number {i+1}: {number}")
```

### 🤔 Try It Yourself!
Generate some random numbers with different ranges. What happens if you change the numbers?

```python
# Try generating random numbers between 1 and 100
your_secret = random.randint(1, 100)
print(f"Your random number is: {your_secret}")

# Try generating numbers with different ranges
# For example, between 50 and 60
```

## Step 2: Getting Player Input 🎮

Now let's learn how to get input from the player:

```python
# Let's ask the player for a guess
print("Think of a number between 1 and 10!")
guess = input("What's your guess? ")

# Convert the input from text to a number
guess = int(guess)
print(f"You guessed: {guess}")

# Let's see if it matches a random number
secret = random.randint(1, 10)
if guess == secret:
    print("Amazing! You got it!")
else:
    print(f"Not quite! The number was {secret}")
```

### 🎯 Mini Challenge
Can you modify the code to tell the player if their guess was too high or too low?

```python
# Write your code here
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

# Add your if/elif/else statements here to give hints
```

## Step 3: Building the Game Loop 🔄

Now let's create the main game loop that lets players keep guessing:

```python
def play_simple_game():
    """
    A simple version of our number guessing game
    """
    secret = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess (1-10): "))
        attempts += 1
        
        if guess == secret:
            print(f"You found it in {attempts} tries!")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

# Let's play!
play_simple_game()
```

### 🌟 Your Turn - Customize the Game!

Now it's your turn to add features to the game. Here are some ideas:
1. Add a maximum number of attempts
2. Keep track of the high score
3. Let the player choose the number range

```python
def play_custom_game():
    # Your improved game code here
    max_attempts = 5  # For example
    secret = random.randint(1, 10)
    attempts = 0
    
    # Add your game logic here

# Try your custom game
play_custom_game()
```

## Step 4: Adding More Features 🚀

Let's make our game even better by adding score tracking:

```python
def play_advanced_game():
    """
    An advanced version of the number guessing game
    """
    score = 100  # Start with 100 points
    secret = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Advanced Number Guessing Game!")
    print("You start with 100 points. Each wrong guess costs 10 points.")
    
    while score > 0:
        guess = int(input(f"\nPoints remaining: {score}\nEnter your guess (1-100): "))
        attempts += 1
        
        if guess == secret:
            print(f"Congratulations! You won with {score} points!")
            return score
        elif guess < secret:
            print("Too low!")
            score -= 10
        else:
            print("Too high!")
            score -= 10
            
    print("Game Over! You ran out of points.")
    return 0

# Let's play the advanced game!
final_score = play_advanced_game()
```

### 🎨 Creative Challenge
Can you add these features to the game?
1. Different difficulty levels
2. Hints that cost points
3. A two-player mode

Try your ideas in the cell below:

```python
def your_awesome_game():
    # Create your enhanced version here!
    pass

# Test your awesome game
your_awesome_game()
```

## Final Challenge: Game Statistics! 📊

Keep track of multiple games and show statistics:

```python
def track_game_stats():
    games = []
    while True:
        score = play_advanced_game()
        games.append(score)
        
        print("\nGame Statistics:")
        print(f"Games played: {len(games)}")
        print(f"Best score: {max(games)}")
        print(f"Average score: {sum(games)/len(games):.1f}")
        
        play_again = input("\nPlay again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

# Run the stats tracker
track_game_stats()
```

## Congratulations! 🎉

You've completed the Number Guessing Game lesson! You can now:
- Generate random numbers
- Use loops for game logic
- Handle player input
- Track scores and statistics
- Build interactive games

Keep experimenting with your game and adding new features. The best games come from creative ideas and lots of testing!