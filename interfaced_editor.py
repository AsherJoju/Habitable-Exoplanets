from ursina import Ursina, EditorCamera, color
from scripts.color_settings import ColorSettings
from scripts.gradient import Gradient
from scripts.noise_settings import NoiseSettings

from scripts.planet import Planet
from scripts.shape_settings import ShapeSettings


RADIUS = 1


app = Ursina()
editor_camera = EditorCamera()

planet = Planet(
    15, # Resolution
    Planet.FaceRenderMask.ALL,
    ShapeSettings(
        planet_radius=RADIUS,
        noise_layers=[
            ShapeSettings.NoiseLayer(
                enabled=True,
                use_first_layer_as_mask=False,
                settings=NoiseSettings(
                    filter_type=NoiseSettings.FilterType.SIMPLE,
                    simple_noise_settings=NoiseSettings.SimpleNoiseSettings(
                        layers=5,
                        strength=1,
                        persistence=0.5,
                        base_roughness=2,
                        roughness=1,
                        min_value=0
                    )
                )
            ),
            ShapeSettings.NoiseLayer(
                enabled=False,
                use_first_layer_as_mask=False,
                settings=NoiseSettings(
                    filter_type=NoiseSettings.FilterType.RIGID,
                    rigid_noise_settings=NoiseSettings.RigidNoiseSettings(
                        layers=5,
                        strength=1,
                        persistence=0.55,
                        base_roughness=2,
                        roughness=1,
                        min_value=0,
                        sharpness=2,
                        weight_scaler=1
                    )
                )
            )
        ]
    ),
    ColorSettings(
        ColorSettings.BiomeColorSettings(
            biomes=[
                ColorSettings.BiomeColorSettings.Biome(
                    Gradient([
                        (0, color.black),
                        (0.5, color.gray),
                        (1, color.white)
                    ]),
                    tint=color.white,
                    tint_percent=0,
                    start_height=0
                )
            ],
            noise=NoiseSettings(
                filter_type=NoiseSettings.FilterType.SIMPLE,
                simple_noise_settings=NoiseSettings.SimpleNoiseSettings()
            ),
            noise_offset=0,
            noise_strength=0,
            blend=0
        )
    )
)
planet.construct_planet()

app.run()
