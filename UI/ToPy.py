# 转换工程文件到Python脚本

# qrc： pyside2-rcc $FileName$ -o $FileNameWithoutExtension$.py
# ui： pyside2-uic $FileName$ -o $FileNameWithoutExtension$.py
import os


# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            FilePath = os.path.join(root, f)

            try:
                father_path,fullname = os.path.split(FilePath)
                name,extension = fullname.split('.')
                if extension == 'qrc':
                    comm = 'pyside2-rcc '+father_path+'\\'+fullname+' -o '+os.getcwd()[0:-3]+'\\'+name+'_rc.py'
                    print(comm)
                    os.system(comm)
                elif extension == 'ui':
                    comm = 'pyside2-uic ' + father_path + '\\' + fullname + ' -o ' + name + '.py'
                    print(comm)
                    os.system(comm)
            except:
                pass

if __name__ == '__main__':
    print('Working path:',os.getcwd())
    try:
        walkFile(os.getcwd())
        print('成功')
    except:
        print('转换失败，检查文件完整性')
