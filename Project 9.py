#Gabrielle.Gervasi1@marist.edu
#Gabi Gervasi
#write a prgram to find prime numbers 


def main ():

    
    print ("This program uses the Sieve of Eratosthenes algorithm to find all the prime numbers up to n.\n")

   
    n = eval(input("Please enter a number. "))

    
    listOfNumbers = []
    primes = []
    for i in range(2, n + 1):
        listOfNumbers.append(i)

    
    while listOfNumbers != []:
        number = listOfNumbers[0]
        
        primes.append(number)
        listOfNumbers.remove(number)
        
        i = 0
        while i < len(listOfNumbers):
            num2 = listOfNumbers[i]
            if num2 % number == 0 and num2 != number:
                
                listOfNumbers.remove(num2)
                i -= 1
            i += 1

    print (primes)

main ()
