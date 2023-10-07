from scripts.color_settings import ColorSettings
from scripts.gradient import Gradient
from scripts.noise_settings import NoiseSettings
from scripts.shape_settings import ShapeSettings
from scripts.planet import Planet
from ursina import color, EditorCamera, Ursina

planet = Planet(
    25, # Resolution
    Planet.FaceRenderMask.ALL,
    ShapeSettings(
        planet_radius=1.0,
        noise_layers=[
            ShapeSettings.NoiseLayer(
                enabled=True,
                use_first_layer_as_mask=False,
                settings=NoiseSettings(
                    filter_type=NoiseSettings.FilterType.SIMPLE,
                    simple_noise_settings=NoiseSettings.SimpleNoiseSettings(
                        layers=3,
                        strength=0.5,
                        persistence=0.5,
                        base_roughness=1,
                        roughness=2,
                        min_value=1
                    )
                )
            ),
            ShapeSettings.NoiseLayer(
                enabled=True,
                use_first_layer_as_mask=True,
                settings=NoiseSettings(
                    filter_type=NoiseSettings.FilterType.RIGID,
                    rigid_noise_settings=NoiseSettings.RigidNoiseSettings(
                        layers=6,
                        strength=3,
                        persistence=0.5,
                        base_roughness=2,
                        roughness=2,
                        min_value=1,
                        sharpness=2,
                        weight_scaler=1
                    )
                )
            )
        ]
    ),
    ColorSettings(
        ColorSettings.BiomeColorSettings(
            [
                ColorSettings.BiomeColorSettings.Biome(
                    Gradient([
                        (0, color.Color(0.5, 0.5, 1, 1)),
                        (0.1, color.Color(0.25, 0.25, 0.75, 1)),
                        (0.2, color.Color(0.25, 0.75, 0, 1)),
                        (0.55, color.Color(0.25, 1, 0.25, 1)),
                        (0.8, color.Color(0.75, 0.75, 0.75, 1)),
                        (0.8, color.Color(0.5, 0.5, 0.5, 1)),
                        (1, color.Color(1, 1, 1, 1))
                    ]),
                    tint=color.white,
                    tint_percent=0,
                    start_height=0.1
                )
            ],
            noise=NoiseSettings(
                filter_type=NoiseSettings.FilterType.SIMPLE,
                simple_noise_settings=NoiseSettings.SimpleNoiseSettings(
                    layers=3,
                    strength=1,
                    persistence=0.5,
                    base_roughness=1,
                    roughness=2,
                    min_value=0
                )
            ),
            noise_offset=0.75,
            noise_strength=0.25,
            blend=0
        )
    )
)


app = Ursina()
editor_camera = EditorCamera()

planet.construct_planet()

app.run()
