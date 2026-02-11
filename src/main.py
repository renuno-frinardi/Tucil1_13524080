# Main Program Entry Point

class Inputter:
    def __init__(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()

        self.row = len(lines)
        self.col = self.row
        self.matrix = [['0' for _ in range(len(lines))] for _ in range(len(lines))]
        self.input(lines)
    
    def input(self, string_input):
        for i in range(self.row):
            line = string_input[i].strip().split()
            for j in range(self.col):
                self.matrix[i][j] = line[j] 
        
    def display(self):
        for row in self.matrix:
            print(' '.join(row))

if __name__ == "__main__":
    filename = input("Masukkan lokasi file: ")
    matrix = Inputter(filename)
    matrix.display()