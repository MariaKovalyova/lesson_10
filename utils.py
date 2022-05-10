import json

json_file = "candidates.json"  # Файл с базой данных


def load_json(): # функция загрузки файла
    with open(json_file, 'r', encoding="UTF=8") as file:
        file = json.load(file)
        return file


def get_person(in_data=None):

    file = load_json()  # Загружаем файл из функции
    candidates_list = "<pre>"  # Иоговоый список кандидатов

    for person in file:
        """Если ничего в функцию не передано, то цикл пройдёт по всем позициям
           Если передано число, то выберёт персонажа с нужным id
           Если передано слово, то выберёт персонажа с нужным skill"""

        if in_data == str(person.get('id')) or in_data is None or in_data.lower() in (person.get('skills')).lower():
            candidates_list += (
            f"Имя кандидата - {person.get('name')}\n" +
            f"Позиция кандидата - {person.get('position')}\n" +
            f"Навыки - {person.get('skills')}\n\n"
            )
            if in_data == str(person.get('id')):  # Если совпадает с id, то прикрепляем изображение и стоп цикл
                candidates_list = f"<img src={person.get('picture')}>\n" + candidates_list
                break
    candidates_list += "</pre>"  # добавляем форматирование в конце

    return candidates_list

