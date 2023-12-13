def min_inequity(salaries, n):
    salaries.sort()
    input_salary = salaries[:n]
    return max(input_salary) - min(input_salary)