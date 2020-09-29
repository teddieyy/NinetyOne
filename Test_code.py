#The following are  test inputs to ensure that code runs correctly. 

#expected output
#print("five hundred and thirty-six")
#actual output
print(num2word("The pump is 536 deep underground."))

#expected output
#print("nine thousand, one hundred and twenty-one")
#actual output
print(num2word("We processed 9121 records."))

#expected output
#print("number invalid")
#actual output
print(num2word("Variables reported as having a missing type #65678."))

#expected output
#print("ten thousand and twenty-two")
#actual output
print(num2word("Interactive and printable 10022 ZIP code."))

#expected output
#print("sixty-six billion, seven hundred and twenty-three million, one hundred and seven thousand and eight")
#actual output
print(num2word("The database has 66723107008 records."))

#expected output
#print("number invalid")
#actual output
print(num2word("I received 23456.9 KGs."))

#0
print(num2word(0))
 