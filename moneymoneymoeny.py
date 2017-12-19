def calculate_years(principal, interest, tax, desired):
    interest_amount = principal * interest
    taxed_amount = interest_amount * tax
    new_total = principal + interest_amount - taxed_amount
    years = 1
    print(new_total)
    if new_total > desired:
        years= 0
    else:
        while new_total < desired:
          principal = new_total
          interest_amount = principal * interest
          taxed_amount = interest_amount * tax
          new_total = principal + interest_amount - taxed_amount
          years += 1
          print(new_total)
    print(years)
    return years


# better solution 

def calculate_years_c(principal, interest, tax, desired):
  count = 0
  sum = principal
  while sum < desired:
    count += 1
    yearly_interest = sum * interest
    yearly_interest -= yearly_interest * tax
    sum += yearly_interest
  return count