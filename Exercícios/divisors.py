##Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec, String> in Rust).

##Example:

##divisors(12); #should return [2,3,4,6]
##divisors(25); #should return [5]
##divisors(13); #should return "13 is prime"

def divisors(integer):
    cont = 1
    lista = []
    while cont < (integer-1):
        cont += 1 
        if integer % cont == 0:
            lista.append(cont)
    if len(lista) == 0:       
        #elif integer % cont != 0:
        return print(f'{integer} is prime')
            
    return print(lista)

divisors(13)
divisors(15)