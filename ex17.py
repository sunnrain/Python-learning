# -*-coding:utf-8-*- 
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read() #结尾无须in_file.close()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)  #如果不存在，会自动生成并写入
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input ("?")


out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()