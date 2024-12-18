# Secret Message Decoder 🕵️
# Introduction to Python String Manipulation

## Welcome, Future Code Breaker! 

In this lesson, we'll learn how to create a secret message decoder using Python. By the end of this notebook, you'll be able to decode secret messages and even create your own! Let's start our journey step by step.

### What We'll Learn:
1. How strings work in Python
2. How to access individual characters in a string
3. How to build a new string character by character
4. How to use loops to process strings

## Step 1: Understanding Strings 📝

First, let's explore how strings work in Python. Run the cell below to see how we can work with text:

```python
# Let's create a simple message
message = "HELLO"

# Print each character and its position
print("Let's look at each character in 'HELLO':")
for position, letter in enumerate(message):
    print(f"Position {position}: {letter}")
```

### 🤔 Try It Yourself!
Change the message to your name and run the cell. What do you notice about the positions of the letters?

```python
# Your turn! Replace "YOUR NAME" with your actual name
message = "YOUR NAME"

# Print each character and its position
for position, letter in enumerate(message):
    print(f"Position {position}: {letter}")
```

## Step 2: Reading Text Backwards 🔄

To decode our secret messages, we need to read text backwards. Let's learn how!

```python
message = "HELLO"

# Method 1: Using a reverse loop
print("Reading backwards using a loop:")
for i in range(len(message)-1, -1, -1):
    print(message[i], end='')
print()  # This adds a new line

# Method 2: Using string slicing
print("Reading backwards using slicing:")
print(message[::-1])
```

### 🎯 Mini Challenge
Can you figure out what these secret messages say?
1. "GNIDOC"
2. "NUF"

Try decoding them using the code below:

```python
# Write your decoding code here
secret_message = "GNIDOC"
decoded_message = secret_message[::-1]
print(f"The secret message '{secret_message}' decodes to: {decoded_message}")

# Try the second message too!
```

## Step 3: Building Our Decoder Function 🛠️

Now let's create a function that can decode any secret message:

```python
def decode_message(secret):
    """
    This function takes a secret message and returns the decoded version
    """
    decoded = ""  # Start with an empty string
    
    # Add each letter from the end to the beginning
    for letter in secret[::-1]:
        decoded += letter
    
    return decoded

# Let's test our function
test_message = "TERCES POT"
decoded = decode_message(test_message)
print(f"Secret message: {test_message}")
print(f"Decoded message: {decoded}")
```

### 🌟 Your Turn - Creating Secret Messages!

Now it's your turn to create and decode secret messages. Use the cells below:

```python
# 1. Create your own secret message by reversing a normal message
normal_message = "YOUR MESSAGE HERE"
secret_message = normal_message[::-1]
print(f"Your secret message is: {secret_message}")

# 2. Try decoding it!
decoded = decode_message(secret_message)
print(f"Decoded message: {decoded}")
```

## Final Challenge: Message Exchange! 🎮

Work with a partner and try these activities:

1. Create a secret message for your partner
2. Exchange messages
3. Try to decode each other's messages
4. Verify if you decoded them correctly!

```python
# Create your secret message here
my_message = "WRITE YOUR MESSAGE"
secret_for_friend = my_message[::-1]
print(f"Give this secret message to your friend: {secret_for_friend}")

# Decode your friend's message here
friends_secret = "PASTE YOUR FRIEND'S MESSAGE"
decoded_friend_message = decode_message(friends_secret)
print(f"Your friend's message says: {decoded_friend_message}")
```

## Bonus: Advanced Decoder! 🚀

For an extra challenge, try creating a decoder that can handle spaces and punctuation:

```python
def advanced_decode(secret):
    """
    An advanced decoder that handles spaces and punctuation
    """
    decoded = ""
    for letter in secret[::-1]:
        decoded += letter
    return decoded

# Test with a more complex message
complex_message = "!GNIDOC EVOL I"
decoded_complex = advanced_decode(complex_message)
print(f"Complex secret: {complex_message}")
print(f"Decoded message: {decoded_complex}")
```

### 🎨 Creative Challenge
Can you modify the decoder to:
1. Handle lowercase and uppercase letters?
2. Ignore spaces when decoding?
3. Add your own special decoding rules?

Try your ideas in the cell below:

```python
# Your creative decoder here!
def creative_decode(secret):
    # Add your code here
    pass

# Test your creative decoder
test_message = "Your test message here"
result = creative_decode(test_message)
print(f"Result: {result}")
```

## Congratulations! 🎉

You've completed the Secret Message Decoder lesson! You can now:
- Understand how strings work in Python
- Read text backwards using different methods
- Create and decode secret messages
- Build your own decoder functions

Remember: The best way to learn coding is by experimenting and trying new things. Don't be afraid to modify the code and see what happens!