with open('исходник.json', encoding='utf-8') as file:
    json_array = [line.rstrip() for line in file.readlines()]

outfile = open("prog0.yaml", 'w', encoding='utf-8')

for x in json_array:
    a = x.split(":")
    if len(a) > 1:
        a[0] = a[0].replace('"', '')
        a[1] = a[1].replace('"', '')
        if a[1][-1] == ',' or a[1][-1] == '{' or a[1][-1] == '[':
            a[1] = a[1][:-1]
        a[0] = a[0].replace('  ', '', 1)
        outfile.write(a[0] + ':' + a[1] + "\n")
print("Конвертация завершена. Результат сохранен в 'prog0.yaml'.")




