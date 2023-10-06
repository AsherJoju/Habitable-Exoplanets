from scripts.noise_filter import NoiseFilter
from scripts.noise_filter_factory import NoiseFilterFactory
from scripts.shape_settings import ShapeSettings
from ursina import Vec3


class ShapeGenerator:
    
    def __init__(self, settings: ShapeSettings):
        self.settings = settings
        self.noise_filters: list[NoiseFilter] = []
        
        for i in range(len(self.settings.noise_layers)):
            self.noise_filters.append(
                NoiseFilterFactory.create_noise_filter(self.settings.noise_layers[i].settings)
            )
    
    
    def get_point_on_planet(self, point_on_unit_sphere: Vec3):
        elevation = 0
        first_layer_value = 0
        
        if len(self.settings.noise_layers) > 0:
            first_layer_value = self.noise_filters[0].evaluate(point_on_unit_sphere)
            if self.settings.noise_layers[0].enabled:
                elevation = first_layer_value
        
        for i in range(1, len(self.noise_filters)):
            if self.settings.noise_layers[i].enabled:
                mask = first_layer_value if self.settings.noise_layers[i].use_first_layer_as_mask else 1
                elevation += self.noise_filters[i].evaluate(point_on_unit_sphere) * mask
        
        return point_on_unit_sphere * self.settings.planet_radius * (elevation + 1)
