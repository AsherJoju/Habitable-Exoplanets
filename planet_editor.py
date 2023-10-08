from scripts.color_settings import ColorSettings
from scripts.gradient import Gradient
from scripts.noise_settings import NoiseSettings
from scripts.shape_settings import ShapeSettings
from scripts.planet import Planet
from ursina import color, EditorCamera, Ursina


RADIUS = 1
SEA_LEVEL = 1
SEA_COLOR = color.Color(0.25, 0.25, 1.0, 1.0)
FLORA_COLOR = color.Color(0.25, 0.75, 0.25, 1.0)


planet = Planet(
    25, # Resolution
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
                        layers=6,
                        strength=0.5,
                        persistence=0.5,
                        base_roughness=1,
                        roughness=1.5,
                        min_value=SEA_LEVEL
                    )
                )
            ),
            ShapeSettings.NoiseLayer(
                enabled=True,
                use_first_layer_as_mask=True,
                settings=NoiseSettings(
                    filter_type=NoiseSettings.FilterType.RIGID,
                    rigid_noise_settings=NoiseSettings.RigidNoiseSettings(
                        layers=3,
                        strength=2,
                        persistence=0.5,
                        base_roughness=2,
                        roughness=4,
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
                        (0, SEA_COLOR),
                        (0.05, color.Color(0.75, 0.75, 0, 1.0)),
                        (0.1, FLORA_COLOR),
                        (0.2, FLORA_COLOR * 0.75),
                        (0.4, FLORA_COLOR * 0.5),
                        (0.5, FLORA_COLOR * 0.25),
                        (0.7, color.Color(0.5, 0.5, 0.5, 1.0)),
                        (1, color.Color(1, 1, 1, 1))
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


app = Ursina()
editor_camera = EditorCamera()

planet.construct_planet()

app.run()
