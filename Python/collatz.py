def collatz(number = 0):
    if number % 2 == 0:#Even
        return number // 2
    elif number % 2 == 1:#Odd
        return 3 * number + 1
    

def main():
    try:
        sequence = int(input('Enter a number: '))
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except ZeroDivisionError:
        print('ZeroDivisionError')

    try:
        result = collatz(sequence)
        #print('AFTER THE TRY')
        #input()
        
        while result != 1:
            result = collatz(result)
            #print('IN WHILE, Reult is:', result, sep=' ')
            #input()
            
        print(result)
    except UnboundLocalError:
        print('UnboundLocalError')

main()
