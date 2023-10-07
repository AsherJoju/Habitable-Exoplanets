from scripts.color_settings import ColorSettings
from scripts.min_max import MinMax
from shaders.height_shader import HeightShader
from ursina import Color, Vec3


class ColorGenerator:
    
    def __init__(self, settings: ColorSettings):
        self.texture_resolution = 64
        self.settings = settings
        self.texture: list[tuple] = []
        
        biomes = []
        for biome in self.settings.biome_color_settings.biomes:
            biomes.append(biome.start_height)
        
        self.shader = HeightShader(
            MinMax(),
            biomes,
            self.texture,
            (len(self.settings.biome_color_settings.biomes), self.texture_resolution)
        )
    
    
    def update_elevation(self, elevation_min_max: MinMax):
        self.shader.default_input["min_max"] = elevation_min_max.tuple()
    
    
    def update_colors(self):
        self.texture = []
        
        for biome in self.settings.biome_color_settings.biomes:
            for i in range(self.texture_resolution):
                g_col = biome.gradient.evaluate(i / (self.texture_resolution - 1))
                tint = biome.tint
                self.texture.append(
                    g_col * (
                        1 - biome.tint_percent
                    ) + Vec3(
                        tint.r,
                        tint.g,
                        tint.b
                    ) * biome.tint_percent
                )
        
        self.shader.default_input["texture"] = self.texture
        self.shader.default_input["height"] = len(self.settings.biome_color_settings.biomes)
        self.shader.default_input["width"] = self.texture_resolution
    