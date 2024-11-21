# ICE02_2 if blocks (2024 Fall)
#
# =======================
# KEEP THE FOLLOWING CODE
# =======================
#
# Input data for roots of a*x**2 + b*x + c = 0
a =     1.0
b =    -1.0e9
c =     1.0

# This is the usual quadratic formula
discriminant = b**2 - 4*a*c
root1 = ( -b + discriminant**(1/2) ) / (2*a)
root2 = ( -b - discriminant**(1/2) ) / (2*a)

# The following algorithm is a floating-point safer
# version to compute quadratic roots r1 and r2
# ===================================================
# 1A) If b is positive then compute r1 as root2 above
# 1B) If b is negative then compute r1 as root1 above
#  2)    Next compute r2 as (c/a)*(1/r1)
# 1C) But if b == 0 then r1 = sqrt(c/a) and r2 = -r1
# ===================================================
#
# Use an if-block to implement the above algorithm
#  - you must have at least one "if" statement with a condition
#  - you must have at least one "elif" statement with a condition
#  - you must have at least one "else" statement
#  - compute roots named r1 and r2 as indicated above
#
# ====================================
# REPLACE THE NEXT TWO STATEMENTS WITH
# YOUR NEW CODE THAT USES AN IF BLOCK.
# ====================================



if b>0:
    r1 = root2
    r2 = (1/r1)*(c/a)
elif b<0:
    r1 = root1
    r2 = (1/r1)*(c/a)
else:
    r1 = (c/a)**1/2
    r2 = -r1





# ==========================================
# DO NOT EDIT THE STATEMENTS BELOW
# ==========================================
print("      Classic roots: ", root1, root2)
print("More accurate roots: ",    r1,    r2)
# ==========================================


