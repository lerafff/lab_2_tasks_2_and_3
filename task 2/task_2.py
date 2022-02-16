'''Lab 2 2'''
import sys
import json


def read_file(file_name):
    '''
    The function reads file
    '''
    with open(file_name, encoding='utf-8') as fille:
        text = json.load(fille)
    return text


def navigation_for_all(text):
    '''
    This function navigates us in the file and we can control it

    '''
    if isinstance(text, list):
        line = '- - - - - - - - - - - -'
        print(line*2 + '\nHere we have a list with ' + str(len(text)) +
              ' elements' + '\n' + line*2 + '\n')
        counter = 0
        for i in range(len(text)):
            print(str(i+1) + '.' + ' ' + 'text[' + str(counter) + ']')
            counter += 1
        counter = 0
        print(line * 2 + '\n1  I want to see all list\n2  \
I want to write an index of element\n3  I want to stop exploring the file')
        pos_options = ['1', '2', '3']
        while True:
            indexx = input(line*2 + '\n\nEnter a number \
(1-3) of offer please: ')
            if indexx in pos_options:
                break
        if indexx == '1':
            for elem in text:
                print(str(elem) + '\n')
        elif indexx == '2':
            while True:
                try:
                    index_to_find = int(input('Please enter a number \
between 0 and ' + str(len(text)) + ': '))
                    if 1 <= index_to_find <= len(text):
                        break
                except ValueError:
                    continue

            navigation_for_all(text[index_to_find - 1])
        elif indexx == '3':
            sys.exit()

    elif isinstance(text, dict):
        line = '- - - - - - - - - - - -'
        counter_2 = 1
        print(line*2 + '\nHere we have a dict with ' +
              str(len(text)) + ' keys\n' + line*2)
        for elem in text.keys():
            print(str(counter_2) + '.' + ' ' + elem)
            counter_2 += 1
        counter_2 = 0
        print(line*2 + '\n1  I want to see all dictionary\n2  \
I want to write a key of element\n3  I want to stop exploring \
the file\n' + line * 2)
        pos_options = ['1', '2', '3']
        while True:
            indexx_2 = input('Enter a number (1-3) of offer please: ')
            if indexx_2 in pos_options:
                break
        if indexx_2 == '1':
            print(text)
            sys.exit()

        elif indexx_2 == '2':
            while True:
                try:
                    index_to_find_2 = int(input('Please enter a number \
between 1 and ' + str(len(text.keys())) + ': '))
                    if 1 <= index_to_find_2 <= len(text.keys()):
                        break
                except ValueError:
                    continue

            key = list(text.keys())[index_to_find_2 - 1]
            navigation_for_all(text[key])

        elif indexx_2 == '3':
            sys.exit()
    elif isinstance(text, str):
        print(text)


def main():
    try:
        file_name = input('- ' * 17 + '\n' +
                          'Enter a path to the file please: ')
        text = read_file(file_name)
        navigation_for_all(text)
    except FileNotFoundError:
        print('\nSorry, it is not correct path to the file. try again!')
        main()
main()
