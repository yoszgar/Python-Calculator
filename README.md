Python Calculator

A simple, interactive command-line calculator written in Python. Pick an operation from a menu, enter two numbers, and get the result printed in the terminal.

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

How It Works

Function	Description

1. add(a, b)	Returns the sum of two numbers

2. subtract(a, b)	Returns the difference of two numbers

3. multiply(a, b)	Returns the product of two numbers

4. divide(a, b)	Returns the quotient; raises an error if b is zero

5. get_number(prompt)	Keeps asking until the user enters a valid number

6. main()	Runs the menu loop and ties everything together


Author

Created by yoszgar.
