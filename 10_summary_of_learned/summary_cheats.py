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

def must_pay_taxes(salary):
    tax = 0.2 
    min_salary_without_tax = 453
    taxed = salary - min_salary_without_tax
    must_pay_tax = taxed * tax 
    return must_pay_tax

print("Liida kalkulaator:")
a = int(input("Number 1: "))
b = int(input("Number 2: "))
print(a % b) # 5 % 2 == 5 - 2 - 2 == 1

while True:
  print("Palgakalkulaator:")
  a = int(input("Number 1: "))
  b = int(input("Number 2: "))
  # + - * /
  tehe = input("Mis tehet soovid teha (+ - * / %): ")
  if tehe == "+":
    print(a + b)

  if tehe == "-":
    print(a - b)

  if tehe == "/":
    print(a / b)

  if tehe == "*":
    print(a * b)



def calculator():
  print("Kalkulaator:")
  a = int(input("Number 1: "))
  b = int(input("Number 2: "))
  # + - * /
  tehe = input("Mis tehet soovid teha (+ - * / %): ")
  if tehe == "+":
    print(a + b)

  if tehe == "-":
    print(a - b)

  if tehe == "/":
    print(a / b)

  if tehe == "*":
    print(a * b)

  if tehe == "%":
    print(a % b)


def profit_tax_calculator():
  print("Palka maksu kalkulaator:")
  salary = int(input("Mis on palk?: "))
  profit_tax = 0.2
  for_taxes = salary * profit_tax
  print("for_taxes", for_taxes)
  worker_gets_to_bank = salary - for_taxes
  print("Palgafond: ", salary)
  print("Tulumaksu peab maksma: ", for_taxes)
  print("Tulumaks maha: ", worker_gets_to_bank)

while True:
  print("\n\nMis kalkulaatorit tahad kasutada?")
  print("a. Liitmine, lahutamine, jagamine, korrutamine, jääk (module %)")
  print("b. Tulumaksu kalkulaator")
  chosen_calculator = input("")

  if chosen_calculator == "a":
    calculator()

  if chosen_calculator == "b":  
    profit_tax_calculator()


# 3 küsimust õigesti == 5


array_of_animals = ["Tupsu", "Milli", "Muri", "Miisu"]
array_of_animal_ages = [10, 15, 7, 1]

print(array_of_animals[3])



array_of_animal_names = ["Tupsu", "Milli", "Muri", "Miisu"]
array_of_animal_ages = [10, 15, 7, 1]

i = 0
for name in array_of_animal_names:
  print(name, array_of_animal_ages[i])
  i = i + 1



array_of_animal_names = ["Tupsu", "Milli", "Muri", "Miisu"]
array_of_animal_ages = [10, 15, 7, 1]
array_of_fur_color = ["hall", "oranz", "pruun-must", "must"]

for i in range(0, len(array_of_animal_names)):
  print("i = ", i)
  print(array_of_animal_names[i], array_of_animal_ages[i], " ja ta on ", array_of_fur_color[i]," värvi")









animals = {
  {"name": "Tupsu", "age": 10, "color": "hall"},
  {"name": "Milli", "age": 15, "color": "oranz"},
  {"name": "Muri", "age": 7, "color": "pruun-must"},
  {"name": "Miisu", "age": 1, "color": "must"},
}

for i in range(0, len(animals)):
  print("i = ", i)
  print(animals[i]["name"], animals[i]["age"], " ja ta on ", animals[i]["color"]," värvi")






animals = [
  {"name": "Tupsu", "age": 10, "color": "hall"},
  {"name": "Milli", "age": 15, "color": "oranz"},
  {"name": "Muri", "age": 7, "color": "pruun-must"},
  {"name": "Miisu", "age": 1, "color": "must"},
]

animals[0]["age"] = 11
print(animals[3]["age"])

for i in range(0, len(animals)):
  print("i = ", i)
  print(animals[i]["name"], animals[i]["age"], " ja ta on ", animals[i]["color"]," värvi")

