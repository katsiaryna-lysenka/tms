import json
import pandas as pd

try:
    with open('my_json_file.json', 'r') as f:
        data = json.loads(f.read())

    output = ','.join([*data[0]])
    print(output)
    for obj in data:
        output += f'\n{obj["id"]},{obj["Name"]},{obj["Age"]}'
    print(output)
    with open('output.csv', 'w') as f:
        f.write(output)

except Exception as ex:
    print(f'Error: {str(ex)}')

df = pd.DataFrame(dict(phone=['76436', '24113', '53422', '24242', '65335']))
df.to_csv('output.csv', mode='a', index=False, header=False)
