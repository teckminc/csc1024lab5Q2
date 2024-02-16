'''
Do not remove any text from these comments
2.	Write a Python program using the while loop to get an input of 
five numbers from the user, then store the input into a list 
called my_list in incremental order. Lastly, calculate the 
total and average values for the numbers stored in my_list.
Following is the sample output of the program.

Enter a number: 1.1
Enter a number: 2.2
Enter a number: 3.3
Enter a number: 4.4
Enter a number: 5.5
my_list = [1.1, 2.2, 3.3, 4.4, 5.5]
Total = 16.5
Average = 3.3

Function to use: float(), input(), print(), list.append(), list.sort()
Operators: <=, +
Structure: while
'''
def main():
    my_list = []
    count = 1
    while count <= 5:
        num = float(input("Enter a number: "))
        my_list.append(num)
        count = count + 1

    my_list.sort()
    print("my_list =" , my_list)
    
    return 0

