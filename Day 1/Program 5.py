r1=int(input("Enter the run scored in 60 balls by Player 1"))
r2=int(input("Enter the run scored in 60 balls by Player 2"))
r3=int(input("Enter the run scored in 60 balls by Player 3"))
s1=r1*100/60
s2=r2*100/60
s3=r3*100/60
print("Strike rate of Player 1 is",s1)
print("Strike rate of Player 2 is",s2)
print("Strike rate of Player 3 is",s3)
print("The final score if Player 1 played 60 more balls ",r1*2)
print("The final score if Player 2 played 60 more balls ",r2*2)
print("The final score if Player 3 played 60 more balls ",r3*2)
print("Maximum number of sixes player 1 could hit ", int(r1 / 6))
print("Maximum number of sixes player 2 could hit ", int(r2 / 6))
print("Maximum number of sixes player 3 could hit ", int(r3 // 6))