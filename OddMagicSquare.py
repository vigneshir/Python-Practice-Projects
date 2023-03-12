# Gives Magic Square (array of numbers which add up to same sum along any row/column/diagonal for odd number of rows/columns entered by user

# Process :
# First check whether current index lies within the array size. If not then as per rule bring it within array size
# Check whether element at current index (which we ensured lies within array size) is filled or 0. If filled, then as per rule shift to other index. Repeat step 1 (verification) for new index.
# Fill the current index (which we ensured lies within array size and is empty) with correct number as per rule.
  
n = int(input("Enter the number (odd) of rows (same as that of columns) in the magic square: "))
    
msq = [ [0 for j in range(n)] for i in range(n) ]
  
i = n//2
j = n-1
t = 1
  
# incorrect code because did not consider possibility that on shifting out-of-bound index or already filled index once, new index might again be an already filled square  
# for t in range(1,n**2+1):
#     if (i == -1 and j == n):
#         i = 0
#         j = n-2
#         msq[i][j] = t
#     elif (i == -1):
#         i = n-1
#         msq[i][j] = t
#     elif (j == n):
#         j = 0
#         msq[i][j] = t
#     elif (msq[i][j] == 0):
#         msq[i][j] = t
#     else:   
#         i = i+1
#         j = j-2
#         msq[i][j] = t
  
#     i = i-1
#     j = j+1   

for t in range(1,n**2+1):
    while( i==-1 or j==n or msq[i][j]!=0):
        if (i==-1 and j==n):
            i=0
            j=n-2
  
        elif(i==-1):
            i=n-1
  
        elif(j==n):
            j=0
  
        else:
            i=i+1 
            j=j-2
  
  
    msq[i][j] = t
    i=i-1
    j=j+1


for i in range(n):
    for j in range(n):
        print("{0:<7}".format(msq[i][j]) , end = "")
    print("")    
        
print("Sum of entries in any row, column or diagonal =", int(n*(n**2+1)/2))    
    
    