import os


class FileReader(fname):
    def __init__(self, fname):
        self.input = fname

    def robocopy(self):
        f = open(self.input)
        print(f.readlines())


def main():
    fname = input('enter file name: ')
    myClass = FileReader(fname)
    myClass.robocopy()


if __name__ == "__main__":
    main()
