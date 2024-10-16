class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if(self.occupation=="Doctor"):
            print(self.name , "goes to Hospital daily.")
        elif(self.occupation=="Farmer"):
            print(self.name , "goes to Fields daily.")
    def speaks(self):
        print(self.name ,"says Hii to Everyone.")
    
x=Human("Ram","Doctor")
x.do_work()
x.speaks()
