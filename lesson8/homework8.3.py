import json
from pathlib import Path

current_path = Path(__file__)
current_dir = current_path.parent
dict_ = [{
    "id": 123456,
    "Name": "Sam",
    "Age": 35
},{
    "id": 765432,
    "Name": "Alex",
    "Age": 54
},{
    "id": 653246,
    "Name": "Dina",
    "Age": 76
},{
    "id": 325678,
    "Name": "Tom",
    "Age": 22
},{
    "id": 653578,
    "Name": "Eva",
    "Age": 13
}]
with open(
    current_dir.joinpath("my_json_file.json"),
    mode="w"
) as w_file:
    json.dump(dict_, w_file, indent=5)

