from scripts.min_max import MinMax
from ursina import Shader


class HeightShader(Shader):
    
    def __init__(self, min_max: MinMax, texture: list, size: tuple[int, int]):
        self.default_input = {
            "min_max": min_max.tuple(),
            "texture": texture,
            "resolution": size[1]
        }
        
        self.vertex = """
        
        #version 140
        
        uniform mat4 p3d_ModelViewProjectionMatrix;
        
        in vec4 p3d_Vertex;
        in vec2 p3d_MultiTexCoord0;
        
        out float vertex_length;
        out vec2 uv;
        
        void main() {
            gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
            vertex_length = length(p3d_Vertex.xyz);
            uv = p3d_MultiTexCoord0;
        }
        
        """
        
        self.fragment = """
        
        #version 140
        
        uniform vec2 min_max;
        uniform vec3 texture[%i * %i];
        uniform int resolution;
        
        in float vertex_length;
        in vec2 uv;
        
        out vec4 frag_color;
        
        float inverseLerp(float a, float b, float x) {
            return (x - a) / (b - a);
        }
        
        void main() {
            int height = %i;
            
            vec2 index = vec2(inverseLerp(min_max.x, min_max.y, vertex_length), uv.x);
            vec4 color = vec4(texture[
                int(index.y * (height - 1)) * resolution + int(index.x * resolution)
            ], 1);
            
            frag_color = color;
        }
        
        """ % (*size, size[0])
        
        super().__init__(vertex=self.vertex, fragment=self.fragment, default_input=self.default_input)
