# Star_Pattern
rows = int(input("Enter number of rows : "))
k = rows - 2
#for downward pyramid
for i in range(rows, -1, -1):
    #for giving spces we use inner loops
    for j in range(k ,0 ,-1):
        print(end=" ")
    #for increase value of k after each iteration    
    k = k + 1
    #this inner loop will print stars
    for j in range(0, i+1):
        print("* ", end="")
    print("")    


#for upward pyramid
k = 2 * rows - 2
for i in range(0,rows):
    #for giving spaces we use inner loops again
    for j in range(0,k):
        print(end=" ")
    #for decrement the value of k after each iteration
    k = k - 1
    #this inner loop will print stars
    for j in range(0, i+1):
        print("* ",end="")
    print("")     

