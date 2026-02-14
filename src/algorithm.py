import time

class Algorithm:
    def __init__(self, matrix, window=None):
        # Deklarasi variabel yang diperlukan
        self.matrix = matrix
        self.window = window
        self.queen_positions = []
        self.color_dict = {}
        self.color_list = []
        self.solved = False
        self.case = 0
        self.modulo = 1000

        # Kalkulasi print step
        if self.matrix.row < 8:
            self.modulo = 1000
        elif self.matrix.row >= 8 and self.matrix.row <= 10:
            self.modulo = 10000
        elif self.matrix.row >= 11 and self.matrix.row <= 13:
            self.modulo = 100000
        else:
            self.modulo = 1000000

        # Pemrosesan input
        self.saveColor()
        self.start = time.time()
        self.computeBruteForce()
        self.end = time.time()
        self.displayResult()
    
    # Menyimpan banyak warna pada papan
    def saveColor(self):
        for i in range(self.matrix.row):
            for j in range(self.matrix.col):
                color = self.matrix.matrix[i][j]
                if color not in ['\n', ' ']:
                    if color not in self.color_dict:
                        self.color_dict[color] = []
                    self.color_dict[color].append((i, j))
        self.color_list = list(self.color_dict.keys())

    # Fungsi inisasi bruteforce
    def computeBruteForce(self):
        tile_options = [self.color_dict[color] for color in self.color_list]
        self.generateCombinations(tile_options, [], 0)
    
    # Fungsi proses rekursif pada brute force
    def generateCombinations(self, tile_options, current_combination, color_index):
        # Basis apabila sudah berada di warna terakhir
        if color_index == len(tile_options):
            if self.isValid(current_combination):
                for i in range(len(current_combination)):
                    self.queen_positions.append(current_combination[i])
                self.solved = True
                return True 
            return False
        
        # Rekurens mengecek seluruh kombinasi warna
        for tile in tile_options[color_index]:
            self.case += 1
            current_combination.append(tile)
            # Melakukan penyimpanan kombinasi
            if self.case % 1000000 == 0:
                self.displayProgress(current_combination)
            if self.generateCombinations(tile_options, current_combination, color_index + 1):
                return True
            current_combination.pop() 
        return False
    
    # Mengecek apakah susunan ratu valid
    def isValid(self, positions):
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                if pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]) == 1:
                    return False
        return True

    # Menampilkan progress
    def displayProgress(self, positions=None):
        matrix = []
        if positions is not None:
            for row in range(self.matrix.row):
                row_now = []
                for col in range(self.matrix.col):
                    placed = False
                    for position in positions:
                        if row == position[0] and col == position[1]:
                            row_now.append('#')
                            placed = True
                            break
                    if not placed:
                        row_now.append(self.matrix.matrix[row][col])
                matrix.append(row_now)
            if self.window:
                self.window.initProg(matrix, self.matrix.row, self.matrix.col)
        else:
            for row in range(self.matrix.row):
                row_now = []
                for col in range(self.matrix.col):
                    placed = False
                    for position in self.queen_positions:
                        if row == position[0] and col == position[1]:
                            row_now.append('#')
                            placed = True
                            break
                    if not placed:
                        row_now.append(self.matrix.matrix[row][col])
                matrix.append(row_now)

    # Menampilkan hasil akhir
    def displayResult(self):
        if self.solved:
            self.displayProgress()
            self.window.initResult(self)
        else:
            self.window.initResult(self)