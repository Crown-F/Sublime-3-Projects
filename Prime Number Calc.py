#Takes user input.
num_input = int(input("Enter a number: "))

#Primary function.
def prime (num):
    if num > 1:
        #Primes have to be greater than 1.
        for i in range(2, num):
            if (num % i ) == 0:
                #If statement determines if input is not a prime.
                print(num, "is not a prime number.")
                print(i, "times" , num//i, "is", num)

                #Variables to help determine the closest prime numbers within a range of input.
                lower = num - 25
                upper = num + 25
                lst_primes = []


                for value in range(lower, upper + 1):
                    #For loop to cycle through created range to find nearest prime numbers in the event that input results in none.
                    if value > 1:
                        for i in range(2, value):
                            #For loop to create prime list.
                            if (value % i) == 0:
                                #Determines which is not a prime in the given range and discards number. Could possibly place a loop 'continue' here and remove outer else statement below.
                                break
                        else:
                            #Appends prime number to lst_primes.
                            lst_primes.append(value)
                    else:
                        #Keeps the 'for' loop in the 'if' statement cycling through the range despite numbers that are not prime.
                        continue


                if len(lst_primes) == 0:
                    #Prime gap is not static, the more an integer increases the further that gap does as well. If gap is too much, and no list is created. Message will print indicating such.
                    print("Prime gap is too large to calculate a list...")
                else:
                    #Will print out list of primes as well as the same list reversed in the event input is not a prime.
                    print("Finding prime numbers between lower and upper parameters...")
                    print("Parameters are set to less than and greater than 25 units away from input.")
                    print(lst_primes)
                    print("Returning list of primes in reverse:")
                    print(lst_primes[::-1])
                    break

        else:
            #Indicates that the given input is a prime number.
            print(num, "is a prime number!")

    else:
        #Primes must be greater than 1. Message will print if a negative integer is given for input.
        print(num, "is not valid. Must be greater than 1.")

prime(num_input)
#Calls function after given input.
