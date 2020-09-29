import sys

#      Lines 6-7 are included if you would like to read a txt file as input


path = '/Users/tanweeredwards/Desktop/NinetyOne/Test_file.txt' # change to desired path
file = open(path,'r')

# Initialise word vectors

ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
tens = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "] 
 
thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "] 
 
 
def abc123(n): 
    a = n % 10                              # units digit
    b = ((n % 100) - a) / 10                # tens digit
    c = ((n % 1000) - (b * 10) - a) / 100   # hundreds digit
    
    a = int(a)
    b = int(b)
    c = int(c)
    
    p = "" 
    q = ""
     
    if c != 0 and b == 0 and a == 0: 
        p = ones[c] + "hundred " 
    elif c != 0: 
        p = ones[c] + "hundred and " 
    if b <= 1: 
        q = ones[n%100] 
    elif b > 1: 
        q = tens[b] + ones[a] 
    abc = p + q 
    return abc 
 
def num2word(s): 
 
    if s == 0: 
        return 'zero'  
             
    num = []
    
    for t in s.split():
        try:
            num.append(float(t))
        except ValueError:
            pass
                
    if len(num) == 0:
        print("number invalid") 
        return

    num = num[0]    
    check = num % 1       # check if integer

    if check != float(0.0):
        print("number invalid")
        return

    i = 3 

    n = int(num)
    n = str(n) 
    word = "" 
    k = 0 
    
    while i == 3:
        nn = n[-i:]     # last i numbers
        n = n[:-i]      # less last i values

        if int(nn) == 0: 
            word = abc123(int(nn)) + thousands[int(nn)] + word 
        else: 
            word = abc123(int(nn)) + thousands[k] + word 
        if n == '': 
            i = i+1 
        k += 1 
    return word[:-1] 
       
k = file.read()

# Prints  to console

print(num2word(k))

# Prints to txt file

original_stdout = sys.stdout    # Save a reference to the original standard output

with open('/Users/tanweeredwards/Desktop/NinetyOne/Test_file.txt', 'a') as f: # change to desired path
 sys.stdout = f                 # Change the standard output to the file we created.
 print(num2word(k))
 sys.stdout = original_stdout






