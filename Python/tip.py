#calculate the tips for meal & drinks
#allowing user to inpout the total value of the bill
total_amount = input("please enter the total bill amount? ")

#calculating the tip amoount for 20,25,30 percentage
per20=float(total_amount)*20/100
per25=float(total_amount)*25/100
per30=float(total_amount)*30/100
#displyingt the result to user
#total20=(per20+total_amount)

print (f" You can pay your tip \n\t @ 20% ${per20} \n\t @25% ${per25} \n\t @ 30% ${per30}")
