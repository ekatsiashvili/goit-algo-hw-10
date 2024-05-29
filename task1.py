import pulp

# Створення проблеми лінійного програмування
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Визначення змінних
# x - кількість виробленого "Лимонаду"
# y - кількість виробленого "Фруктового соку"
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Визначення об'єктивної функції (максимізація загальної кількості продуктів)
problem += x + y, "Total_Products"

# Визначення обмежень
problem += 2 * x + y <= 100, "Water_Constraint"
problem += 1 * x <= 50, "Sugar_Constraint"
problem += 1 * x <= 30, "Lemon_Juice_Constraint"
problem += 2 * y <= 40, "Fruit_Puree_Constraint"

# Розв'язання проблеми
problem.solve()

# Виведення результатів
print("Status:", pulp.LpStatus[problem.status])
print("Lemonade Production:", pulp.value(x))
print("Fruit Juice Production:", pulp.value(y))
print("Total Products Produced:", pulp.value(problem.objective))