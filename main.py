from core.assistant import Assistant
from gui.main_gui import run_gui
from gui.tray_icon import create_icon
import threading

if __name__ == "__main__":
    # Inicializar el asistente
    assistant = Assistant()

    # Ejecutar el ícono en la bandeja en un hilo separado
    tray_thread = threading.Thread(target=create_icon, args=(assistant,))
    tray_thread.daemon = True  # Finaliza el hilo cuando el programa principal termine
    tray_thread.start()

    # Iniciar GUI principal
    run_gui(assistant)
