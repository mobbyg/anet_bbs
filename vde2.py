import curses

class TextEditor:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.current_row = 0
        self.current_col = 0
        self.content = [""]  # Initial content with an empty line

    def print_menu(self):
        # Clear the screen and display the menu options
        self.stdscr.clear()
        self.stdscr.addstr("Text Editor\n\n")
        self.stdscr.addstr("1. Open file\n")
        self.stdscr.addstr("2. Save file\n")
        self.stdscr.addstr("3. Edit file\n")
        self.stdscr.addstr("4. Print content\n")
        self.stdscr.addstr("5. Exit\n\n")
        self.stdscr.addstr("Select an option: ")
        self.stdscr.refresh()

    def open_file(self):
        # Clear the screen and prompt the user for the file path
        self.stdscr.clear()
        self.stdscr.addstr("Enter the path and filename: ")
        self.stdscr.refresh()
        path = self.stdscr.getstr().decode("utf-8")
        try:
            # Attempt to open the file and read its content
            with open(path, "r") as file:
                self.content = file.readlines()
            self.stdscr.addstr("\nFile opened successfully.\n")
        except FileNotFoundError:
            self.stdscr.addstr("\nFile not found.\n")
        self.stdscr.refresh()
        self.stdscr.getch()  # Wait for user input

    def save_file(self):
        # Clear the screen and prompt the user for the file path
        self.stdscr.clear()
        self.stdscr.addstr("Enter the path and filename to save: ")
        self.stdscr.refresh()
        path = self.stdscr.getstr().decode("utf-8")
        with open(path, "w") as file:
            # Write the content to the specified file
            file.writelines(self.content)
        self.stdscr.addstr("\nFile saved successfully.\n")
        self.stdscr.refresh()
        self.stdscr.getch()  # Wait for user input

    def print_content(self):
        # Clear the screen and display the content of the file
        self.stdscr.clear()
        self.stdscr.addstr("File Content:\n\n")
        for line in self.content:
            self.stdscr.addstr(line)
        self.stdscr.refresh()
        self.stdscr.getch()  # Wait for user input

    def edit_file(self):
        while True:
            # Wait for the user to press a key and get the key's integer value
            key = self.stdscr.getch()

            # Check if Enter key is pressed
            if key == curses.KEY_ENTER or key == 10:
                if self.current_col == len(self.content[self.current_row]) - 1:
                    # Handle new lines and line splitting
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
                if self.current_col
