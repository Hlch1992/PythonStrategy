import os


class FileReader():
    def __init__(self, input, out):
        self.input = input
        self.out = out

    def robocopy(self):
        f = open(self.input)
        o = open(self.out, 'w')
        o.writelines(f.readlines())


def main():
    myClass = FileReader(r'C:\Users\Hlch1\ReadInThisFile.txt', r'C:\Users\Hlch1\WriteOutThisFile.txt')
    myClass.robocopy()


if __name__ == "__main__":
    main()
