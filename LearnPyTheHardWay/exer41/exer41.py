# ex41: ex41 Leraning To Speak Object Oriented

import random
# from urllib import urlopen  #urlopen 损坏，无法调用，所以我改用openfile了

import sys

# WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class ###(###):":
        "Make a class nameed ### that is-a ###.\n创建一个叫做 ### 的类，并且它是一个 ###.",
    "class ###(object): \n\tdef __init__(self,***)" :
        "class ### has-a __init__ that takes self and *** parameters. \n类 ### 有一个__init__初始化，并且接受self 和 *** 作为变量",
    "class ###(object): \n\tdef ***(slef,@@@)":
        "class ### has-a function named *** that takes self and @@@ parameters.\n类 ### 有一个叫做 *** 的方法 并且会接受 self 和 @@@ 作为变量",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@. \n从***实例中获得***方法，并且使用self,@@@变量来调用它",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'. \n从***实例中获得***属性，并且将它设置成为 '***'."
}

# do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True

# load up the words from the website
for word in open("WordList.txt",'r').readlines():
    WORDS.append(word.strip()) # strip() 函数， delete unecessary symbols befor and after target strings such as ' ', "\t\n"

def convert(snippet,phrase):
    # 创建列表class_name 并赋值w，w是从WRODS列表中随机取出，?个元素（? 取决于，snippet列表里含有"###"的个数)
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
    other_names = random.sample(WORDS,snippet.count("***"))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence [:]

        # fake class names
        for word in class_names:
            result = result.replace("###",word,2)
            # Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
            # 如果指定第三个参数max，则替换不超过 max 次  str.replace(old, new[, max])

        # fake other names
        for word in other_names:
            result = result.replace("***",word,2)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 2)

        results.append(result)
    return results

# keep going until they hit Ctrl-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question , answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question , answer = answer, question
            print(question)
            input(">")
            print("ANSWER: %s\n\n" % answer)

except EOFError:
    print ("\nBye")


