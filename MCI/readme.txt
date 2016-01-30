MCI Folder

This folder holds some of my attempts to create an MCI interpreter for ANet. 
For the most part it seems to work, except when using the Z command to change the background color. If it is used BEFORE a foreground (text) color change, it doesn’t go through as the C command to change the text color, overrides the ANSI escape for background color. 

If used AFTER the C command, it works fine. My thoughts were to use a global temp variable to store the command if it was used BEFORE the c command and then have it check for a value in the loop. If there was a Z command in the variable, add it to the beginning of the escape sequence in the right order. 

I just haven’t gotten to it yet.

-Rich
