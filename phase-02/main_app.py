#humne bank_logic wale file ko yaha import kiya by using import module
# or import module ka use kr ke humne import utils ko bhi yaha import kiya
import bank_logic
import utils

# humne yaha ek new object banaya or bank_logic ko import kr ke ooske 
#ooske logic ko use kiya
user_1 = bank_logic.Account("Yadav Ji", 500000)

print("Welcome to the modular ATM")
user_1.show_info()

#by importing utils humne yaha random module ka use kiya.
sent_otp = utils.generate_otp()
print(f"The OTP is {sent_otp}")

#as well as by importing utils humne date.time module ka bhi use kiya.
current_time = utils.get_current_time()
print(f"The login time is {current_time}")

# idher humne chance naam ka variable banaya jiska value 5 hai
# iska use hai ki user ko bss 5 chance milege otp input krne ke lia
chance = 5
# fir humne while loop ka use kiya.
while chance > 0:
 try:
    user_input = int(input("Enter the otp: "))
    if user_input == sent_otp:
        print(f"Success ! logged time is {current_time}")
        user_1.show_info()

#yaha humne file handling ka concept use kiya hai.
#jisse run krne per ek txt.file create hoga 
#jisse pata chalega user ka login time or otp
        with open("Account_details.txt","a") as f:
            f.write(f"{user_1.name} logged at {current_time}\n")
            print(f"Account Holder name : {user_1.name}")
            print(f"Account balance is: {user_1.balance}")
            break
    else:
        if chance > 0:
            print("Wrong otp. Try again")
        else:
            print("Account blocked")
 except ValueError():
    print("Please Enter the otp in numbers")

