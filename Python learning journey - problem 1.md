# Python Programming Journey - Year 8
## A Step-by-Step Guide to Building Python Programs

### How to use this notebook:
1. Open this in Google Colab
2. Each section contains:
   - Learning objectives
   - Example code to study
   - Tasks to complete
   - Challenge extensions
3. Run each cell with the ▶️ button or press Shift+Enter
4. Write your code in the provided code cells
5. Save your work regularly

## 🎮 Problem 1: Number Guessing Game
### Learning Objectives:
- Understanding basic Python syntax
- Working with variables and user input
- Using while loops and if statements
- Implementing basic game logic

### 1.1 Study the Example
```python
# Example of a simple number checker
import random

# Generate a random number between 1 and 10
secret = random.randint(1, 10)

# Get one guess from the user
guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("You got it!")
else:
    print(f"Sorry, it was {secret}")

# Run this cell to try the simple version
```

### 1.2 Your First Task
```python
# Task: Complete the number guessing game
# Requirements:
# 1. Number should be between 1 and 100
# 2. Player gets 7 attempts
# 3. Tell player if guess is too high or too low
# 4. Keep track of attempts used

import random

def number_guessing_game():
    # Your code here
    pass  # Delete this line when you start coding

# Test your game
number_guessing_game()
```

### 1.3 Challenge Extension
```python
# Challenge: Improve the game
# Add these features:
# 1. Ask if player wants to play again
# 2. Keep track of high score (least attempts)
# 3. Add difficulty levels (easy: 1-50, hard: 1-200)

# Your improved version here
```

## 🌡️ Problem 2: Temperature Converter
### Learning Objectives:
- Creating functions
- Input validation
- Mathematical operations
- Error handling

### 2.1 Study the Example
```python
# Example of a simple Celsius to Fahrenheit converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

# Test the function
temp = float(input("Enter temperature in Celsius: "))
result = celsius_to_fahrenheit(temp)
print(f"{temp}°C = {result}°F")
```

### 2.2 Your Task
```python
# Task: Create a complete temperature converter
# Requirements:
# 1. Convert between C, F, and K
# 2. Handle invalid inputs
# 3. Round results to 2 decimal places
# 4. Include input validation

def convert_temperature(value, from_unit, to_unit):
    # Your code here
    pass

# Example test cases:
test_cases = [
    (0, 'C', 'F'),    # Should be 32.0
    (98.6, 'F', 'C'), # Should be 37.0
    (300, 'K', 'C'),  # Should be 26.85
]

# Test your function
for value, from_unit, to_unit in test_cases:
    result = convert_temperature(value, from_unit, to_unit)
    print(f"{value}°{from_unit} = {result}°{to_unit}")
```

### 2.3 Challenge Extension
```python
# Challenge: Create a temperature converter interface
# Add these features:
# 1. Menu for selecting conversion type
# 2. Continuous conversion until user quits
# 3. History of conversions

# Your improved version here
```

## 📊 Problem 3: Word Statistics
### Learning Objectives:
- String manipulation
- Using dictionaries
- Working with loops
- Basic statistics

### 3.1 Study the Example
```python
# Example of basic text analysis
text = "Hello World"
print(f"Length: {len(text)}")
print(f"Words: {len(text.split())}")
print(f"Uppercase: {text.upper()}")
```

### 3.2 Your Task
```python
# Task: Create a text analysis function
# Requirements:
# 1. Count total words
# 2. Calculate average word length
# 3. Find most common letter
# 4. Count vowels and consonants

def analyze_text(text):
    # Your code here
    pass

# Test your function
sample_text = "The quick brown fox jumps over the lazy dog!"
results = analyze_text(sample_text)
# Add code to print results
```

### 3.3 Challenge Extension
```python
# Challenge: Enhance the text analyzer
# Add these features:
# 1. Identify palindromes
# 2. Count punctuation marks
# 3. Find longest and shortest words

# Your improved version here
```

## 🛒 Problem 4: Shopping List Manager
### Learning Objectives:
- Object-Oriented Programming (OOP)
- File handling
- Data persistence
- User interface design

### 4.1 Study the Example
```python
# Example of a basic shopping list
shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"Added: {item}")

def show_list():
    for item in shopping_list:
        print(f"- {item}")

# Test the basic functions
add_item("Apples")
add_item("Bread")
show_list()
```

### 4.2 Your Task
```python
# Task: Create a Shopping List class
# Requirements:
# 1. Add items with quantities
# 2. Remove items
# 3. Update quantities
# 4. Save to file
# 5. Load from file

class ShoppingList:
    def __init__(self):
        # Your code here
        pass

# Test your shopping list
my_list = ShoppingList()
# Add your test code here
```

### 4.3 Challenge Extension
```python
# Challenge: Enhance the shopping list
# Add these features:
# 1. Categories for items
# 2. Price tracking
# 3. Budget management
# 4. Shopping history

# Your improved version here
```

## 📝 Problem 5: Quiz Game
### Learning Objectives:
- Combining all previous concepts
- Random selection
- Score tracking
- Program organization

### 5.1 Study the Example
```python
# Example of a simple quiz question
questions = {
    "What is the capital of France?": "Paris"
}

def ask_question(question, correct_answer):
    answer = input(question + " ")
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        return 1
    else:
        print(f"Sorry, the answer was {correct_answer}")
        return 0

# Test the function
score = ask_question("What is the capital of France?", "Paris")
print(f"Score: {score}")
```

### 5.2 Your Task
```python
# Task: Create a complete quiz game
# Requirements:
# 1. Multiple questions in dictionary
# 2. Random question selection
# 3. Score tracking
# 4. Percentage calculation
# 5. Final results display

def create_quiz():
    # Your code here
    pass

# Run your quiz
create_quiz()
```

### 5.3 Challenge Extension
```python
# Challenge: Enhance the quiz game
# Add these features:
# 1. Multiple choice questions
# 2. Different difficulty levels
# 3. Time limits for questions
# 4. High score system
# 5. Category selection

# Your improved version here
```

## 📚 Additional Resources
- Python Documentation: https://docs.python.org/3/
- Google Colab Tutorial: https://colab.research.google.com/
- Python Beginner's Guide: https://wiki.python.org/moin/BeginnersGuide

## 🎯 Final Project Ideas
1. Combine multiple concepts to create:
   - A shop management system
   - A student grade tracker
   - A simple text-based game
   - A personal diary system

## ✅ Assessment Checklist
For each program, make sure you have:
- [  ] Written clear comments
- [  ] Handled invalid inputs
- [  ] Tested with different cases
- [  ] Added error messages
- [  ] Used meaningful variable names
- [  ] Formatted code consistently
