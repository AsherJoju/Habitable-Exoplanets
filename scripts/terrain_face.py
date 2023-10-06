from ursina import Mesh, Vec2, Vec3

from scripts.shape_generator import ShapeGenerator


class TerrainFace:
    
    def __init__(self, shape_generator: ShapeGenerator, mesh: Mesh, resolution: int, local_up: Vec3):
        self.shape_generator = shape_generator
        self.mesh = mesh
        self.resolution = resolution
        self.local_up = local_up
        self.axis_a = Vec3(self.local_up.y, self.local_up.z, self.local_up.x)
        self.axis_b = Vec3(self.local_up.cross(self.axis_a))
    
    
    def construct_mesh(self):
        vertices: list[Vec3] = []
        triangles: list[tuple[int, int, int, int]] = []
        
        for y in range(self.resolution):
            for x in range(self.resolution):
                i = x + y * self.resolution
                percent = Vec2(x, y) / (self.resolution - 1)
                
                point_on_unit_cube = (
                    self.local_up
                    + (percent.x - 0.5) * self.axis_a * 2
                    + (percent.y - 0.5) * self.axis_b * 2
                )
                point_on_unit_sphere = Vec3(point_on_unit_cube.normalized())
                point_on_planet = self.shape_generator.get_point_on_planet(point_on_unit_sphere)
                
                vertices.append(point_on_planet)
                
                if x != self.resolution - 1 and y != self.resolution - 1:
                    triangles.append((
                        i,
                        i + self.resolution,
                        i + self.resolution + 1,
                        i + 1
                    ))
    
        self.mesh.vertices = vertices
        self.mesh.triangles = triangles
        self.mesh.generate_normals()
        
        self.mesh.generate()
