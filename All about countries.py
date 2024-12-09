class lebanon():
    def cap(self):
        print("The capital of lebanon is beirut")
    def lang(self):
        print("arabic is spoken in lebanon")
    def type(self):
        print("lebanon is an indeveloping country")
class USA():
    def cap(self):
        print("The capital of USA is washington DC")
    def lang(self):
        print("English is spoken in USA")
    def type(self):
        print("USA is a developing country")
obj_leb=lebanon()
obj_USA=USA()
for country in (obj_leb,obj_USA):
    country.cap()
    country.lang()
    country.type()