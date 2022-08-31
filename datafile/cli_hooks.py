from pprint import pprint
from datafile import run
import constants
import os
import sys
import re

container = run()


def _swap_hash_key_value(hasher: dict[str, str]) -> dict[str, str]:
    '''
    swap the dict values with keys. The function gets dictionary
    as parameter and returns dictionary.
    '''
    return dict(zip(list(hasher.values()), list(hasher.keys())))


def _modify_container(file: str) -> None:
    '''
    Read bscrnclisting.txt file and adjust the listing for rnc in the
    container.
    '''
    try:
        with open(file) as fin:
            for line in fin.readlines():
                if re.match(r'^\s+?$', line):
                    continue
                cols = re.findall(r'\S+', line)
                if cols[0].isnumeric() and 'National' in line:
                    container[cols[4]] = [cols[0], cols[5]]
    except Exception as ex:
        print(ex.args)
        # print(f'File with name`bscrnclisting.txt` is missing.')
        sys.exit()
    # finally:
    #     pprint(container)


def _user_input(msg: str, header: str = r'^[^0-9]') -> str:
    'Get user input, adjust it to meet the DPC'
    value = input(msg)
    if value == constants.ZERO_DPC:
        return value
    while re.match(header, value):
        print('Invalid input. Use Integers only', end='')
        print(f'( or Use {constants.ZERO_DPC} to Cancel.)')
        value = input(msg)
    return value.upper()


def main() -> None:
    global container
    container = _swap_hash_key_value(container)
    pprint(container)

    filename = os.path.abspath('datafile/bscrnclisting.txt')

    _modify_container(filename)

    result = container.get(f"H'00{_user_input('Enter DPC: ')}", None)

    lai = _user_input('Enter LAI (GCI or SAI): ', r'^62150')

    if isinstance(result, list):
        filename = f'{result[1]}.txt'
        #constants.print_sai(filename, **{})
        print(lai, result)
    elif isinstance(result, str):
        print(lai, result)
    else:
        print(f'\a\a\a'f'Invalid. The Network Element doesn\'t exists.')
        sys.exit()


if __name__ == '__main__':
    main()
