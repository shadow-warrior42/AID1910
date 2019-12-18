import os

DIR = "/home/tarena/备份/"
dir = input(">>") # 要备份的目录
if dir[-1] != '/':
    dir += '/'

# 拷贝文件
def copy(file):
    fr = open(dir+file,'rb')
    fw = open(DIR+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 选择要拷贝的文件
def main():
    file_list = os.listdir(dir)
    for file in file_list:
        if os.path.isfile(dir+file):
            copy(file)

if __name__ == '__main__':
    main()