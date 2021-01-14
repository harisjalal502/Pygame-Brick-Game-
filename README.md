# Pygame-Brick-Game-
How to run Pygame Programs

Intro
Running Pygame programs is a little different under varying operating systems. See below for the specific instructions for your particular operating system.

Windows
While developing code, you will want to use a batch file to run your programs (rather than from IDLE directly; pygame and IDLE do not play nicely together).

To make your own, open any text editor (IDLE will do. You can also use Notepad found under Accessories. Do NOT use Word.). Enter the following two lines:

[your filename].py

pause


Then save the file as [your filename].bat. You will want to make sure you change the "file type" to All Files. This file should be in the same directory as your Python code.

To run the program, double-click the .bat file. It will pop up a black console window and then your pygame window should appear. When you close the pygame window, the console window will remain with the message "Hit any key to continue…". Do so to make it disappear.

The main reason for the batch file is so you can see any error messages that pop up when you run the program. Once you are confident that your program is correct, you can double-click on the Python file directly to run it.

Mac
1. Open a terminal. (Command+Space, then type terminal in the search box and press enter.)

2. Navigate to the folder where the Python program you want to run is located. By default IDLE saves in your Documents folder, so enter 'cd Documents' into the terminal to get there.

3. Type 'python2.7 [your filename].py' and press enter to run the program. Watch the terminal for any errors.


Ubuntu/Linux
1. Open a terminal. (Gnome: Applications->Accessories->Terminal. Unity (Ubuntu 11.04): Applications ->Type 'terminal' in the search box -> Double click on the terminal application icon.)

2. Navigate to the folder where the Python program you want to run is located. By default IDLE saves in your home folder, so if you use that you don't actually have to do anything.

3. Type 'python [program name].py' and press enter to run the program. Watch the terminal for any errors.