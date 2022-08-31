from pprint import pprint
from typing import Union
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
    while re.match(header, value, re.MULTILINE) or value == '':
        print('Invalid input. Use Integers only', end='')
        print(f'( or Use {constants.ZERO_DPC} to Cancel.)')
        value = input(msg)
    return value.upper()


def _run(result: Union[list[str], str], **kwargs) -> None:
    if isinstance(result, list):
        filename = open(f'{result[1]}.txt', 'w')
        constants.print_sai(filename, **{'sai': kwargs['lai'], 'laisai_name': kwargs['name'],
                                         'rncid': result[0], 'cs_name': result[1]})
        filename.close()
    elif isinstance(result, str):
        filename = open(f'{result}.txt', 'w')
        constants.print_gci(filename, **{'gci': kwargs['lai'], 'laigci_name': kwargs['name'],
                                         'dpc': f"H'00{kwargs['dpc']}", 'cs_name': result})
    else:
        print(f'\a\a\a'f'Invalid. \nREASON: Remove the Zero(s) in front of the DPC,'
              f' then check again. OR ** The Network Element doesn\'t exists. **')
        sys.exit()


def main() -> None:
    global container
    container = _swap_hash_key_value(container)
    pprint(container)

    filename = os.path.abspath('datafile/bscrnclisting.txt')

    _modify_container(filename)

    dpc = _user_input('Enter DPC: ')
    result = container.get(f"H'00{dpc}", None)
    lai = _user_input('Enter LAI (GCI or SAI): ', r'^[^62150]')
    name = input('Enter Site Name: ')

    _run(result, **{'lai': lai, 'dpc': dpc, 'name': name})


if __name__ == '__main__':
    main()
