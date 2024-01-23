"""
文件写入，如果没有目标文件，则创建文件，若有文件，则会覆盖文件内容
"""
f = open("F:/123.txt","w",encoding="utf-8")
f.write("hello,world")
f.flush()