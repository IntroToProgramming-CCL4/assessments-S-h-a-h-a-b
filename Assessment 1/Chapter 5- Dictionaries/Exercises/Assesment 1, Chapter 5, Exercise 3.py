# Create a glossary of programming terms and their meanings
glossary = {
    "Variable": "A named container for storing data in a program.",
    "Comment": "A line of text in a program that is not executed and is used to provide explanations or notes.",
    "Loop": "A control structure that repeatedly executes a set of statements while a condition is true.",
    "Conditional statement": "A control structure that allows a program to make decisions based on specified conditions.",
    "List": "An ordered collection of items that can contain elements of different types." }
    
# Print each word and its meaning using loop
for key, value in glossary.items():
    print(key+":","\n"+value+"\n")

# Add five more Python terms to your glossary.    
glossary['String'] = 'A string is a sequence of characters enclosed in single or double quotes. Its used to represent text in Python.'
glossary['Function'] = 'A function is a reusable block of code that performs a specific task.You can define your functions or use built-in functions in Python.'
glossary['Input'] = 'In Python, you can use the input function to receive user input from the keyboard.'
glossary['Print'] = 'The print statement is used to display output to the console.'
glossary['Operator'] = 'Operators in Python are special symbols or keywords that are used to perform operations on variables and values.'

# Print all words and their meanings 
print("\n\n")
for key, value in glossary.items():
    print(key+":","\n"+value+"\n")


