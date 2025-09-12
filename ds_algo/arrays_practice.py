
import ctypes  # used for c arrays

class CustomList:
    
    def __init__(self):
        pass
    
    def __make_array(self, cap):
        pass
    
    def __resize_array(self, cap):
        pass
    
    def __str__(self):
        result = ""
        for i in range(self.n):
            result += f"{self.container[i]},"
        return f"({self.n}/{self.cap}) [{result}]"
    
    def append(self, x):
        pass
    
    def index(self, x):
        pass
    
    def delete(self, x):
        pass

if __name__ == "__main__":
    my_list = CustomList()
    print("Initializing:", my_list)
    # Append elements
    my_list.append(10)
    print("After appending 10:", my_list)
    my_list.append(20)
    print("After appending 20:", my_list)
    my_list.append(30)
    print("After appending 30:", my_list)
    # Find an element
    print("Index of 20:", my_list.index(20))
    print("Index of 15:", my_list.index(15))
    # Remove an element
    my_list.delete(20)
    print("After removing 20:", my_list)
    my_list.delete(15)
    print("After removing 15:", my_list)
    my_list.delete(10)
    print("After removing 10:", my_list)
    # Append elements
    my_list.append(40)
    print("After appending 40:", my_list)
