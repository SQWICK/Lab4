import json
import yaml

data = "исходник.json"

with open(data, 'r', encoding='UTF-8') as file:
    data_json = json.load(file)
    data_yaml = yaml.dump(data_json, default_flow_style=False, allow_unicode=True)

with open("prog1.yaml", 'w', encoding='UTF-8') as outfile:
    outfile.write(data_yaml)
    print("Конвертация завершена. Результат сохранен в 'prog1.yaml'.")
