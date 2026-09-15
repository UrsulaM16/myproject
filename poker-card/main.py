# Here you have the suits symbols:
# ♣ ◆ ❤ ♠

# TODO

class InvalidCardError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Card:
    def __init__(self, value: int | str, suit: str):
        CARTAS: list[str] = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
        PALOS: dict[str, str] = {'♣':'Treboles','♦':'Diamantes','♥':'Corazones','♠':'Picas' }
        if isinstance(value,int) and value <=1 and value >= 13:
            raise InvalidCardError(f'{repr(self=value)} is not a supported value')
        if isinstance(value,str) and value not in CARTAS:
            raise InvalidCardError(f'{repr(self=value)} is not a supported symbol')
        if suit not in PALOS:
            raise InvalidCardError(f'{repr(self=suit)} is not a supported suit')
        # Crear atributos
        self.value: int | str = value
        self.suit: str = suit

def __repr__(self):
        # Lee el fichero data/glyphs.dat si existe
        try:
            with open('data/glyphs.dat', 'r', encoding='utf-8') as f:
                for line in f:
                    v, s, glyph = line.strip().split(',')
                    if str(self.value) == v and self.suit == s:
                        return glyph
        except FileNotFoundError:
            pass
        return f"{self.value}{self.suit}"

def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.value == other.value and self.suit == other.suit 

def _rank(self) -> int:
        return 14 if val == 1 else val

def __lt__(self, other: "Card") -> bool:
        return self._rank() < other._rank()

def __gt__(self, other: "Card") -> bool:
        return self._rank() > other._rank()

def __add__(self, other: "Card") -> "Card":
        # Determinar el nuevo palo (el de la carta mayor o el de self si son iguales)
        if other > self:
            new_suit = other.suit
        else:
            new_suit = self.suit




carta1 = Card(1, '♦')
print(repr(carta1))
carta2 = Card('A', '♦')
print(repr(carta2))