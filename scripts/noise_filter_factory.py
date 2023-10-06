from scripts.noise_filter import NoiseFilter
from scripts.noise_settings import NoiseSettings
from scripts.rigid_noise_filter import RigidNoiseFilter
from scripts.simple_noise_filter import SimpleNoiseFilter


class NoiseFilterFactory:
    
    @staticmethod
    def create_noise_filter(settings: NoiseSettings) -> NoiseFilter:
        match settings.filter_type:
            case NoiseSettings.FilterType.SIMPLE:
                return SimpleNoiseFilter(settings.simple_noise_settings)
            case NoiseSettings.FilterType.RIGID:
                return RigidNoiseFilter(settings.rigid_noise_settings)
    