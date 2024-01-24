"""
文件工具类
"""


# 接收传入文件的路径，打印文件全部内容，如果文件不存在则捕获异常输出提示信息，通过finally关闭文件对象
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding="utf-8")
        for line in f:
            print(line)
    except Exception as e:
        print(f"文件不存在,原因是{e}")
    finally:
        if f:    # 如果变量是None，则变量是False，则不会执行f.close，否则才会执行f.close
            f.close()


# 接收文件路径以及传入数据，将数据追加到文件中
def append_to_file(file_name, data):
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(data)
