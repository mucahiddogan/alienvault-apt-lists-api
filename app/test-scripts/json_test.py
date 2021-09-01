import pandas as pd 

apt = pd.read_json("data.json")

with open("asd.txt","w") as text:
    text.write(apt.to_string())
print(apt.to_string())