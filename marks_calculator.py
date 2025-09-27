#Aggregate marks & Average.


print("Enter obtained marks of each subject:\n")

#Input value
hin=float(input("Hindi:"))
eng=float(input("English:"))
math=float(input("Maths:"))
sci=float(input("Science:"))
sst=float(input("Social Science:"))

#Formula of Aggregate Marks
agm=hin+eng+math+sci+sst

#Formula of Average
avg=agm/5

print("Aggregate Marks:",agm,"/500","\nAverage Marks:",avg)
