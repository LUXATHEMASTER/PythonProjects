from cs1lib import *
class City:     #Create city class

    def __init__(self,code,name,region,pop,latitude,longitude):#Initialise city values
        self.code=code
        self.name=name
        self.region=region
        self.pop=pop
        self.latitude=latitude
        self.longitude=longitude

    def __str__(self):      #Return city

        return self.name+","+str(self.pop)+","+str(self.latitude) +","+ str(self.longitude)






