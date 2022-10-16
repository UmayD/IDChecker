# IDChecker

**IDChecker** is a project to check whether a Turkish National ID number is valid or not. The project has written in **Python** and **Flask**.

Here are rules for a valid ID:
- ID must all be numbers, no letters or other superfluous characters
- ID must be 11 digits
- The first number of the ID cannot be 0
- The sum of: 1st, 3rd, 5th, 7th and 9th digits multiplied by seven, 
decremented by the sum of: 2nd, 4th, 6th and 8th digits, divided by 10, have the remainder equal to the 10th digit
- The remainder from the sum of the first 10 digits, divided by 10, gives the 11th digit.
