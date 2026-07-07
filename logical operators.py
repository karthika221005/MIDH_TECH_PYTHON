marks = int(input("Enter your marks: "))

# AND Operator
if marks >= 35 and marks > 90:
    print("Pass and Excellent Performance")
else:
    print("Condition for AND is False")

# OR Operator
if marks >= 35 or marks > 90:
    print("Pass OR Scored More Than 90")
else:
    print("Failed")

# NOT Operator
if not (marks < 35):
    print("You Passed")
else:
    print("You Failed")