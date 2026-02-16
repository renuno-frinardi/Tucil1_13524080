# Kelas untuk membuat GUI dari program

import tkinter as Tk
from tkinter import filedialog as Fdg
from tkinter import messagebox as Msg
import matrix as Mat
import algorithm as Algo
import drawimg as Drw
import math as Math

class Window:
    def __init__(self, algorithm=None):
        # Setup initializer window
        self.root = Tk.Tk()
        self.algorithm = algorithm
        self.root.geometry("800x600")
        self.root.title("N-Queens Solver")
        self.root.configure(bg="#21222c")

        # Setup layout dasar aplikasi
        self.header = Tk.Frame(self.root, bg="#222222", height=50)
        self.content = Tk.Frame(self.root, bg="#21222c")
        self.footer = Tk.Frame(self.root, bg="#222222", height=50)

        self.header.pack(fill="both")
        self.content.pack(fill="both", expand=True)
        self.footer.pack(fill="both")

        # Setup header
        self.header_label = Tk.Label(self.header, text="N-Queens Solver", font=("Arial", 16, "bold"), bg="#222222", fg="#f8f8f2")
        self.header_label.pack(pady=10)

        # Setup footer
        self.footer_label = Tk.Label(self.footer, text="Tugas Kecil 1 IF2211 Strategi Algoritma", font=("Arial", 10), bg="#222222", fg="#f8f8f2")
        self.footer_label.pack(pady=10)

        # Setup Loop
        self.solution = None
        self.problem = None
        self.initHome()
        self.root.mainloop()

    # Fungsi inisiasi home page aplikasi
    def initHome(self):
        if self.solution:
            del self.solution
        if self.problem:
            del self.problem
        self.clearLayout()

        # Setup container
        main_content = Tk.Frame(self.content, bg="#21222c")
        main_content.pack(fill="both")
        main_content.place(relx=0.5, rely=0.5, anchor="center")

        # Setup gambar
        img = Tk.PhotoImage(file="src/assets/image.png")
        label_img = Tk.Label(main_content, image=img, bg="#21222c")
        label_img.image = img 
        label_img.pack(pady=(0, 30))

        # Setup text
        label1 = Tk.Label(main_content, text="Selamat datang di N-Queens Solver!", font=("Arial", 20, "bold"), bg="#21222c", fg="#8be9fd")
        label2 = Tk.Label(main_content, text="Pastikan input dalam bentuk file dengan matriks persegi", font=("Arial", 14), bg="#21222c", fg="#f8f8f2") 
        label1.pack()
        label2.pack(pady=(0, 20))

        # Setup button
        btn = Tk.Button(main_content, text="Start Solving", font=("Arial", 14), bg="#44475a", fg="#f8f8f2", command=self.fileTxt)
        btn.pack()

    # Fungsi inisiasi page progress
    def initProg(self, array_mat, row_i, col_i):
        self.clearLayout()
        grid_frame = Tk.Frame(self.content, bg="#21222c")
        grid_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Print matriks proses
        for r in range(row_i):
            for c in range(col_i):
                label = Tk.Label(grid_frame, text=array_mat[r][c], relief="solid", width=4, height=2, bg="#44475a", fg="#f8f8f2", font=("Courier", 10, "bold"))
                label.grid(row=r, column=c, padx=2, pady=2)
        
        self.root.update()

    # Fungsi inisiasi page hasil
    def initResult(self, algorithm):
        self.clearLayout()
        self.algorithm = algorithm

        main_content = Tk.Frame(self.content, bg="#21222c")
        main_content.pack(fill="both")
        main_content.place(relx=0.5, rely=0.5, anchor="center")
        
        # Kasus apabila tdk ditemukan solusi
        if not self.algorithm.solved:

            img = Tk.PhotoImage(file="src/assets/failed.png")
            label_img = Tk.Label(main_content, image=img, bg="#21222c")
            label_img.image = img 
            label_img.pack(pady=20)
                
            label = Tk.Label(main_content, text="Tidak ada solusi yang ditemukan.", font=("Arial", 16, "bold"), bg="#21222c", fg="#f8f8f2")
            label.pack(pady=20)

        # Kasus apabila ditemukan solusi
        else:
            image = Drw.Drawer(self.algorithm)
            
            image.solution.save("src/output/solution.png")
            img = Tk.PhotoImage(file="src/output/solution.png")

            label_img = Tk.Label(main_content, image=img, bg="#21222c")
            label_img.image = img 
            label_img.pack(pady=20)

            label1 = Tk.Label(main_content, text=f"Banyak kasus yang ditinjau: {self.algorithm.case}", font=("Arial", 14, "bold"), bg="#21222c", fg="#f8f8f2")
            label2 = Tk.Label(main_content, text=f"Waktu yang dibutuhkan: {Math.ceil((self.algorithm.end - self.algorithm.start) * 1000)} ms", font=("Arial", 14, "bold"), bg="#21222c", fg="#f8f8f2")
            label1.pack(pady=(0, 10))
            label2.pack(pady=(0, 20))

        btn = Tk.Button(main_content, text="Coba Lagi", font=("Arial", 14), bg="#44475a", fg="#f8f8f2", command=self.initHome)
        btn.pack()
    
    # Fungsi untuk dialog box file
    def fileTxt(self):
        self.my_txt = Fdg.askopenfilename(initialdir="", title="Pilih sebuah file txt", filetypes=[("Text files", "*.txt"), ("All files", "*")])
        if not self.my_txt:
            return
        
        self.problem = Mat.Matrix(self.my_txt)
        
        if not self.problem.valid:
            Msg.showerror("Validation Error", self.problem.error_message)
            return
        
        self.solution = Algo.Algorithm(self.problem, self)

    # Fungsi membersihkan bagian content pada aplikasi
    def clearLayout(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        