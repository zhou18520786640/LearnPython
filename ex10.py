#coding:utf-8

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non aline."
backslash_cat = "I'm \\a\\cat"

fat_cat = """
I'll do a list:
\t*Cat food
\t*Fishies
\t*Catnip\n\t*Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#       常见转义字符
#       \'	  单引号
#       \"	  双引号
#       \a	  发出系统响铃声
#       \b	  退格符
#       \n	  换行符
#       \t	  横向制表符
#       \v	  纵向制表符
#       \r	  回车符
#       \f	  换页符
#       \o	  八进制数代表的字符
#       \x	  十六进制数代表的字符
#       \000	  终止符，\000后的字符串全部忽略

#       常见格式化字符字符
#       %c	 格式化字符及其ASCII码
#       %s	 格式化字符串
#       %d	 格式化整数
#       %u	 格式化无符号整型
#       %o	 格式化无符号八进制数
#       %x	 格式化无符号十六进制数
#       %X	 格式化无符号十六进制数（大写）
#       %f	 格式化浮点数字，可指定小数点后的精度
#       %e	 用科学计数法格式化浮点数
#       %E	 作用同%e，用科学计数法格式化浮点数
#       %g	 根据值的大小决定使用%f活%e
#       %G	 作用同%g，根据值的大小决定使用%f活%e
#       %p	 用十六进制数格式化变量的地址