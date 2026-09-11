class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        # Los atributos se inicializan dentro del constructor para cada instancia
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []         # Lista propia para cada teléfono
        self.status = False    # Estado inicial por defecto

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, *apps: str):
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)

    def uninstall_app(self, *apps: str):
        for app in apps:
            if app in self.apps:
                self.apps.remove(app) 