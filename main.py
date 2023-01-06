from view.ventana_principal import App
from controller.sesion import iniciar_sesion

print(iniciar_sesion("lucas", "1234"))

if __name__ == "__main__":
    app = App()
    app.mainloop()
