# Kelas untuk menggambar solusi

from PIL import Image, ImageDraw

class Drawer:
    # Insiasi variable dan skema warna
    def __init__(self, algoritma):
        self.color_dict = {
                'A': '#FF5733', 'B': '#33FF57', 'C': '#3357FF', 'D': '#F333FF',
                'E': '#FF33A1', 'F': '#33FFF3', 'G': '#F3FF33', 'H': '#A133FF',
                'I': '#FF8C33', 'J': '#33FF8C', 'K': '#8C33FF', 'L': '#FF3333',
                'M': '#33FF33', 'N': '#3333FF', 'O': '#FFFF33', 'P': '#FF33FF',
                'Q': '#33FFFF', 'R': '#A52A2A', 'S': '#800080', 'T': '#008080',
                'U': '#FFD700', 'V': '#C0C0C0', 'W': '#808080', 'X': '#FFA500',
                'Y': '#000080', 'Z': '#FF1493'
            }
        self.height = algoritma.matrix.row * 8 + 1
        self.width = self.height
        self.solution = self.drawQueen(self.drawGrid(algoritma.matrix), algoritma.queen_positions)

    # Menggambar grid terlbih dahulu
    def drawGrid(self, matrix):
        image = Image.new("RGB", (self.height, self.width), "white")
        draw = ImageDraw.Draw(image)
        for i in range(matrix.row):
            for j in range(matrix.col):
                draw.rectangle([(j*8, i*8), (j*8+8, i*8+8)], fill=self.color_dict.get(matrix.matrix[i][j]), outline="black")
        return image

    # Menggambar ratu pada papan
    def drawQueen(self, image, position):
        draw = ImageDraw.Draw(image)
        for pos in position:
            draw.rectangle([(pos[1]*8+2, pos[0]*8+2), (pos[1]*8+2, pos[0]*8+5)], fill="black")
            draw.rectangle([(pos[1]*8+3, pos[0]*8+4), (pos[1]*8+5, pos[0]*8+6)], fill="black")
            draw.rectangle([(pos[1]*8+4, pos[0]*8+2), (pos[1]*8+4, pos[0]*8+3)], fill="black")
            draw.rectangle([(pos[1]*8+6, pos[0]*8+2), (pos[1]*8+6, pos[0]*8+5)], fill="black")
        upscaled_image = image.resize((250, 250), resample=Image.NEAREST)
        return upscaled_image