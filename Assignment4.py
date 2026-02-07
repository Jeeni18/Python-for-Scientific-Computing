class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        self.ar = None
        self.peri = None
    
    def area(self):
        self.ar = self.length * self.breadth

    def perimeter(self):
        self.peri = 2*(self.length + self.breadth)


rectangle1 = Rectangle(10,8)
rectangle1.area()
print("Area of rectangle:",rectangle1.ar)
rectangle1.perimeter()
print("Perimeter of rectangle:",rectangle1.peri)
print()

#question2
# height = [1,86,2,5,4,8,3,7]
# area1 = 1 * height[0]
# area = 0
# for i in height:
#     for height in range(0,-1):
#         area = j * (height)
#         if(area > area1):
#             area1 = area
# print("Required:",area1)

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         i, j = 0, len(height) - 1
#         ans = 0
#         while i < j:
#             t = (j - i) * min(height[i], height[j])
#             ans = max(ans, t)
#             if height[i] < height[j]:
#                 i += 1
#             else:
#                 j -= 1
#         return ans

# class ContainerWithMostWater:
#     def __init__(self, height):
#         self.height = height
    
#     def max_area(self):
#         max_area = 0
#         n = len(self.height)
        
#         for i in range(n):
#             for j in range(i + 1, n):
#                 width = j - i
#                 current_height = min(self.height[i], self.height[j])
#                 current_area = width * current_height
#                 max_area = max(max_area, current_area)
        
#         return max_area

# height = [1, 8,6, 2, 5, 4, 8, 3, 7]
# container = ContainerWithMostWater(height)
# result = container.max_area()
# print("Required:", result)  



# #create a superclass Shape and make its subclass rectangle and circle
class Shape:
    def __init__(self,area,perimeter) -> None:
        self.area = area
        self.perimeter = perimeter

    def info(self):
        print("Area: ",self.area)
        print("Perimeter: ",self.perimeter)

# class Rectangle(Shape):
#     def __init__(self,area,perimter,length,breadth):
#         super().__init__(area,perimter)
#         self.length = length
#         self.breadth = breadth 
    
#     def calculate_info(self):
#         length = 2

    
class Circle(Shape):
    def __init__(self,area,perimeter,radius):
        super().__init__(area,perimeter)
        self.radius = radius

    def calc_radius(self):
        radius = self.perimeter / (2 *3.14)
        print("Radius:",radius)


Shape1 = Shape(100,200)
Shape1.calc_radius()