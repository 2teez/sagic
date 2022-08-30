from pprint import pprint
from datafile import run


container = run()

def swap_hash_key_value(hasher: dict[str, str]) -> dict[str, str]:
    '''
    swap the dict values with keys. The function gets dictionary
    as parameter and returns dictionary.
    '''
    return dict(zip(list(hasher.values()), list(hasher.keys())))


def main() -> None:
    global container
    container = swap_hash_key_value(container)
    pprint(container)

if __name__ == '__main__':
    main()
