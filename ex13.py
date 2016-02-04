#coding:utf-8

# sys 库（python中叫模组）
from sys import argv

script, first, second, third, fourth = argv
name = raw_input("your name?")

print "The script is called:" + script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your name variable is:" + name