name=str(input("Enter Your Name:"))
marks=[]
n=int(input("Number of subject:"))
for i in range(1,n+1):
    score=float(input(f"Subject {i} marks:"))
    marks.append(score)
total=sum(marks)
print("Total marks:",total)
print("Average marks:",total/n)
high=max(marks)
low=min(marks)
percentage=(total/(n*100))*100
print("Percentage of student:",percentage)
print("Highest Score:",high)
print("Lowest score:",low)
if low<35:
    print("The student is Fail in one or two subjects.")
elif percentage >=90:
    print("Student passed with A Grade.")
elif percentage>70:
    print("Student passed with B Grade.")
elif percentage>50:
    print("Student passed with C Grade.")
elif percentage>45:
    print("Student paseed with D Grade.")
else:
    print("Student is Fail.")

