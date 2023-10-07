from ursina import Color, Vec3


class Gradient:
    
    def __init__(self, gradient: list[tuple[float, Color]]):
        self.gradient = gradient
    
    
    def get_gradient(self):
        return self.gradient
    
    
    def get_points(self):
        points = []
        
        for point in self.gradient:
            points.append(point[0])
        
        return points
    
    
    def get_colors(self):
        points = []
        
        for point in self.gradient:
            points.append(tuple(point[1]))
        
        return points
    
    
    def evaluate(self, point: float):
        for i in range(len(self.gradient)):
            point1, color1 = self.gradient[i]
            point2, color2 = self.gradient[i + 1]
            
            # print(point1, point, point2, point1 <= point and point <= point2)
            
            if point1 <= point and point <= point2:
                t = (point - point1) / (point2 - point1)
                
                color = Vec3(
                    (color1.r + (color2.r - color1.r) * t),
                    (color1.g + (color2.g - color1.g) * t),
                    (color1.b + (color2.b - color1.b) * t)
                )
                return color
        return Vec3(0, 0, 0)
