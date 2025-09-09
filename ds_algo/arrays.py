##### Dynamic Arrays #####
# Functions:
#   1. add element to the end O(1): append(x)
#   2. return index of first element with specified value O(n): index(x) 
#   3. delete the first element with specified value O(n): remove(x)

### Takeaways ###
# - Pay careful attention when moving the elements after delete and
#   make sure you are moving the right number of elements (pos,n-1)
#   not (pos,n)

# Initialize an array of max size 1 which is empty at first
# 1. Every time we add an element, check if max_size == current_size
#   If yes, double the size of array and create a new array of double
#   the size and copy the elements over
# 2. Returning index of the element is just a search till we find the element
# or reach the end of the array
# 3. To delete an element, we find the first element and copy all elements after
# it one index prior and change the size. Optionally, reduce the size of the array
# if the current # of elements is less than half the size of array

import ctypes

class CustomList:
  
  def __init__(self):
    self.size = 1
    self.n = 0
    self.container = self.__make_array(self.size)
    
  def append(self, x):
    if self.n == self.size:
      self.__resize(self.size*2)
    self.container[self.n] = x
    self.n += 1
  
  def index(self, x):
    for i in range(self.n):
      if self.container[i] == x:
        return i
    return None
  
  def delete(self, x):
    pos = self.index(x)
    if pos is None:  # also handles the empty case
      return None
    for i in range(pos, self.n-1):
      self.container[i] = self.container[i+1]
    self.n -= 1
    if self.n <= self.size/2:
      self.__resize(int(self.size/2))
      
  def __make_array(self, cap):
    return (cap * ctypes.py_object)()
  
  def __resize(self, cap):
    new_container = self.__make_array(cap)
    for i in range(self.n):
      new_container[i] = self.container[i]
    self.container = new_container
    self.size = cap
    
  def __str__(self):
    result = ""
    for i in range(self.n):
      result += str(self.container[i]) +","
    return f"[{result}] n={self.n} size={self.size}"


if __name__=="__main__":
  my_list = CustomList()
  # Append elements
  my_list.append(10)
  my_list.append(20)
  my_list.append(30)
  print("After appending 10, 20, 30:", my_list)
  # Find an element
  print("Index of 20:", my_list.index(20))
  print("Index of 15:", my_list.index(15))
  # Remove an element
  my_list.delete(20)
  print("After removing 20:", my_list)
  my_list.delete(15)
  print("After removing 15:", my_list)
  # Append elements
  my_list.append(40)
  print("After appending 40:", my_list)
