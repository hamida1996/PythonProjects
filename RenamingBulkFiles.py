import os

def main(path):
    i = 0
    for file_name in os.listdir(path):
        dest = "image" + str(i) + ".jpg"
        source = path + file_name
        dest = path + dest
        os.rename(source, dest)
        i += 1

if __name__ == '__main__':
    _input = input("Paste the directory address: ")
    address = _input.replace("\\", "/") + '/'
    main(address)
