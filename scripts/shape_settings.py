from scripts.noise_settings import NoiseSettings


class ShapeSettings:
    
    class NoiseLayer:
        
        def __init__(self, enabled: bool, use_first_layer_as_mask: bool, settings: NoiseSettings):
            self.enabled = enabled
            self.use_first_layer_as_mask = use_first_layer_as_mask
            self.settings = settings
    
    
    def __init__(self, planet_radius: float, noise_layers: list[NoiseLayer]):
        self.planet_radius = planet_radius
        self.noise_layers = noise_layers
    