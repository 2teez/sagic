
from datafile.datafile import run
from datafile import constants
import re
import sys

# network elements names, id for 3G and dpc for 2G
datacontainer = run()


def _check_file(file: str) -> bool:
    'check if the file exists'
    if os.path.exists(os.path.abspath(file)):
        return True
    return False


def _modification(value):
    'Generate hexi-decimal numbers for LAC and CELLIDs'
    try:
        value = '%X' % int(value)
    except Exception as ex:
        print(f'{ex.args}')
        sys.exit()

    value = f'0{value}' if len(value) <= 3 else f'{value}'
    return value


def _make_laigci(lst: list[str]):
    'Make a site configuration for 2G. Write to a new or existing file'
    cs_name = lst[0]

    dpc = datacontainer.get(cs_name, None)

    # when dpc is None -- different case
    if not dpc:
        cs_name = (list(elem
                        for elem, _ in datacontainer.items() if cs_name[1:] in elem[1:])) or None
        cs_name = cs_name[0] if cs_name else 'NOT AVALIABLE'
        dpc = datacontainer.get(cs_name, constants.ZERO_DPC)

    laigci_name = lst[2]
    lac = _modification(lst[1])
    cellid = _modification(lst[3])
    gci = f'62150{lac}{cellid}'

    # check if the file exist
    filename = f'{cs_name}.txt'
    filehandler = open(filename, 'a') if _check_file(
        filename) else open(filename, 'w')

    constants.print_gci(filehandler, **{'gci': gci, 'laigci_name': laigci_name,
                                        'dpc': dpc, 'cs_name': cs_name})


def _make_laisai(lst: list[str]):
    'Make a site configuration for 3G. Write to a new or existing file'
    cs_name = lst[0]
    rncid = datacontainer.get(cs_name, 'Not Avaliable.')
    laisai_name = lst[2]

    lac = _modification(lst[1])
    cellid = _modification(lst[3])
    sai = f'62150{lac}{cellid}'

    # check if the file exist
    filename = f'{cs_name}.txt'
    filehandler = open(filename, 'a') if _check_file(
        filename) else open(filename, 'w')

    constants.print_sai(filehandler, **{'sai': sai, 'laisai_name': laisai_name,
                                        'rncid': rncid, 'cs_name': cs_name})


def _data_munch(line: str):
    'Check in each line for either BSC or RNC and use approprate function.'
    values = list(wrd.group() for wrd in re.finditer(r'\S+', line))
    # check the length of the each data line.
    # it MUST be in 4 colums. If more concatenate the first two colums
    if len(values) > 4:
        values[0] = f'{values[0]} {values[1]}'
        values.pop(1)  # remove the concatenated colum 1

    if 'bsc' in values[0].lower():
        _make_laigci(values)
    else:
        _make_laisai(values)


def main(file: str):
    '''
    Read through the file: [datafiles.txt].
    For each of the line, call function: [_data_munch].
    '''
    with open(file, 'r') as fin:
        for line in fin.readlines():
            _data_munch(line)


if __name__ == '__main__':
    import os
    '''
    check if the file ```datafiles.txt``` exists.
    if not raise an exception to get the file which
    with data that is needed.
    '''
    filename = 'datafiles.txt'
    try:
        if not os.path.exists(filename):
            raise Exception('Usage: python3 sagic.py')
    except Exception as ex:
        print(f'{ex.args[0]}')
        print(f'You MUST have file with filename ```datafiles.txt```')
        sys.exit()
    main(filename)
