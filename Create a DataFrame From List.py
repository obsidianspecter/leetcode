import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
   
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    
    
    print('+------------+-----+')
    print('| student_id | age |')
    print('+------------+-----+')
    for index, row in df.iterrows():
        print(f'| {row["student_id"]:<10} | {row["age"]:<3} |')
    print('+------------+-----+')
    
    return df


student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

createDataframe(student_data)
