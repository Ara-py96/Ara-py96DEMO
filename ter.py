from time import *
class place:
    area = "Chennai"
    def __init__(self,location):
        self.location = location
    def setWhere(self,where):
        self.where = where
        print("location is set as",self.where)
    def setLocation(self,place):
        self.area = place
    class building:
        def __init__(self,build):
            self.buid = build
        def buld(self,BULDNAME):
            print("##############################################################")
            for i in range(10):
                print("wait"+".")

            sleep(20)
            print("from",BULDNAME)
            print("build",BULDNAME,"has finised")
            print("location of",BULDNAME, "is in",self.buid,"in",place.area)
