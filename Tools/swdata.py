import json

class SwData:
    def __init__(self, jFile):
        with open(jFile) as json_file:
            self.data = json.load(json_file)

class Sw:
    def __init__(self, name):
        self.name = name
    def getSWName(self):
        return self.name

#TEST:
sd = SwData("c:\\Users\\uidk3912\\Desktop\\Automation_scripts\\Tools\\sw_data.json")

