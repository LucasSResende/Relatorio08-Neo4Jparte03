from pprintpp import pprint as pp
import EscolaDB as qProfs


def divider():
    print('\n' + '-' * 80 + '\n')




while 1:
    option = input('1. Create teacher\n'
                   '2. Create grade\n'
                   '3. Create relation teacher-grade\n')

    if option == '1':
        name = input('  nome do Professor: ')
        age = input('   Idade: ')
        area = input('  Área de atuação: ')
        person = {
            'name': name,
            'age': age,
            'area': area,
        }
        aux = qProfs.create(person)
        divider()


    elif option == '2':
        assunto = input('  Assunto da matéria: ')
        horario = input('   Horário: ')
        grade = {
            'assunto': assunto,
            'horario': horario

        }
        aux = qProfs.create_grade(grade)
        divider()

    elif option == '3':
        name = input('  nome do Professor: ')
        assunto = input('   Assunto: ')
        year = input('    Ano: ')
        relation = {
            'name': name,
            'assunto': assunto,
            'year': year
        }
        aux = qProfs.create_relation(relation)
        divider()



    elif option == '3':
        aux = qProfs.read_all_nodes()
        pp(aux)
        divider()

    else:
        break

qProfs.db.close()
