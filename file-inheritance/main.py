from importlib.resources import contents

#ejemplo de HERENCIA DE FICHEROSSSS OJOOOOOO O.O

# clase padre es FILE 
class File:                             
    def __init__(self, path: str):    # METODO CONTRUCTOR: se ejecuta inmediato
        self.path = path               # guarda la ruta del archivo
        self.contents = []   # inicia como lista vacía para almacenar

    def add_content(self, content: str):   #metodo para agregar cadena de texto a la lista
        self.contents.append(content)   #se anexa al final de la lisra 

    @property # decorador-> transforma el metodo en atributo 
    def size(self) -> int:
        return sum(len(item) for item in self.contents)   # mide la longitud del texto en self.contens y los suma todos para obtene el total de caracteres
                                                          # recuerda que puedes devolver con el formato que pide el enunciado. 
    @property
    def info(self) -> str:
        #Devuelve el formato base requerido: la ruta formateada junto con el tamaño devuelto por self.size.
        return f"{self.path} [size={self.size}B]" #tambien puede ser como lo definio el profesor, recuerda en el anterior 

#CLASES HIJA. Hereda del padre(File)
class MediaFile(File):
    #Llama al constructor de la clase padre (File). Esto inicializa path y crea la lista vacía contents
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path) #llama a metodos de la clase padre(file)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

##Llama a la propiedad info de File (que devuelve "/ruta [size=XB]"). A ese resultado le concatena las nuevas líneas con el códec, la geolocalización y la duración.
    @property
    def info(self) -> str:
        return (
            f"{super().info}\n" #recuerda /n salto de linea 
            f"Codec: {self.codec}\n"
            f"Geolocalization: {self.geoloc}\n"
            f"Duration: {self.duration}s"
        )

#CLASES HIJA(Hereda de MediaFile)
class VideoFile(MediaFile):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple):
        super().__init__(path, codec, geoloc, duration) # Recuerda que llama al metodo constructor del padre(recuerda es MediaFile)
        self.dimensions = dimensions #anexa al final, recuerda el enunciado 

    @property
    def info(self) -> str:
        return f"{super().info}\nDimensions: {self.dimensions}"  #Como queremos que se presente la info, lo que te falta 