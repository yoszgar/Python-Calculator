Python Calculator

A simple, interactive command-line calculator written in Python. Pick an operation from a menu, enter two numbers, and get the result printed in the terminal.

Features
Addition, subtraction, multiplication, and division
Interactive menu: choose the operation first, then enter your numbers
Input validation: asks again if you type something that isn't a number
Division by zero is handled with a clear error message instead of a crash
Runs in a loop so you can do as many calculations as you like
Requirements
Python 3.6 or newer
No external libraries needed
Getting Started
Clone the repository:
   git clone https://github.com/yoszgar/Python-Calculator.git
Move into the project folder:
   cd Python-Calculator
Run the calculator:
   python calculator.py
Usage

When you start the program, a menu appears:

Choose an operation:
  1. Addition
  2. Subtraction
  3. Multiplication
  4. Division
  q. Quit
Your choice:

Type the number of the operation you want, then enter the two numbers when prompted. The result is printed, and the menu appears again. Type q to quit.

Example
Your choice: 4
Enter the first number: 27
Enter the second number: 4
Division result: 6.75
Project Structure
Python-Calculator/
├── calculator.py   # The calculator program
└── README.md       # Project description
How It Works
Function	Description
add(a, b)	Returns the sum of two numbers
subtract(a, b)	Returns the difference of two numbers
multiply(a, b)	Returns the product of two numbers
divide(a, b)	Returns the quotient; raises an error if b is zero
get_number(prompt)	Keeps asking until the user enters a valid number
main()	Runs the menu loop and ties everything together
Author

Created by yoszgar.
