'''
Keshav Shah

Question 7: Reverse Words
Given a string, return the string with the order of the space-separated words reversed

Stack

Time Complexity: O(n) (Go through all the letters in the input string)
Space Complexity: O(n) (Add all the letters to the stack)

Process:
    - Utilize the python split function to split all the words into separate strings
    - Add all the words to a stack
    - Retrieve the words from the stack and append it to a string for output

Time Spent: 30 minutes
'''

def reverse_words(str):

    stack = []
    output = []
    # split string
    string = str.split(' ')
    for s in string:
        stack.append(s)
    while stack:
        # add the string to the output list while the stack is not empty
        output.append(stack.pop())
    # returns a string that is concatenated from the elements of the output list
    return " ".join(output)

def main():
    print(reverse_words("Uber Career Prep")) # Correctly outputs Prep Career Uber

    print(reverse_words("Emma lives in Brooklyn, New York.")) # Correctly outputs York. New Brooklyn, in lives Emma

    print(reverse_words("Hi, Doe John am I")) # Correctly outputs I am John Doe Hi,

    print(reverse_words("hi .")) # Correctly outputs . hi

    print(reverse_words("bye")) # Correctly outputs bye
main()
