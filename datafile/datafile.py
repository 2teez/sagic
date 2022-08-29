import re
from typing import Union

datacontainer: dict[str, str] = {}


def _parse_each_line(line: str):
    '''
    parse each line, by getting all the non-empty colums. 
    Filter out need colums using first character of each line.
    if the first character is a number, that line is RNC, else
    it is a BSC. 
    ```NOTE```: The colums take for the two Element are different.
    '''
    global datacontainer
    line = list(line)[0]
    if line:
        # get all non-empty or space character us regexp
        values = re.findall(r'\S+', line)
        if values[0].isnumeric():
            datacontainer[values[5]] = values[0]
        else:
            values[5] = '' if values[5] == 'Available' else values[5]
            datacontainer[f'{values[4]} {values[5]}'.strip(' ')] = values[2]


def _get_line(line: str, look_for: str) -> Union[str, None]:
    'get each line needed'
    yield line if look_for in line else None


def _main(filename: str):
    'get filename and load it into a dictionary'
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            _parse_each_line(_get_line(line.strip(), 'National'))


def run():
    '''
    The only function that should exported from this module.
    '''
    import os
    filename = os.path.abspath('datafile/bscrnclisting.txt')
    if os.path.exists(filename):
        _main(filename)
    else:
        raise Exception(f'{filename} doesn\'t exist.')
    return datacontainer


if __name__ == '__main__':
    run()
