from tkinter import Tk, Label, Button
import threading

def run_gui(assistant):
    def toggle_active():
        assistant.active = not assistant.active
        status_label.config(text="Activo" if assistant.active else "Inactivo")

    def start_listening():
        if assistant.active:
            threading.Thread(target=assistant.process_command).start()

    root = Tk()
    root.title("Asistente de Voz")

    status_label = Label(root, text="Activo", font=("Arial", 16))
    status_label.pack(pady=10)

    toggle_button = Button(root, text="Activar/Inactivar", command=toggle_active)
    toggle_button.pack(pady=5)

    listen_button = Button(root, text="Escuchar", command=start_listening)
    listen_button.pack(pady=5)

    root.mainloop()
