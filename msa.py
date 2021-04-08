#Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for num in range(1, 1000):
    if num % 2 != 0:
        print num

#Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for x in range(5, 100):
    if x % 5 == 0:
        print x

#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a)

# Create a program that prints the average of the values in the list: 
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)