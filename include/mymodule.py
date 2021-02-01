'''
A python module to exhibit the use of the __main__ name.
'''

def foo():
    ''' A test function. '''
    return 1

# Main Function
def main():
    # put all your main program driver code here
    print(foo())
    
# main is called once when the script is executed.    
if __name__ == '__main__':
    main()
