# 1.

# m,s,e=int(input('enter mark of math:')),int(input('enter mark of science:')),int(input('enter mark of english:'))

# if 0<=m<=100 and 0<=s<=100 and 0<=e<=100:
#     if m>=35 and s>=35 and e>=35:
#         print('you have passed all subject')
#     else:
#         print('you are fail')

# else:
#     print('you mark is not between 0 and 100')


# q2

# age,income=int(input('enter age:')),float(input('enter income:'))

# if 1<=age<=120 and 0<=income<=100000:
#    if age>=60 and income>=25000:
#         print('you are eligible ')

# else:
#     print('you are not eligible')

# q3.

# amount = float(input("enter  amount : "))
# membership = input("are you a registered member? (yes/no): ")


# if 0 < amount <= 100000 and membership in ["yes", "no"]:

#     if amount > 2000 and membership == "yes":
#         print("You get a 15% discount.")
#     else:
#         print("You are not eligible for the discount.")
# else:
#     print("Invalid input. Please enter valid amount and membership status.")


# q4


# member = input("Enter membership type (premium/regular): ")
# cart_value = int(input("Enter cart value : "))
# num_items = int(input("Enter number of items: "))


# if member in ["premium", "regular"] and 0 <= cart_value <= 100000 and 0 <= num_items <= 100:

#     if member == "premium" or (cart_value > 5000 and num_items > 3):
#         print("Discount applied")
#     else:
#         print("No discount")
# else:
#     print("Invalid input. Please check the values entered.")


# q5

# amount = int(input("enter the amount:"))
# bal = int(input("enter a bal:"))

# if 0 <= amount <= 100000 and 0 <= bal <= 100000:
#     if amount % 100 == 0 and amount<=bal-50:
#         print("withdrawal successfully")

#     else:
#         print("transaction declined")

# else:
#     print("invalid amount and bal")


# q6  College Admission Eligibility

# m,p,c=int(input('enter mark of math:')),int(input('enter mark of physics:')),int(input('enter mark of computer science:'))

# if 0<=m<=100 and 0<=p<=100 and 0<=c<=100:
#     if m>=80 and (p>=70 or c>=70):
#         print('you are eligible for cs')

#     else:
#         print('you are not eligible for cs')

# else:
#     print('invalid range of subjects')


# q7 Gym Membership Plan

# age,fitness=int(input('enter the age:')),int(input('enter the fitness:'))

# if 10<=age<=100 and 1<=fitness<=10:
#     if 18<=age<=40 and fitness>=8:
#         print('membership granted')

#     else:
#         print('you are not eligible')

# else:
#     print('invlid range of age or fitness')

# q8 flight Check-in Baggage Rules

# cabin = int(input("enter cabin:"))
# checkin = int(input("enter the checkin:"))

# if 0 <= cabin <= 50 and 0 <= checkin <= 50:
#     if cabin <= 7 and checkin <= 20:
#         print("allowed to board")
#     else:
#         print("baggage limit exceeded")

# else:
#     print("invalid range of data")


# q9  Tax Bracket Calculator

# income=int(input('enter the income:'))

# if 0<=income<=5000000:
#     if income<=250000:
#         print('tax rate :0%')

#     elif 250000<income<= 500000:
#         print('tax rate:5%')

#     elif 500000<income<=1000000:
#         print('tax rate:20%')

#     elif income>1000000:
#         print('tax rate:30%')

# else:
#     print('invalid range of data')


# q10.University Grading Policy
# mark=int(input('enter the mark:'))

# if 0<=mark<=100:
#     if mark>=90:
#         print('grade A')

#     elif 80<=mark<90:
#         print('grade B')
#     elif 70<=mark<80:
#         print('grade C')
#     elif 60<=mark<70:
#         print('grade D')
#     else:
#         print('fail')

# else:
#     print('invalid range')


# q11  Hotel Room Booking Rate

# season = input("enter the season name:")
# if season == "peak":
#     print("Room rate: ₹5000")
# elif season == "mid":
#     print("Room rate: ₹3000")
# elif season == "off":
#     print("Room rate: ₹1500")
# else:
#     print("Invalid season")


#q12.Job Applicant Shortlisting

# experience = int(input("Enter years of experience: "))


# if 0 <= experience <= 50:
  
#     if experience >= 10:
#         print("Role: Senior")
#     elif 5 <= experience <= 9:
#         print("Role: Mid-Level")
#     elif 2 <= experience <= 4:
#         print("Role: Junior")
#     else:
#         print("Role: Internship")
# else:
#     print("Invalid input. Experience must be between 0 and 50.")


#q13  . Restaurant Tip Suggestion

# Input
# service = input("Enter service quality (excellent/good/average/poor): ").strip().lower()
# bill_amount = int(input("Enter bill amount (in ₹): "))


# if service == "excellent":
#     tip_percent = 0.20
# elif service == "good":
#     tip_percent = 0.15
# elif service == "average":
#     tip_percent = 0.10
# elif service == "poor":
#     tip_percent = 0.05
# else:
#     tip_percent = 0.0


# tip_amount = int(bill_amount * tip_percent)


# print(f"Suggested tip: ₹{tip_amount}")


#nested if:
#q14.  Smart Parking Fee System

# vehile=input('enter vehicle name:')
# dur=int(input('enter duration:'))

# if vehile=='car':
#     if dur<=2:
#         print('charge is 50')
#     elif dur<=5:
#         print('charge is 100')
#     else:
#         print('charge is 200')    
        
# elif vehile=='bike':
#     if dur<=2:
#      print('charge is 50')
#     elif dur<=5:
#         print('charge is 100')
#     else:
#         print('charge is 200')

# else:
#     print('vehicle is not allowed')         
            
            
#q15.  E-Commerce Discount Eligibility

# Input
# membership = input("Enter membership type (prime/non-prime): ")
# cart_value = int(input("Enter cart value (in ₹): "))

# discount_percent = 0


# if membership == "prime":
#     if cart_value >= 5000:
#         discount_percent = 0.30
#     elif cart_value >= 2000:
#         discount_percent = 0.15
#     else:
#         discount_percent = 0.05
# elif membership == "non-prime":
#     if cart_value >= 5000:
#         discount_percent = 0.10
#     else:
#         discount_percent = 0.0
# else:
#     print("Invalid membership type.")
#     exit()


# discount_amount = int(cart_value * discount_percent)
# print(f"Discount: {discount_amount}")
 
 
#q16  Online Exam Evaluation System

# Input
attendance = int(input("Enter attendance percentage: "))
avg_score = int(input("Enter average score: "))
min_subject_score = int(input("Enter minimum subject score: "))

# Decision logic
if attendance >= 75:
    if avg_score >= 50:
        if min_subject_score < 35:
            print("Fail: Subject Failed")
        else:
            print("Pass")
    else:
        print("Fail: Low Average Score")
else:
    print("Fail: Attendance Shortage")
 
 
        