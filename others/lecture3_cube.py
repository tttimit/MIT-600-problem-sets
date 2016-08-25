##Find the cube root of a perfect cube(while-loop version)
##x = int(input("Enter an integer: "))
##ans = 0
##while ans * ans * ans < abs(x):
##    ans = ans + 1
##if ans * ans * ans != abs(x):
##    print(x , 'is not a perfect cube')
##else:
##    if x < 0:
##        ans = -ans
##    print(x , 'is the perfect cube of', ans)

# Find the cube root of a perfect cube(for-loop version)
x = int(input("Enter an integer: "))
for ans in range(0, abs(x) + 1):
    if ans ** 3 == abs(x):
        break
if ans ** 3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans))
