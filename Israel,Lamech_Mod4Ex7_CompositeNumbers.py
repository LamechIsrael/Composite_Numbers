#############################################
# CS 1110A - Programming in Python          #
# Module 4 - Exercise 7 - Composit Numbers  #
# Author: Lamech Israel                     #
#                                           #
#############################################


def composite(n):
    
    
    
    # Go through all the numbers from 2 to n
    for i in range(2, n):
        
        # Divide n by the current number to get a digit
        equation = float(n) / i
        
        # Check if the result is an Integer or a Float
        if equation.is_integer() and i != 1:
            return True
    # If the loop finishes without returning True, return False
    return False
    
    
def composite_range(a, b):
    
    
    # Create an array to hold all the composite numbers
    composite_array = []
    
    for c in range(a, b+1):
        # If the number is composite, add it to the array
        if composite(c):
            composite_array.append(c)
    
    # Turn the array into a string of numbers
    finished_string = ' '.join(str(e) for e in composite_array)
    
    # Print string
    print(finished_string)
            

def main():
    a = int(input('\nlower bound: '))
    
    # Exit the code if 'a' is 0
    if a == 0:
        print('\nDone!')
        exit()
        
    # Ask for 'b' if 'a' is not 0
    else:
        b = int(input('upper bound: '))
        
        # Request a new number if the upper bound is less than the lower
        if b < a:
            print('\nPlease make sure the upper number is greater...')
        
        # Compute if everything is fine
        else:
            print('\nComposites in the range {}-{}:\n'.format(a,b))
            
            composite_range(a, b)
     


# Input

print('Composite Numbers')

while True:
    main()
    
