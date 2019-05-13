
def splitIntoArray(path):
    with open(path) as file:
        lines = file.read().splitlines()
    print(lines)

if __name__ == '__main__':
    splitIntoArray('pn100.txt')
