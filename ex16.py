# -*-coding:utf-8-*- 
from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
print "Opening the file..."
target = open(filename, 'w')  #首先需要把filename open， 然后才能进行读写操作

print "Truncating the file. Goodbye!"
target.truncate()  # 删除内容

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write those to the file."
#target.write(line1 + "\n" + line2 + "\n" + line3)  # + 进行连接
target.write("%r\n%r\n%r\n" % ( line1, line2, line3))  # 注意%(line1, line2, line3 的位置)
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
test = open(filename)
print test.read()
