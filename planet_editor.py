from scripts.color_settings import ColorSettings
from scripts.gradient import Gradient
from scripts.noise_settings import NoiseSettings
from scripts.shape_settings import ShapeSettings
from scripts.planet import Planet
from ursina import color, EditorCamera, Ursina


# Real World Value
SUN_MASS = 1 # In solar masses effects temprature
PLANET_DISTANCE = 1 # in AUs (effect teprature)

SEA_LEVEL = 1 # Sea Level, (effects how much land is there) used in percent
RADIUS = 1 # Radius of the planet (scales it) in percent
WATER_AVAILABILITY = 0.75 # Efects strength of Flora Color in percent
TEMPRATURE = SUN_MASS * PLANET_DISTANCE * 10 # Effects Ration Of Plants over Rock and Snow

SEA_COLOR = color.Color(0.25, 0.25, 1.0, 1.0) # Sea / Water Color (based on Sun and Sky)
FLORA_COLOR = color.Color(0.25, 0.75, 0.25, 1.0) # Planet Color (effects Land Color)
ROCK_COLOR = color.Color(0.5, 0.5, 0.5, 1) # ROCK COLOR (effects moutains)


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
                        (5 / TEMPRATURE / 10, color.Color(0.75, 0.75, 0, 1.0)),
                        (1 / TEMPRATURE, FLORA_COLOR),
                        (2 / TEMPRATURE, FLORA_COLOR * WATER_AVAILABILITY * 0.75),
                        (4 / TEMPRATURE, FLORA_COLOR * WATER_AVAILABILITY * 0.5),
                        (5 / TEMPRATURE, FLORA_COLOR * WATER_AVAILABILITY * 0.25),
                        (7 / TEMPRATURE, ROCK_COLOR / TEMPRATURE * 10),
                        (1, color.Color(1, 1, 1, 1) / TEMPRATURE * 10)
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
