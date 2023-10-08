from enum import Enum
from ursina import Vec3


class NoiseSettings:
    
    class FilterType(Enum):
        
        SIMPLE = 0
        RIGID = 1
    
    
    class SimpleNoiseSettings:
        
        def __init__(
            self,
            layers=1,
            strength=1.0,
            persistence=0.5,
            roughness=1.0,
            base_roughness=2.0,
            center=Vec3(0, 0, 0),
            min_value=1.0
        ):
            self.layers = layers
            self.strength = strength
            self.persistence = persistence
            self.base_roughness = base_roughness
            self.roughness = roughness
            self.center = center
            self.min_value = min_value
    
    
    class RigidNoiseSettings(SimpleNoiseSettings):
        
        def __init__(
            self, 
            sharpness=2.0,
            weight_scaler=0.75,
            **kwargs
        ):
            self.sharpness = sharpness
            self.weight_scaler = weight_scaler
            super().__init__(**kwargs)
    
    
    def __init__(
        self,
        filter_type: FilterType,
        simple_noise_settings=SimpleNoiseSettings(),
        rigid_noise_settings=RigidNoiseSettings()
    ):
        self.filter_type = filter_type
        self.simple_noise_settings = simple_noise_settings
        self.rigid_noise_settings = rigid_noise_settings
    