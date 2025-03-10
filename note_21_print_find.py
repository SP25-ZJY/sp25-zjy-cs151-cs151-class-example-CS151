def print_by_line(my_list):
    for item in my_list:
        print(item)

def find_first(name_list, char):
    for name in name_list:
        if name[0] == char:
            return name

    return "not found"

def main():
    fruit_list = ['Apple', 'Orange', 'Banana', 'Blueberry']
    print_by_line(fruit_list)
    name = find_first(fruit_list, 'Z')
    print('-' * 40)
    print(f'The first name that starts with Z is: {name}')

main()