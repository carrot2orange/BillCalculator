#No.1 
def setAmount (bill, tip):
	print "billAmount", bill, "tipPercentage", tip

#No.2
def total (bill, tip):
	return bill + bill*tip

#No.3
def split (tBill, numOfPeop):
	return round(tBill/numOfPeop)

#This is BillCalculator.py 
def main():
	choice = int(raw_input("choose 1-calculate tip or 2-split the bill"))
	if(choice == 1):
		billAmount = float(raw_input("How much is your bill?"))
    	tipPercentage = float(raw_input("What percentage do you want to tip?"))
    	print "total bill is", total(billAmount, tipPercentage)

	choice = int(raw_input("choose 1-calculate tip or 2-split the bill"))
	if(choice == 2):
	 	totalBill = float(raw_input("How much is your total bill?"))
	 	numOfPeople = int(raw_input("How many people in your party?"))
    	print "The cost per person is", split(totalBill, numOfPeople)

    # else:
    #  	print "choose just 1 or 2, please"

if __name__ == '__main__':
	main()
	
	

# '''
# tBill = 0
# #No.1 
# def setAmount (bill, tip):
# 	print "billAmount", bill, "tipPercentage", tip

# setAmount(17, 0.1)

# #No.2
# def total (bill, tip):
# 	return bill + bill*tip
# #Tip = billAmount * tipPercentage
# #TotalBill = billAmount + Tip

# print total(17, 0.1)
# tBill = total(17, 0.1)

# #No.3
# def split (numOfPeop):
# 	global tBill
# 	return round(tBill/numOfPeop)

# #numberOfPeople 
# #SplitedBill = TotalBill/numberOfPeople

# print split(3)
# '''