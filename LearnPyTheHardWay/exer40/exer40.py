# ex40:Modules, Classes, And Objects
import mystuff

mystuff.apple()

a = mystuff.tangerine
print(a)

sample_class = mystuff.MyStuff() # 实例化 instantiate

print(sample_class.tangerine)
sample_class.apple()

thing = mystuff.MyStuff() # 实例化 instantiate
thing.apple()
print(thing.tangerine)

## getting things from things
### dict style
# mystuff['apple']

### module style
mystuff.apple()
print(mystuff.tangerine)

###class style
thing = mystuff.MyStuff()
thing.apple()
print(thing.tangerine)


class Song():
    def __init__(self, *lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics[0]:
            print(line)

    def sing_another_song(self, *lyrics):
        for line in self.lyrics:
            print(line, end="-")

print("\n"*5)
happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "Whith pockets full of shells"])

indians = Song(["one little","two little","three little indians"])

happy_baby.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
indians.sing_me_a_song()

abc = Song("A","B","C","D","E","F","G")
abc.sing_another_song()





