class House:

    def __init__(self, floors):

        if floors < 0:

            raise ValueError("Количество этажей не может быть отрицательным.")

        self.floors = floors

    def __eq__(self, other):

        return isinstance(other, House) and self.floors == other.floors

    def __lt__(self, other):

        return isinstance(other, House) and self.floors < other.floors

    def __le__(self, other):

        return isinstance(other, House) and self.floors <= other.floors

    def __gt__(self, other):

        return isinstance(other, House) and self.floors > other.floors

    def __ge__(self, other):

        return isinstance(other, House) and self.floors >= other.floors

    def __ne__(self, other):

        return not self.__eq__(other)

    def __add__(self, value):

        if isinstance(value, int):

            self.floors += value

            return self

        raise TypeError("value должно быть целым числом.")

    def __radd__(self, value):

        return self.__add__(value)

    def __iadd__(self, value):

        return self.__add__(value)