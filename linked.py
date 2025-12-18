class LinkedList:
    def __init__(self,data):
        self.data=data
        self.next=None
list1=LinkedList(15)
list2=LinkedList(20)
list1.next=list2
print(list1.next.data)