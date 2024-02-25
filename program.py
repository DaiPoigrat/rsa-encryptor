import sys
from console_manager import ConsoleManager

if __name__ == '__main__':
    arg_list = sys.argv[1:]

    manager = ConsoleManager()
    if len(arg_list) == 0:
        manager.help()

    while len(arg_list) > 0:
        try:
            arg = arg_list.pop(0)

            if arg.startswith('-'):
                match arg:
                    case '-k' | '--keys':
                        manager.generate_keys()
                    case '-e' | '--encrypt':
                        if len(arg_list) == 0:
                            manager.encrypt({})
                        else:
                            next_arg = arg_list.pop(0)
                            data = {}
                            if next_arg == '-p' or next_arg == '--path':
                                path_value = arg_list.pop(0)
                                data['-p'] = path_value
                            if next_arg == '-k' or '--key':
                                path_value = arg_list.pop(0)
                                data['-k'] = path_value
                            manager.encrypt(data)
                    case '-d' | '--decrypt':
                        if len(arg_list) == 0:
                            manager.decrypt({})
                        else:
                            next_arg = arg_list.pop(0)
                            data = {}
                            if next_arg == '-p' or next_arg == '--path':
                                path_value = arg_list.pop(0)
                                data['-p'] = path_value
                            if next_arg == '-k' or '--key':
                                path_value = arg_list.pop(0)
                                data['-k'] = path_value
                            manager.decrypt(data)
        except Exception as e:
            print(f'Wrong list of arguments')
            print(f'{e = }')
