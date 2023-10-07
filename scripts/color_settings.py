from scripts.gradient import Gradient
from scripts.noise_settings import NoiseSettings
from ursina import Color


class ColorSettings:
    
    class BiomeColorSettings:
        
        class Biome:
            
            def __init__(self, gradient: Gradient, tint: Color, tint_percent: float, start_height: float):
                self.gradient = gradient
                self.tint = tint
                self.tint_percent = tint_percent
                self.start_height = start_height
            
        
        def __init__(
            self,
            biomes: list[Biome],
            noise: NoiseSettings,
            noise_offset: float, 
            noise_strength: float,
            blend: float
        ):
            self.biomes = biomes
            self.noise = noise
            self.noise_offset = noise_offset
            self.noise_strength = noise_strength
            self.blend = blend
        
    
    def __init__(self, biome_color_settings: BiomeColorSettings):
        self.biome_color_settings = biome_color_settings
