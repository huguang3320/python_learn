"""
读取文件
将文件写入到bill.txt.bak文件作为备份
同时，将文件中带有“测试”的字样的数据行丢失
"""
wr = open("F:/bill.txt.bak","a",encoding="utf-8")

with open("F:/123.txt","r",encoding="utf-8") as f:
    for line in f.readlines():
        if line.count("测试") > 0:
            continue
        else:
            wr.write(line)
    wr.flush()