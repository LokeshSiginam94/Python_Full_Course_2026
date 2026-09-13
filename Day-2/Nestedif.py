age=int(input("Enter your age:"))
had_covid=input("Have you had covid? (yes/no):")
if age>=18:
    if had_covid.lower()=="yes":
        print("You are eligible for vaccination")
    else:
        print("You are not eligible for vaccination")

Age=int(input("Enter your age:"))
has_id=True
if Age>=18:
    if has_id:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
