#Daily Challenge : Pagination
import math
class Pagination():
    
    def __init__(self, items = None, page_size = 10):
        if items == None:
            items = []
        self.items = items
        self.page_size =page_size
        self.current_index = 0
        self.total_page = math.ceil(len(items)/self.page_size)
        
        
    def get_visible_items(self):
        start = self.current_index * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # def go_to_page(self, page_num):
    #     if page_num < 1 or page_num > self.total_pages:
    #         return ValueError("Page number out of range")
    #     self.current_index = page_num - 1
    #     return self

    def go_to_page(self, page_num):
        if 1 <= page_num <= self.total_page:
            self.current_index = page_num - 1   
            return self                         
        else:
            raise ValueError("Page number out of range")  

    def first_page(self):
        self.current_index = 0
        return self
            
        
    def last_page(self):
        self.current_index = self.total_page -1
        return self
        
    def next_page(self):
        if self.current_index < self.total_page - 1:
            self.current_index += 1
        return self

    def previous_page(self ):
        if self.current_index < self.total_page - 1:
            self.current_index -= 1
        return self

    def __str__(self):
        visible_items = self.get_visible_items()
        return "\n".join(str(item) for item in visible_items)
    
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
       
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(e)  # prints: Page number out of range

print(p.current_index + 1)
# Output: ValueError
    
try:
    p.go_to_page(0)
# Raises ValueError  
except ValueError as e:
    print("", e)

print("Current page:", p.current_index + 1)    
            
