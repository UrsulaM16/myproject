class SensorTemperatura:
    def __init__(
        self,
        ubicacion: str | None,
        lecturas_iniciales: list[str | int | float | None] | None,
    ) -> None:
        # 1. Validación defensiva de ubicación
        if isinstance(ubicacion, str) and ubicacion.strip():
            self._ubicacion: str = ubicacion.strip()
        else:
            self._ubicacion: str = "Desconocida"

        # 2. Inicialización defensiva de la lista privada
        self._lecturas: list[float] = []

        # 3. Filtrado y conversión de lecturas
        if lecturas_iniciales is not None:
            for item in lecturas_iniciales:
                # Descartar None y booleanos (True/False)
                if item is None or isinstance(item, bool):
                    continue

                if isinstance(item, (int, float)):
                    self._lecturas.append(float(item))
                elif isinstance(item, str):
                    texto_limpio = item.strip()
                    if texto_limpio:
                        try:
                            self._lecturas.append(float(texto_limpio))
                        except (ValueError, TypeError):
                            pass

    @property
    def ubicacion(self) -> str:
        """Getter para acceder a la ubicación."""
        return self._ubicacion

    @property
    def lecturas(self) -> list[float]:
        """Getter defensivo que devuelve una copia para proteger la mutabilidad."""
        return self._lecturas.copy()

    def promedio(self) -> float:
        """Calcula el promedio protegiendo contra división por cero."""
        if not self._lecturas:
            return 0.0

        return sum(self._lecturas) / len(self._lecturas)