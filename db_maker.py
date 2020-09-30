import os
import pandas as pd
image_dir = os.path.join("student_db")
data = []
for index, filename in enumerate(os.listdir(image_dir), start=1):
    if filename.endswith(".png"):
        new_name = filename.replace(" ", "_")
        os.rename(str(image_dir) + os.sep + filename,
                  str(image_dir)+os.sep + new_name)
        print(new_name)
        data.append([new_name, new_name, index])

df = pd.DataFrame(data, columns=['name', 'image', 'roll_no'])
df.to_excel("student_db/people_db.xlsx")
