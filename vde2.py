import curses

class ConsoleTextEditor:
    def __init__(self):
        self.content = []
        self.current_row = 0
        self.current_col = 0

    def run(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

        try:
            while True:
                self.print_menu()
                choice = self.stdscr.getch()

                if choice == ord('1'):
                    self.new_file_and_edit()
                elif choice == ord('2'):
                    self.open_file()
                elif choice == ord('3'):
                    self.save_file()
                elif choice == ord('4'):
                    self.print_content()
                elif choice == ord('5'):
                    print("Exiting the text editor.")
                    break
                else:
                    self.stdscr.addstr("\nInvalid choice. Please try again.")
        finally:
            curses.endwin()

    def print_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr("\nConsole Text Editor Menu:\n")
        self.stdscr.addstr("1. New File and Edit\n")
        self.stdscr.addstr("2. Open File\n")
        self.stdscr.addstr("3. Save File\n")
        self.stdscr.addstr("4. Print Content\n")
        self.stdscr.addstr("5. Exit\n")
        self.stdscr.refresh()

    def new_file_and_edit(self):
        self.content = [""]
        self.current_row = 0
        self.current_col = 0
        self.stdscr.addstr("\nNew file created. Type your text.\n")
        self.edit_file()


    def edit_file(self):
        while True:
            key = self.stdscr.getch()

            if key == curses.KEY_ENTER or key == 10:
                self.content.insert(self.current_row + 1, self.content[self.current_row][self.current_col:])
                self.content[self.current_row] = self.content[self.current_row][:self.current_col] + "\n"
                self.current_row += 1
                self.current_col = 0
            elif key == curses.KEY_BACKSPACE or key == 127:
                if self.current_col > 0:
                    self.content[self.current_row] = self.content[self.current_row][:self.current_col - 1] + self.content[self.current_row][self.current_col:]
                    self.current_col -= 1
            elif key == curses.KEY_LEFT:
                if self.current_col > 0:
                    self.current_col -= 1
            elif key == curses.KEY_RIGHT:
                if self.current_col < len(self.content[self.current_row]) - 1:
                    self.current_col += 1
            elif key == curses.KEY_UP:
                if self.current_row > 0:
                    self.current_row -= 1
                    if self.current_col > len(self.content[self.current_row]) - 1:
                        self.current_col = len(self.content[self.current_row]) - 1
            elif key == curses.KEY_DOWN:
                if self.current_row < len(self.content) - 1:
                    self.current_row += 1
                    if self.current_col > len(self.content[self.current_row]) - 1:
                        self.current_col = len(self.content[self.current_row]) - 1
            elif key == 4:  # Ctrl+D
                break
            else:
                self.content[self.current_row] = self.content[self.current_row][:self.current_col] + chr(key) + self.content[self.current_row][self.current_col:]
                self.current_col += 1

            self.refresh_editor()

    def refresh_editor(self):
        self.stdscr.clear()
        self.stdscr.addstr("\nEditing file:\n")
        for i, line in enumerate(self.content):
            if i == self.current_row:
                self.stdscr.addstr(line[:self.current_col])
                self.stdscr.addstr(line[self.current_col:self.current_col + 1])
            else:
                self.stdscr.addstr(line)
        self.stdscr.refresh()

    def open_file(self):
        file_path = self.stdscr.getstr("\nEnter the file path to open: ").decode('utf-8')
        try:
            with open(file_path, "r") as file:
                self.content = file.readlines()
                print(f"File '{file_path}' opened.")
        except FileNotFoundError:
            print("File not found.")

    def save_file(self):
        file_path = self.stdscr.getstr("\nEnter the file path to save: ").decode('utf-8')
        with open(file_path, "w") as file:
            file.writelines(self.content)
            print(f"File '{file_path}' saved.")

    def print_content(self):
        print("\nFile Content:")
        for line in self.content:
            print(line, end="")

if __name__ == "__main__":
    editor = ConsoleTextEditor()
    editor.run()
