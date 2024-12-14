import re
with open('исходник.json', encoding='utf-8') as file:
    json_array = [line.rstrip() for line in file.readlines()]

outfile = open("prog2.yaml", 'w', encoding='utf-8')

pattern = r'[\{\}":]'

for x in json_array:
    a = x.split(":")
    if len(a) > 1:
        a[0] = a[0].replace('"', '')
        a[1] = re.sub(pattern, "", a[1])
        a[1] = a[1].replace('"', '')
        a[0] = a[0].replace('  ', '', 1)
        outfile.write(a[0] + ':' + a[1] + "\n")
print("Конвертация завершена. Результат сохранен в 'prog2.yaml'.")