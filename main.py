# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
 
# Função principal para modo de jogo dois jogadores
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        if is_board_full(board) or check_win(board, "X") or check_win(board, "O"):
            break
        row, col = map(int, input(f"Jogador {player}, digite a linha e coluna (separadas por espaço): ").split())
        if not is_valid_move(board, row, col):
            print("Movimento inválido. Tente novamente.")
            continue
        make_move(board, row, col, player)
        player = "O" if player == "X" else "X"

    print_board(board)
    if check_win(board, "X"):
        print("Jogador X venceu!")
    elif check_win(board, "O"):
        print("Jogador O venceu!")
    else:
        print("Empate!")        

# Função para verificar se um jogador venceu
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Função para verificar se o tabuleiro está cheio (empate)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Função para verificar se o movimento é válido
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

# Função para realizar um movimento
def make_move(board, row, col, player):
    board[row][col] = player

# Função principal
def main():
    play()

if __name__ == "__main__":
    main()
