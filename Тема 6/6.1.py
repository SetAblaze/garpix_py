class Parallelepiped:
    def __init__(self, base_width, base_height, height):
        self._base_width = base_width
        self._base_height = base_height
        self._height = height

    def get_base_area(self):
        return self._base_width * self._base_height

    def get_volume(self):
        return self.get_base_area() * self._height

    def get_side_area(self):
        return 2 * self._height * (self._base_width + self._base_height)

    @staticmethod
    def get_info():
        print(Parallelepiped.__dict__)

parall = Parallelepiped(3, 4, 5)

Parallelepiped.get_info()

print('Площадь боковой поверхности параллелепипеда: ', parall.get_side_area())
print('Объем параллелепипеда: ', parall.get_volume())
print('Площадь основания параллелепипеда: ', parall.get_base_area())
