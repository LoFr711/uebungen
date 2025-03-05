from PIL import Image

def mandelbrot(c: complex, m: int) -> int:
    z = 0 + 0j  # Startwert ist 0
    for n in range(m):
        z = z**2 + c  # Richtige Iterationsformel
        if abs(z) > 2:  # Escape-Bedingung
            return n
    return m

def sample(z: complex, w: complex, x: int, y: int, sx: int, sy: int) -> complex:
    real = z.real + (w.real - z.real) * (x / (sx - 1))
    imag = z.imag + (w.imag - z.imag) * (y / (sy - 1))
    return complex(real, imag)

def color(i: int, max_i: int) -> tuple[int, int, int]:
    if i == max_i:
        return (0, 0, 0)  # Schwarz für Mandelbrot-Set
    hue = int(255 * (i / max_i) ** 0.5)  # Quadratische Farbskalierung für schöne Verläufe
    return (hue, 255, 255)

def render_mandelbrot(a: complex, b: complex, sx: int, sy: int, m: int, jpg_name: str):
    img = Image.new('HSV', (sx, sy))
    pixels = img.load()  # Schneller als putpixel()

    for x in range(sx):
        for y in range(sy):
            c = sample(a, b, x, y, sx, sy)
            colour = color(mandelbrot(c, m), m)
            pixels[x, y] = colour

    img.convert('RGB').save(jpg_name, quality=95)

render_mandelbrot(-2-1j, 1+1j, 900, 600, 50, "output.jpg")
