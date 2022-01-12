class gameboard():
    def __init__(self, size):
        self.board = []
        self.size = size
        self.spaces_left = size*size
        self.status = ""
        self.condition = "incomplete"
        start_num = 1
        for i in range(size):
            row = []
            for j in range(size):
                row.append(start_num)
                start_num += 1
            self.board.append(row)
    def print_board(self):
        number_space = "  | "
        line_space = " -- +"
        current_number = 0
        print_start_line = "+"
        for x in range(self.size):
            print_start_line += line_space
        print(print_start_line)
        for i in range(self.size):
            current_row = self.board[i]
            print_number_row = "| "
            print_line_row = "+"
            
            for j in range(self.size):
                current_number += 1
                number = current_row[j]
                if len(str(number)) == 2:
                    number_space = " | "
                else:
                    number_space = "  | "
                print_number_row += str(number) + number_space
                print_line_row += line_space
                
            print(print_number_row)
            print(print_line_row)
    def find_placement(self, row_index, column_index):
        row = self.board[row_index]
        item = row[column_index]
        if type(item) == int:
            item = "#"
        return item
    def check_win(self, player):
        win = ""
        wins_dict = {}
        wins_dict["diagonal_top_left"] = ""
        wins_dict["diagonal_top_right"] = ""
        for i in range(self.size):
            win += player
            column_name = "column_" + str(i)
            wins_dict[column_name] = ""
            row_name = "row_" + str(i)
            wins_dict[row_name] = ""
            wins_dict["diagonal_top_left"] += self.find_placement(i,i)
            wins_dict["diagonal_top_right"] += self.find_placement(i,self.size-i-1)
            for j in range(self.size):
                wins_dict[column_name] += self.find_placement(j,i)
                wins_dict[row_name] += self.find_placement(i,j)
               
        for i in wins_dict.values():
            if i == win:
                self.status = player + " has won the game!"
                self.condition = "complete"
                break
            
    def check_full(self):
        if self.spaces_left == 0:
            self.condition = "complete"
            return True
        else:
            return False
    def get_condition(self):
        self.check_full()
        return self.condition
    def place_piece(self, player, position):
        row = 0
        column = 0
        for i in range(self.size):
            if position >= i*self.size + 1 and position <= i*self.size + self.size:
                row = i
                column = position - i*self.size - 1
                break
        item = self.find_placement(row, column)
        if item == "#" and position > 0 and position <= self.size * self.size:
            self.board[row][column] = player
            self.spaces_left -= 1
            self.status = "Great move " + player + " !"
            return True
        else:
            self.status = "Invalid selection, please try again"
            return False
    def print_status(self):
        print(self.status)
def main():
    game_size = int(input("Enter grid size: "))
    board = gameboard(game_size)
    print()
    board.print_board()
    print()
    player = "x"
    while board.get_condition() == "incomplete":
        selection = int(input("[PLAYER " + player + "] Enter your placement: "))
        choice = board.place_piece(player, selection)
        while choice == False:
            board.print_status()
            selection = int(input("[PLAYER " + player + "] Enter your placement: "))
            choice = board.place_piece(player, selection)
        print()
        board.check_win(player)
        board.print_status()
        print()
        board.print_board()
        print()
        if player == "x":
            player = "o"
        else:
            player = "x"
        

if __name__ == "__main__":
    main()