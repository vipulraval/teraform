#recommend 3 standard tip amounts

server = input("what is your server's name?")
bill = float(input("How much was your total restaurant bill? $"))
bill_flt = format(bill,'.2f')

bill_15 = format((bill*0.15),'.2f')
bill_20 = format((bill*0.20),'.2f')
bill_25 = format((bill*0.25),'.2f')

# I was having trouble with the x.2f method of limiting float decimals
# did some searching to come up with the format(x,'.2f')
print(f"Suggested Tip Ammounts:\n\t 15%: ${bill_15} \n\t 20%: ${bill_20} \n\t 25%: ${bill_25}")

tip = input("Tell me your desired tip percentage and I will calculate your final bill. %")
tip_print = format((((float(tip))/100)* bill),'.2f')
total = format((((float(tip))/100) * bill + bill),'.2f')
print(f"\tYour original charge was: \t${bill_flt}")
print(f"\tYour tip amount is: \t\t% {tip_print}")
print(f"\tYour total will be: \t\t${total}")
print(f"Don't forget to thank your server {server} as well!")
