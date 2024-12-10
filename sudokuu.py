# Menampilkan grid Sudoku
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Mengecek apakah angka valid untuk dimasukkan pada posisi (row, col)
def is_valid(board, row, col, num):
    # Mengecek baris
    if num in board[row]:
        return False

    # Mengecek kolom
    for i in range(9):
        if board[i][col] == num:
            return False

    # Mengecek kotak 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Meminta input angka dari pemain
def get_input(board):
    while True:
        try:
            row = int(input("Masukkan baris (1-9): ")) - 1
            col = int(input("Masukkan kolom (1-9): ")) - 1
            num = int(input("Masukkan angka (1-9): "))
            
            # Memeriksa apakah input berada dalam rentang yang valid
            if row < 0 or row >= 9 or col < 0 or col >= 9:
                print("Baris dan kolom harus antara 1 dan 9.")
                continue
            if num < 1 or num > 9:
                print("Angka yang dimasukkan harus antara 1 dan 9.")
                continue
            if board[row][col] != 0:
                print("Sel ini sudah terisi, pilih sel kosong.")
                continue
            if not is_valid(board, row, col, num):
                print("Angka tersebut tidak valid, coba lagi.")
                continue
            
            # Jika valid, masukkan angka ke papan
            board[row][col] = num
            break
        except ValueError:
            print("Input tidak valid, coba lagi.")

# Fungsi untuk menyelesaikan Sudoku menggunakan backtracking
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Mencari sel kosong
                for num in range(1, 10):  # Coba angka 1 sampai 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Masukkan angka
                        if solve(board):  # Rekursi untuk melanjutkan ke sel berikutnya
                            return True
                        board[row][col] = 0  # Kembali ke keadaan semula (backtrack)
                return False  # Jika tidak ada angka yang valid
    return True  # Semua sel terisi dengan benar

# Menampilkan papan dan meminta input hingga selesai
def play_sudoku(board):
    while True:
        print("\nPapan Sudoku Saat Ini:")
        print_board(board)
        
        # Mengecek apakah Sudoku selesai
        if all(board[row][col] != 0 for row in range(9) for col in range(9)):
            print("\nSudoku selesai!")
            break
        
        # Meminta input dari pemain
        get_input(board)

# Contoh board Sudoku (0 berarti kosong)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Mulai permainan
play_sudoku(board)
