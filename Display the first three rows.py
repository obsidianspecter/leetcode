import pandas as pd
from typing import List

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
  
    first_three_rows = employees.head(3)
    
    
    return first_three_rows


data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

employees = pd.DataFrame(data)


result = selectFirstRows(employees)

print(result)
