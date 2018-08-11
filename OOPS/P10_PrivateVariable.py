# Author: PANDIT DANDGULE
# In this example we will see how the private variables work in Python

class Person(object):
    def __init__(self,name):
        self.name=name
        self.__education='Engineering' #private variable

    def displayInfo(self):
        name=self.name
        education=self.__education  #can only be access within a class
        print('My name is',name,'and I have completed my', education)

if __name__=='__main__':
    myObj=Person('Pandit')
    myObj.displayInfo()
    print(myObj.name)
    print(myObj._Person__education)



