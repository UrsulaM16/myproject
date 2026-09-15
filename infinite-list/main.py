# creas la clase 
class InfiniteList:
    # Constructor def __init__
    # Recibe la instancia en self, todos los elementos posicionales iniciales agrupados en la tupla *args,
    # y un argumento nombrado fill_value cuyo valor por defecto es None
    def __init__(self, *args, fill_value=None):
        self.items = list(args)
        self.fill_value = fill_value

    def _expand(self, index: int):
        """Amplía la lista interna si el índice supera la longitud actual."""
        # Si fill_value es None, no expandir (lanzará error después)
        if self.fill_value is None:
            return
        
        if index >= len(self.items):
            # Añade fill_value hasta que la lista tenga tamaño index + 1
            padding_needed = index + 1 - len(self.items)
            self.items.extend([self.fill_value] * padding_needed)

    def __getitem__(self, index):
        # Manejar slices
        if isinstance(index, slice):
            # Expandir si es necesario para el slice
            start, stop, step = index.indices(len(self.items) + 1000)
            if stop > len(self.items):
                # Si fill_value es None, no expandimos
                if self.fill_value is not None:
                    self._expand(stop - 1)
            return self.items[index]
        
        # Manejar índices negativos
        if index < 0:
            # Convertir a índice positivo
            normalized = len(self.items) + index
            if normalized < 0:
                # Fuera de rango
                raise IndexError("list index out of range")
            return self.items[normalized]
        
        # Manejar índices positivos
        # Si fill_value es None y el índice está fuera de rango, lanzar error
        if self.fill_value is None and index >= len(self.items):
            raise IndexError("list index out of range")
        
        # Si fill_value existe, expandir
        self._expand(index)
        return self.items[index]

    def __setitem__(self, index, value):
        # Manejar slices
        if isinstance(index, slice):
            # Expandir si es necesario para el slice
            start, stop, step = index.indices(len(self.items))
            if stop > len(self.items):
                if self.fill_value is not None:
                    self._expand(stop - 1)
            self.items[index] = value
            return
        
        # Manejar índices negativos
        if index < 0:
            # Convertir a índice positivo
            normalized = len(self.items) + index
            if normalized < 0:
                # Fuera de rango
                raise IndexError("list assignment index out of range")
            self.items[normalized] = value
            return
        
        # Manejar índices positivos
        # Si fill_value es None y el índice está fuera de rango, lanzar error
        if self.fill_value is None and index >= len(self.items):
            raise IndexError("list assignment index out of range")
        
        # Si fill_value existe, expandir
        self._expand(index)
        self.items[index] = value

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        # Une los elementos convertidos a cadena mediante comas sin espacios
        return ','.join(str(item) for item in self.items)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(InfiniteList)