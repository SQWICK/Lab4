
def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        import json
        data = json.load(file)
    return data

def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('day,subject,time,weeks,teacher,building,room,format\n')

        for day, day_info in data['timetable'].items():
            lessons = day_info['lessons']
            for order, lesson_info in lessons.items():
                row = f"{day}," \
                      f"{lesson_info['subject']}," \
                      f"{lesson_info['time']}," \
                      f"{lesson_info['weeks']}," \
                      f"{lesson_info['teacher']}," \
                      f"{lesson_info['building']}," \
                      f"{lesson_info['room']}," \
                      f"{lesson_info['format']}\n"
                file.write(row)

# Чтение данных из файла
data = read_json('исходник.json')

write_csv('prog5.csv', data)

print("Расписание успешно преобразовано в формат CSV.")


