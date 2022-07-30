# ввод данных пользователем и запись в файл


def add_contact():  
    id = input('введите номер id')                    
    name = input('Имя: ')
    surname = input('Фамилия: ')
    phone = input('Номер телефона: ')
    comment = input('Комментарий: ')
    return [id, name, surname, phone, comment]

    def write_data_one_string(data):
        data_str = ''
    for each in data:
        data_str += each + ';'
    data_str += '\n'
    with open('phonebook.txt', 'a') as file:
        file.write(data_str)


def write_data_dif_string(data):
    with open('phonebook.txt', 'a') as file:
        for each in data:
            file.write(each)
            file.write('\n')



# def delete_contact(self):
#         self.loadAll()

#         entry_to_delete = input("ENTER NAME OF ENTRY TO DELETE: ")
#         if entry_to_delete in self.phonebook.keys():
#             del self.phonebook[entry_to_delete]
#             file = open(self.phonebook_file, 'w')
#             for name, number in self.phonebook.items():
#                 string = name + '\t' + number + '\n'
#                 file.write(string)
#             file.close()
#             print("ENTRY DELETED SUCCESSFULLY")

