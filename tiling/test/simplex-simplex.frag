#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER



varying vec2 v_texcoord;


// 
// ================================
vec2 skew (vec2 st) {
    st *= 1.733;
    vec2 r = vec2(1.1547*st.x);
    r.y = st.y+0.5*r.x;
    return r;
}

vec3 simplexCoord (vec2 st, float td) {
    return 1.0-mix(vec3(st.x,1.0-vec2(st.x-st.y,st.y)),vec3(1.0-vec2(st.x,st.y-st.x),st.y),td);
}

vec3 simplexGrid (vec2 st) {
    vec3 xyz = vec3(0.0);
    
    vec2 p = fract(skew(st));
    if (p.x > p.y) {
        xyz.xy = 1.0-vec2(p.x,p.y-p.x);
        xyz.z = p.y;
    } else {
        xyz.yz = 1.0-vec2(p.x-p.y,p.y);
        xyz.x = p.x;
    }
    
    return fract(xyz);
}

vec3 simplexRotatedGrid (vec2 st) {
    vec3 xyz = vec3(0.0);
    
    vec2 p = fract(skew(st));
    if (p.x > p.y) {
        xyz.xy = 1.-vec2(p.x,p.y-p.x);
        xyz.z = p.y;
    } else {
        xyz.zx = 1.-vec2(p.x-p.y,p.y);
        xyz.y = p.x;
    }
    
    return fract(xyz);
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color.rgb += simplexGrid(v_texcoord.xy*5.);

    gl_FragColor = color;
}