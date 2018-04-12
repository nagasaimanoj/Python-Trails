class Rectangle():
    def calculate_area(self, width, height):
        return width * height


if __name__ == "__main__":
    area = Rectangle().calculate_area(height=5, width=7)
    print(area)
