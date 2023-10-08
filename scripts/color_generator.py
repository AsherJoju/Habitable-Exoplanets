from opensimplex import OpenSimplex
from time import time_ns
from scripts.color_settings import ColorSettings
from scripts.min_max import MinMax
from scripts.noise_filter_factory import NoiseFilterFactory
from scripts.noise_settings import NoiseSettings
from shaders.height_shader import HeightShader
from ursina import Vec3


class ColorGenerator:
    
    def __init__(self, settings: ColorSettings):
        self.texture_resolution = 128
        self.settings = settings
        self.texture: list[tuple] = []
        self.noise_filter = NoiseFilterFactory.create_noise_filter(
            self.settings.biome_color_settings.noise
        )
        self.shader = HeightShader(
            MinMax(),
            self.texture,
            (len(self.settings.biome_color_settings.biomes), self.texture_resolution)
        )
    
    
    def get_biome_percent_from_point(self, point: Vec3):
        height_percent = (point.y + 1) / 2.0
        height_percent += (
            self.noise_filter.evaluate(point) - self.settings.biome_color_settings.noise_offset
        ) * self.settings.biome_color_settings.noise_strength
        biome_index = 0
        num_biomes = len(self.settings.biome_color_settings.biomes)
        blend_range = self.settings.biome_color_settings.blend / 2.0 + 0.0001 # Make it Non-Zero
        
        # for i in range(num_biomes):
        #     distance = height_percent - self.settings.biome_color_settings.biomes[i].start_height
        #     weight = inverselerp(-blend_range, blend_range, distance)
            
        #     biome_index *= (1 - weight)
        #     biome_index += i * weight

        for i in range(num_biomes):
            if self.settings.biome_color_settings.biomes[i].start_height < height_percent:
                biome_index = i
            else:
                break
        
        biome_index = max(0, min(biome_index, num_biomes - 1))
        
        return biome_index / max(1, num_biomes - 1)
    
    
    def update_elevation(self, elevation_min_max: MinMax):
        self.shader.default_input["min_max"] = elevation_min_max.tuple()
    
    
    def update_colors(self):
        self.texture = []
        
        for biome in self.settings.biome_color_settings.biomes:
            for i in range(self.texture_resolution):
                g_col = biome.gradient.evaluate(i / (self.texture_resolution - 1))
                tint = biome.tint
                self.texture.append(
                    g_col * (1 - biome.tint_percent)
                    + Vec3(tint.r, tint.g, tint.b) * biome.tint_percent
                )
        
        self.shader.default_input["texture"] = self.texture
        self.shader.default_input["height"] = len(self.settings.biome_color_settings.biomes)
        self.shader.default_input["width"] = self.texture_resolution
    