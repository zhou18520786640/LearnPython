#coding:utf-8

# 引入模组的argv功能
from sys import argv

# 将argv解包，读到脚本名和文件名里面
script, filename = argv

# 根据文件名打开文件，存入到txt对象
txt = open(filename)

# 打印文件名
print "Here's your file %r:" % filename
# txt文件对象执行read()方法，输出文件内容
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()