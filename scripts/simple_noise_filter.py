from opensimplex import OpenSimplex
from scripts.noise_filter import NoiseFilter
from scripts.noise_settings import NoiseSettings
from time import time_ns
from ursina import Vec3


SEED = time_ns()


class SimpleNoiseFilter(NoiseFilter):
    
    def __init__(self, settings: NoiseSettings.SimpleNoiseSettings):
        self.noise = OpenSimplex(SEED)
        self.settings = settings
    
    
    def evaluate(self, point: Vec3):
        noise_value = 0
        frequency = self.settings.base_roughness
        amplitude = 1
        
        for _ in range(self.settings.layers):
            p = Vec3(point * frequency + self.settings.center)
            v = self.noise.noise3(p.x, p.y, p.z)
            
            noise_value += (v + 1) * 0.5 * amplitude
            
            frequency *= self.settings.roughness
            amplitude *= self.settings.persistence
        
        noise_value = max(0, noise_value-self.settings.min_value)
        
        return noise_value * self.settings.strength
    