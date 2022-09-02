class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 1

    def add_at_tail(self, data) -> bool:
        # Write code here
        temp = Node(data)
        temp.next = self.head
        temp.previous = self.head.previous
        self.head.previous = temp
        temp.previous.next = temp
        self.count += 1
        return True

    def add_at_head(self, data) -> bool:
        # Write code here
        if self.head == None:
            temp = Node(data)
            self.head = temp
            self.head.next = self.head
            self.head.previous = self.head
            self.count += 1
            #print(self.count,"???")
            return True
        else:
            temp = Node(data)
            temp.next = self.head
            temp.previous = self.head.previous
            self.head.previous = temp
            temp.previous.next = temp
            self.head = temp
            self.count += 1
            return True

    def add_at_index(self, index, data) -> bool:
        # Write code here
        if index>=0 and index<=self.count:
            if index == self.count :
                self.add_at_tail(data)
                return True



            elif index == 0:
                self.add_at_head( data)
                return True
            else:
                a = 0
                self.count += 1
                insert_node = Node(data)
                index_node = self.head
                while (a < index):
                    index_node = index_node.next
                    a += 1
                insert_node.next = index_node
                insert_node.previous = index_node.previous
                insert_node.previous.next = insert_node
                index_node.previous = insert_node
                return True

    def get(self, index) -> int:
        # Write code here

        if index < 0 and index >= self.count:
            return -1
        elif  self.head== None:
            return -1
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.data

    def delete_at_index(self, index) -> bool:
        # Write code here
        if index >= 0 and index < self.count:
            if index == 0:
                self.head.previous.next = self.head.next
                self.head.next.previous = self.head.previous
                self.head = self.head.next
                self.count -= 1
                return True
            elif index == self.count - 1:
                temp = self.head.previous
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                self.count -= 1
                return True
            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                self.count -= 1
                return True

        else:
            return False

    def get_previous_next(self, index) -> list:
        # Write code here
        if index >= 0 and index < self.count:
            l = []
            temp = self.head
            for i in range(index):
                temp = temp.next
            l.append(temp.previous.data)
            l.append(temp.next.data)
            return l
        else:
            return -1

    def display(self):
        temp=self.head
        print(self.count)
        for i in range (self.count):
            print(temp.data,"*",i)
            temp=temp.next

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0
for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)
obj = DoublyCircularLinkedList()
result = []


for i in range(len(operations)):

    if operations[i] == "add_at_head":
        a=obj.add_at_head(data[i])
        if a!=None:
            result.append(a)
        else:
            result.append(False)
        #print(obj.add_at_head(data[i]),"***")
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
        #print(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        a=obj.add_at_index(int(data[i][0]), data[i][1])
        if a!=None:
            result.append(a)
        else:
            result.append(False)
        #print(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
        #print(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
        #print(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))
        #print(obj.delete_at_index(data[i]))
    #print("\n\n")
    #print(obj.count,"MMMMMM")
    #obj.display()
    #print(i,"++++")
    #print("\n\n")

print(result)

