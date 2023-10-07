from scripts.color_settings import ColorSettings
from scripts.gradient import Gradient
from scripts.noise_settings import NoiseSettings
from scripts.shape_settings import ShapeSettings
from scripts.planet import Planet
from ursina import color, EditorCamera, Ursina

planet = Planet(
    15, # Resolution
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
                        strength=0.25,
                        persistence=0.75,
                        base_roughness=1,
                        roughness=1.5,
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
                        strength=4,
                        persistence=0.25,
                        base_roughness=1.5,
                        roughness=2.5,
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
                        (0.0, color.black),
                        (0.5, color.gray),
                        (1.0, color.white)
                    ]),
                    tint=color.red,
                    tint_percent=0.25,
                    start_height=0
                ),
                ColorSettings.BiomeColorSettings.Biome(
                    Gradient([
                        (0.0, color.black),
                        (0.5, color.gray),
                        (1.0, color.white)
                    ]),
                    tint=color.green,
                    tint_percent=0.25,
                    start_height=0.25
                ),
                ColorSettings.BiomeColorSettings.Biome(
                    Gradient([
                        (0.0, color.black),
                        (0.5, color.gray),
                        (1.0, color.white)
                    ]),
                    tint=color.blue,
                    tint_percent=0.25,
                    start_height=0.75
                )
            ]
        )
    )
)


app = Ursina()
editor_camera = EditorCamera()

planet.construct_planet()

app.run()
