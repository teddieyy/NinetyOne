# NinetyOne Coding Challenge

##  Explanation

The code begins by defining 3 vectors containing the words for the tens, hundreds and thousands digits respectively. 

The sub function abc123 is then defined. This function takes the given number (in digits) as the input. Three variable (a, b, c) are then assigned to the units, tens and hundreds digits. An algorithm then differentiates the maginitude of the respective digits (using the modulus function to determine remainders) and assigned the appropriate word to it (from the defined word vectors). 

The function num2word takes the inputted string, s, and identifies all the numerical characters within the string. This is done by seperating the string into a list of individual "words". Each  "word" is then run through a for loop in order to determine whether it is an integer. This step also rejects any floats or numbers with foreign characters ie hashtags and returns an empty list instead with the appropriate error messages. A special case is implemented for an input of "0". Finally, this function then uses the sub function abc123 to puzzle together the entire number in words. This is done in an iterative loop and runs until each number has been accounted for, with each iteration adding an additional word.  

## Assumptions

It is assumed that the inputed string will contain numeric digits to be converted to words. It is also assumed that  any floats will be inputted using a period  as a delimeter, not a comma. 

## Limitations
No commas are printed, in addition there are cases where the "and" is not included, ie when there is no tens unit. 

For example:
print(num2word("The database has 66723107008 records.")) prints:
"sixty six billion seven hundred and twenty three million one hundred and seven thousand eight" where an 'and' is missing before the 'eight'. 

When there is an invalid input, the programme outputs "invalid input" and "None"  as opposed to just "invalid input" to the txt file. 

## Evolve possibilities 

Being able to convert floats to words. This would not require much more work, but an additonal for loop for the integers that follow the decimal point. The words for these decimals can be sourced from the "ones" vector. 

## Instructions 

### If running from and to a txt file:
1. Change the file  path to the desired path  (line 6). 
2. Change the file  path to the desired path  (line 95). 
3. This will read the txt file and add the number in words to that same txt file. It will also print the words to the console. 

### If running from and to the console:
1. Comment out lines 6-7.
2. Comment out lines 85-98.
3. Initialise the function by running it. 
4. In the console, input num2word("k"), where k is the string containing a number which you would like to convert to a  word. 
