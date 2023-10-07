from scripts.min_max import MinMax
from ursina import Shader


class HeightShader(Shader):
    
    def __init__(self, min_max: MinMax, biomes: list[float], texture: list, size: tuple[int, int]):
        self.default_input = {
            "min_max": min_max.tuple(),
            "biomes": biomes,
            "texture": texture,
            "height": size[0],
            "width": size[1]
        }
        
        self.vertex = """
        
        #version 140
        
        uniform mat4 p3d_ModelViewProjectionMatrix;
        
        in vec4 p3d_Vertex;
        
        out float distance;
        out float latitude;
        
        void main() {
            gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
            distance = length(p3d_Vertex.xyz);
            latitude = (p3d_Vertex.y + 1) / 2.0;
        }
        
        """
        
        self.fragment = """
        
        #version 140
        
        uniform vec2 min_max;
        uniform float biomes[%i];
        uniform vec3 texture[%i * %i];
        uniform int height;
        uniform int width;
        
        in float distance;
        in float latitude;
        
        out vec4 frag_color;
        
        void main() {
            float point = clamp((distance - min_max.x) / (min_max.y - min_max.x), 0.0, 1.0);
            
            int biome = 0;
            for (int i = 0; i < height; i++) {
                if (biomes[i] < latitude) {
                    biome = i;
                } else {
                    break;
                }
            }
            
            int index = int(biome * width + point * width);
            vec4 color = vec4(texture[index], 1);
            
            frag_color = color;
        }
        
        """ % (size[0], *size)
        
        super().__init__(vertex=self.vertex, fragment=self.fragment, default_input=self.default_input)
