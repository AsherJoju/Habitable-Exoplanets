from scripts.color_settings import ColorSettings
from scripts.noise_settings import NoiseSettings
from scripts.shape_settings import ShapeSettings
from scripts.planet import Planet
from ursina import color, EditorCamera, Ursina


app = Ursina()
editor_camera = EditorCamera()

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
                        strength=0.25,
                        persistence=0.5,
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
                        persistence=0.5,
                        base_roughness=1.5,
                        roughness=2,
                        min_value=1,
                        sharpness=2,
                        weight_scaler=0.75
                    )
                )
            ),
        ]
    ),
    ColorSettings(
        planet_color=color.white
    )
)
planet.construct_planet()

app.run()
