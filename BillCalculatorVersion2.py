#This is BillCalculatorVersion2.py in activity3 at scope class.
tip_amount = 0
total_bill= 0
split_amount = 0
def calculate_bill(original_bill_amount, tip_percentage=18, split_number=1):
	global tip_amount
	global total_bill
	global split_amount
	tip_amount = original_bill_amount*tip_percentage*0.1
	total_bill = original_bill_amount + tip_amount
	split_amount = total_bill/split_number
	print "original bill is", original_bill_amount
	print "tip amount", tip_amount
	print "total bill", total_bill
	print "split amount", split_amount

def main():
 	calculate_bill(100)
 	calculate_bill(100, tip_percentage=20)
 	calculate_bill(100, 25, 3)
 	calculate_bill(100, split_number=2)

if __name__ == '__main__':
	main()
