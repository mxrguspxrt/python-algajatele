1
2
3
4
[1, 2, 3, 4]
"a"
"b"
"c"
["a", "b", "c"]
1+1
3-1
4/2
4*4
1 + 2 < 2
1 + 1 > 2

def must_pay_taxes(salary):
    tax = 0.2 
    min_salary_without_tax = 453
    taxed = salary - min_salary_without_tax
    must_pay_tax = taxed * tax 
    return must_pay_tax