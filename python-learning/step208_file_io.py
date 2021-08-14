import os

"""
def writeData():
    data = "\nHello World!"
    with open('file_io.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('file_io.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()
"""


fName = 'Hello.txt'


fPath = 'C:\\A\\'


abPath = os.path.join(fPath, fName)


print(abPath)


# /Users/vinhpham/Documents/GitHub/Python-Projects/python-learning/file_io.txt


if __name__ == "__main__":
    # writeData()
    # openFile()


