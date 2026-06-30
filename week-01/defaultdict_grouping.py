employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 72000},
    {"name": "Bob", "dept": "Sales", "salary": 58000},
    {"name": "Carla", "dept": "Engineering", "salary": 81000},
    {"name": "David", "dept": "Sales", "salary": 62000},
    {"name": "Eva", "dept": "Marketing", "salary": 55000},
    {"name": "Frank", "dept": "Engineering", "salary": 69000},
]

from collections import defaultdict

def average_salary(rate):
    d = defaultdict(list)
    for x in rate:
        d[x["dept"]].append(x["salary"])

    result = {}
    for depts, salaries in d.items():
        result[depts] = sum(salaries) / len(salaries)
    return result

print(average_salary(employees))
