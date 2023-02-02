import os
import json
from rich.console import Console

console = Console()

for root, dirs, files in os.walk(r'.\src\datapack\data'):
    if files != []:
        for file in files:
            filepath = f'{root}/{file}'.replace('\\', '/')
            with open(filepath, 'r') as file:
                data = json.load(file)
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            console.log(filepath)