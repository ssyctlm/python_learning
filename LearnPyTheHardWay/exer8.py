# --coding:utf-8 --
formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % ("I had this thing.", "That you could type up right.",
                   "But it didn't sing.", "So I said goodnight."))

#2 最后一行有单引号又有双引号，工作时，如果“”内内容没有‘ 符号，它打印时就显示’‘， 如果有’，它就显示“‘”
