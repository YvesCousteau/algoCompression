class Node(object):
    frequency = 0
    left = None
    right = None
    character = None
    code = None
    def __init__(self,character,frequency):
        self.character = character
        self.frequency = frequency
        pass
    def setChildren(self,left,right):
        self.left = left
        self.right = right
        pass
    def setCode(self,code):
        self.code = code
        pass
