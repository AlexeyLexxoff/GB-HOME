import json


def save_note(notes, file_path):
    with open(file_path, 'w') as file:
        file.write(json.dumps(notes, indent=4))

def load_notes(file_path):
    with open(file_path, 'r') as file:
        notes = json.loads(file.read())
        return notes


def add_note(notes, new_note):
    max_id = max(note['id'] for note in notes) if notes else 0
    new_note['id'] = max_id +1
    notes.append(new_note)


def edit_note(notes, note_id, new_title=None, new_datetime=None, new_body=None):
    for note in notes:
        if note['id'] == note_id:
            if new_title:
                note['title'] = new_title
            if new_body:
                note['body'] = new_body
            if new_datetime:
                note['datetime'] = new_datetime
            break





def delete_note(notes, note_id, ):
    notes[ : ] = [note for note in notes if note['id']!= note_id]

def main(note=None):
    file_path = 'notes.json'
    notes = load_notes(file_path)

    while True:
        print('1. Показать все записи')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Удалить запись')
        print('5. Выйти')

        select = input('Укажите действие')

        if select =='1':
            print('Записи: ')
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата,Время: {note['datetime']}")


        elif select =='2':
            title = input('Введите заголовок записи: ')
            body = input('Введите текст записи: ')
            datetime = input('Введите дату и всремя заметки (в формате "год-месяц-день, час-минута-секунда"): ')

            new_note = {
                'title': title,
                'body': body,
                'datetime': datetime
            }

            add_note(notes, new_note)
            save_note(notes, file_path)

        elif select == '3':
            note_id = int(input('Введите ID записи для изменения'))
            new_title = input('Введите новый заголовок записи')
            new_body = input('Введдите новый текст записи')
            new_datetime = input('Введите новую дату и время записи')

            edit_note(notes, note_id, new_title,new_body,new_datetime)
            save_note(notes,file_path)

        elif select =='4':
            note_id =  int(input('Укажите ID заметки для удаления'))

            delete_note(notes,note_id)
            save_note(notes,file_path)

        elif select =='5':
            break

        else:
            print('Неправильный ввод. Повторите еще раз')


if __name__ == '__main__':
    main()
