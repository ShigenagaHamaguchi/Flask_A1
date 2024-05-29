TAX_RATE1 = 0.1
TAX_RATE2 = 0.2

BOUDER = 1000000
def calc_salary(salary):
    if salary < BOUDER:
        payamount = salary - salary*TAX_RATE1
    else:
        payamount = salary - (TAX_RATE1*BOUDER  + (salary-BOUDER)*TAX_RATE2)
    
    print(payamount)
    return round(payamount)


def calc_tax(salary):

    if salary < BOUDER:
        tax1 =salary*TAX_RATE1
        return tax1,None
    else:
        tax1 = TAX_RATE1*BOUDER
        tax2 = (salary-BOUDER)*TAX_RATE2
        return tax1,tax2