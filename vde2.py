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
            # Wait for the user to press a key and get the key's integer value
            key = self.stdscr.getch()

            # Check if Enter key is pressed
            if key == curses.KEY_ENTER or key == 10:
                # Handle new lines and line splitting
                if self.current_col == len(self.content[self.current_row]) - 1:
                    # Insert a new line at the cursor position
                    self.content.insert(self.current_row + 1, "\n")
                    self.current_row += 1
                    self.current_col = 0
                else:
                    # Split the current line at the cursor position
                    line = self.content[self.current_row]
                    new_line = line[self.current_col:]
                    self.content[self.current_row] = line[:self.current_col] + "\n"
                    self.content.insert(self.current_row + 1, new_line)
                    self.current_row += 1
                    self.current_col = 0
        
            # Check if Backspace key is pressed
            elif key == curses.KEY_BACKSPACE or key == 127:
                if self.current_col > 0:
                    # Delete the character before the cursor
                    self.content[self.current_row] = self.content[self.current_row][:self.current_col - 1] + self.content[self.current_row][self.current_col:]
                    self.current_col -= 1
        
            # Check if Left arrow key is pressed
            elif key == curses.KEY_LEFT:
                if self.current_col > 0:
                    # Move the cursor one position to the left
                    self.current_col -= 1
        
            # Check if Right arrow key is pressed
            elif key == curses.KEY_RIGHT:
                if self.current_col < len(self.content[self.current_row]) - 1:
                    # Move the cursor one position to the right
                    self.current_col += 1
        
            # Check if Up arrow key is pressed
            elif key == curses.KEY_UP:
                if self.current_row > 0:
                    # Move the cursor one row up and adjust column position
                    self.current_row -= 1
                    self.current_col = min(self.current_col, len(self.content[self.current_row]))
        
            # Check if Down arrow key is pressed
            elif key == curses.KEY_DOWN:
                if self.current_row < len(self.content) - 1:
                    # Move the cursor one row down and adjust column position
                    self.current_row += 1
                    self.current_col = min(self.current_col, len(self.content[self.current_row]))
        
            # Check if Ctrl+D is pressed (to exit editing)
            elif key == 4:  # Ctrl+D
                break
        
        # If none of the special keys, treat the key as a character and insert it
            else:
                if self.current_col == len(self.content[self.current_row]):
                    # Append the character at the end of the line
                    self.content[self.current_row] += chr(key)
                    self.current_col += 1
                else:
                    # Insert the character at the cursor position within the line
                    self.content[self.current_row] = self.content[self.current_row][:self.current_col] + chr(key) + self.content[self.current_row][self.current_col:]
                    self.current_col += 1
        
            # Refresh the editor display to show changes
            self.refresh_editor()

    def refresh_editor(self):
        self.stdscr.clear()
        self.stdscr.addstr("\nEditing file:\n")

        max_width = 80  # Maximum width of the editing area

        for i, line in enumerate(self.content):
            while len(line) > max_width:
                # Find the last space before the last word within the max_width
                last_space_index = line[:max_width].rfind(" ")
                if last_space_index == -1:
                    last_space_index = max_width - 1
                self.content.insert(i + 1, line[:last_space_index].rstrip())
                line = line[last_space_index + 1:]

            if i == self.current_row:
                visible_line = line[self.current_col:self.current_col + max_width]
                self.stdscr.addstr(visible_line)
            else:
                self.stdscr.addstr(line[:max_width])
            self.stdscr.addstr("\n")  # Add a newline after each line

        self.stdscr.refresh()

    def main(stdscr):
        editor = TextEditor(stdscr)
        editor.refresh_editor()
        editor.edit_file()

    curses.wrapper(main)


    def open_file(self):
        file_path = self.stdscr.getstr("\nEnter the file path to open: ").decode('utf-8')
        try:
            with open(file_path, "r") as file:
                self.content = file.readlines()
                print(f"File '{file_path}' opened.")
        except FileNotFoundError:
            print("File not found.")

    def save_file(self):
        self.stdscr.addstr("\nEnter the file path to save: ")
        self.stdscr.refresh()
        curses.echo()  # Enable echoing of input
        file_path = self.stdscr.getstr().decode('utf-8')
        curses.noecho()  # Disable echoing of input
        self.stdscr.clear()

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
