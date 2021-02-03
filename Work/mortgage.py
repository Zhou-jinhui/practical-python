# mortgage.py
#
# Exercise 1.7: Dave's mortgage

principal  = 500_000
rate       = 0.05
total_paid = 0.0
payment	   = 2684.11

while principal > 0:
	principal = principal * (1+rate/12) - payment
	total_paid += payment

print("Total paid", total_paid)


# Exercise 1.8: Extra payments

principal  = 500_000
rate       = 0.05
total_paid = 0.0
months     = 1

while principal > 0:
	if months <= 12:
		payment = 3684.11
	else:
		payment = 2684.11
	principal = principal * (1+rate/12) - payment
	total_paid += payment
	months += 1

print("Total paid", total_paid)
print("Months", months)


# Exercise 1.9: Making an Extra Payment Calculator

extra_payment_start_month = int(input("Extra payment start month: "))
extra_payment_end_month   = int(input("Extra payment end month: "))
extra_payment 			  = float(input("Extra paymnet: "))

principal  = 500_000
rate       = 0.05
total_paid = 0.0
months     = 1
origin_payment    = 2684.11

while principal > 0:
	if (
		months >= extra_payment_start_month and
		months <= extra_payment_end_month
		):
		payment = origin_payment + extra_payment
	else:
		payment = origin_payment
	principal = principal * (1+rate/12) - payment
	total_paid += payment
	months += 1

print("Total paid", total_paid)
print("Months", months)

# start month: 61
# end month: 108
# extra payment: 1000
# total pay: 880074.0999999964 total months: 311


# Exercise 1.10: Making a table

extra_payment_start_month = int(input("Extra payment start month: "))
extra_payment_end_month   = int(input("Extra payment end month: "))
extra_payment 			  = float(input("Extra paymnet: "))

principal  = 500_000
rate       = 0.05
total_paid = 0.0
months     = 0
origin_payment    = 2684.11

while principal > 0:
	months += 1
	if (
		months >= extra_payment_start_month and
		months <= extra_payment_end_month
		):
		payment = origin_payment + extra_payment
	else:
		payment = origin_payment
	principal = principal * (1+rate/12) - payment
	total_paid += payment
	print(months, round(total_paid, 2), round(principal, 2))

print("Total paid", round(total_paid, 2))
print("Months", round(months, 2))


# Exercise 1.11: Bonus

extra_payment_start_month = int(input("Extra payment start month: "))
extra_payment_end_month   = int(input("Extra payment end month: "))
extra_payment 			  = float(input("Extra paymnet: "))

principal  = 500_000
rate       = 0.05
total_paid = 0.0
months     = 0
origin_payment    = 2684.11

while principal > 0:
	months += 1
	if (
		months >= extra_payment_start_month and
		months <= extra_payment_end_month
		):
		payment = origin_payment + extra_payment
	else:
		payment = origin_payment
	principal = principal * (1+rate/12) - payment
	total_paid += payment
	if principal < 0:
		total_paid += principal
		principal = 0
	print(months, round(total_paid, 2), round(principal, 2))

print("Total paid", round(total_paid, 2))
print("Months", round(months, 2))


# Exercise 1.12: A Mystery