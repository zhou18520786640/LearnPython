#coding:utf-8

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

# 1.上网查一下raw_input什么功能？
# raw_input则是不管用户输入什么类型的都会转变成字符型.

# 2.raw_input再写一遍
print "What is your name?",
name = raw_input()
print "what is your job?",
job = raw_input()
print "what is your dream?",
dream = raw_input()
print "your name is %s, job is %s, dream is %s" % (name, job, dream)

