from my_utils import str_util,file_util

s = str_util.str_reverse("hello world")
print(s)

ss = str_util.substr("hello world", 1,4)
print(ss)

file_util.print_file_info("F:/1234.txt")

#file_util.append_to_file("F:/123.txt","aaaaabbbbbcccc \n")