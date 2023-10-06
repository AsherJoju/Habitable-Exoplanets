from enum import Enum
from scripts.color_generator import ColorGenerator
from scripts.color_settings import ColorSettings
from scripts.shape_generator import ShapeGenerator
from scripts.shape_settings import ShapeSettings
from scripts.terrain_face import TerrainFace
from ursina import Entity, Mesh, Vec3
from ursina.shaders import basic_lighting_shader


class Planet:
    
    class FaceRenderMask(Enum):
        
        ALL = 0
        TOP = 1
        BOTTOM = 2
        LEFT = 3
        ROGHT = 4
        FRONT = 5
        BACK = 6
    
    
    def __init__(
        self,
        resolution: int,
        face_render_mask: FaceRenderMask,
        shape_settings: ShapeSettings,
        color_settings: ColorSettings
    ):
        self.resolution = resolution
        self.face_render_mask = face_render_mask
        self.shape_settings = shape_settings
        self.color_settings = color_settings
        self.shape_generator = ShapeGenerator(self.shape_settings)
        self.color_generator = ColorGenerator(self.color_settings)
        
        self.entities: list[Entity] = []
        self.terrain_faces: list[TerrainFace] = []
    
    
    def construct_planet(self):
        self.initialize()
        self.generate_mesh()
        self.generate_colors()
    
    
    def initialize(self):
        self.shape_generator = ShapeGenerator(self.shape_settings)
        self.color_generator = ColorGenerator(self.color_settings)
        self.terrain_faces = []
        
        directions = [
            Vec3(0, 1, 0), # UP
            Vec3(0, -1, 0), # DOWN
            Vec3(-1, 0, 0), # LEFT
            Vec3(1, 0, 0), # RIGHT
            Vec3(0, 0, 1), # FRONT
            Vec3(0, 0, -1) # BACK
        ]
        
        for i in range(6):
            if len(self.entities) == i:
                entity = Entity(
                    model=Mesh(mode="triangle"),
                    shader=basic_lighting_shader
                )
                self.entities.append(entity)
            
            terrain_face = TerrainFace(
                self.shape_generator,
                self.entities[i].model,
                self.resolution,
                directions[i]
            )
            self.terrain_faces.append(terrain_face)
            
            render_face = (
                self.face_render_mask == Planet.FaceRenderMask.ALL
                or self.face_render_mask == list(Planet.FaceRenderMask)[i + 1]
            )
            self.entities[i].enabled = render_face
    
    
    def generate_mesh(self):
        for i in range(6):
            if self.entities[i].enabled:
                self.terrain_faces[i].construct_mesh()
    
    
    def generate_colors(self):
        for entity in self.entities:
            entity.color = self.color_settings.planet_color
