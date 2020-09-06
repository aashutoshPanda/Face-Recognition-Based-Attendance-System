import pandas as pd

df = pd.read_excel(r'student_db/people_db.xlsx')

# print(df[1]['name'])
roll_record = {}
for key, row in df.iterrows():
    roll_no = row['roll_no']
    name = row['name']
    image_path = row['image']
    roll_record[roll_no] = name
