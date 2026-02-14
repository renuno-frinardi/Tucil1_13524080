class Matrix:
    # Method untuk inisiasi kelas
    def __init__(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()

        self.valid = False
        self.error_message = ""
        
        # Mengecek apakah file kosong
        if len(lines) == 0:
            self.error_message = "File kosong"
            self.row = 0
            self.col = 0
            self.matrix = []
            return
        
        # Menghilangkan bari kosong
        lines = [line for line in lines if line.strip()]
        
        if len(lines) == 0:
            self.error_message = "File tidak mengandung data matrix"
            self.row = 0
            self.col = 0
            self.matrix = []
            return
        
        self.row = len(lines)
        
        # Mengecek apakah ada nilai kosong pada matriks
        first_row_length = len(lines[0].strip())
        for _, line in enumerate(lines):
            if len(line.strip()) != first_row_length:
                self.error_message = "Matrix harus persegi"
                self.row = 0
                self.col = 0
                self.matrix = []
                return
        
        # Mengecek apakah matriks persegi
        if self.row != first_row_length:
            self.error_message = f"Matrix tidak persegi"
            self.row = 0
            self.col = 0
            self.matrix = []
            return
        
        self.col = self.row
        self.matrix = [['0' for _ in range(self.row)] for _ in range(self.row)]
        self.input(lines)
        self.valid = True
    
    # Menerima input
    def input(self, string_input):
        for i in range(self.row):
            line = list(string_input[i].strip())
            for j in range(self.col):
                if j < len(line):
                    self.matrix[i][j] = line[j]