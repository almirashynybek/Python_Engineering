height = int(input('Enter please the height of triangle: '))

for i in range (height, 0, -1):
    print(" " * (height-i), end='')
    print('*' * (2 * i - 1))

# *******
#  *****
#   ***
#    *  
    
for i in range (height, 0, -1):
    print(" " * (height-i), end='')
    print('*' * i )

# ****
#  ***
#   **
#    * 
    
for i in range (height, 0, -1):
    print('*' * i )

# ****
# ***
# **
# *

for i in range (1, height + 1):
    print('*' * i )

# *
# **
# ***
# ****