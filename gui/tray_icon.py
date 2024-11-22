from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

def create_icon(assistant):
    def toggle_active(icon, item):
        assistant.active = not assistant.active
        item.text = "Desactivar" if assistant.active else "Activar"

    # Crear un ícono simple
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 10, 54, 54), fill=(255, 0, 0))
    # image = Image.open("../src/chameleon.svg")

    # Menú contextual del ícono
    menu = Menu(
        MenuItem("Activar", toggle_active, checked=lambda item: assistant.active),
        MenuItem("Salir", lambda icon, item: icon.stop())
    )

    # Crear y ejecutar el ícono
    icon = Icon("Asistente de Voz", image, menu=menu)
    icon.run()
