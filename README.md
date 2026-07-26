# PFA Net Calculator

## Overview
The CLI Application takes the user's gross income and outputs the income after taxes by Romanian standards while asking if the inputted revenue is annual or monthly and whether or not the user has had expenses which are taken into account before calculating the taxes.

## Screenshots
The program succesfully calculates a freelancer's net income based on the gross income and expenses (if any) with Romanian taxes:

<img width="379" height="115" alt="Screenshot 2026-07-26 at 22 34 21" src="https://github.com/user-attachments/assets/ca64800c-7565-4b8c-b52d-b943d3e45947" />


It can catch errors such as if the user inputs a string instead of a float:

<img width="403" height="171" alt="Screenshot 2026-07-26 at 22 35 40" src="https://github.com/user-attachments/assets/17cba0a8-175a-442f-a2bb-225526fc356a" />

Or if the user's expenses are higher than the revenue:

<img width="426" height="108" alt="Screenshot 2026-07-26 at 22 34 45" src="https://github.com/user-attachments/assets/8c7c410a-06a3-45ac-9d58-36d8121dae4b" />

## Architecture & Defensive Programming
  The code contains multiple functions in order to have a straight-forward logic that can be accessible to any future coders reviewing it.
  
  The main function is used to get the necessary information to calculate the taxes while calling other functions such as get_input_float so that the information doesn't pile up in a single function.

### Functions
  `calculate_pfa_taxes` takes the reveneue as an argument before taxes and calculates them accordingly using multiple if/else statements, proceeding to then return the taxes (CAS,CASS).
  
  `get_input_float` is used to get the gross income and deductible expenses as they are both numeric values.
  
  `get_input_timeline` checks whether the inserted revenue is monthly or yearly and calculates it into the yearly revenue if needed.

### The Defense
  As with all programs, we as coders need to expect that the user will input something that breaks the logic; in this case simple string/float mistakes are taken into account using try/except ValueError, prompting the user again since everything is inside a `while True` loop that breaks when the user has succesfully inputted a correct value.
  
  Since we are talking about revenue, it has to be positive and so if the user inputs a negative number the program prints a message to let the user know that they have made a mistake and simply prompts them again.
