# Image gallery
A Qt-based gallery application for image slide shows.


# Features
## Choosing files and folders
Launching the application opens a file picker, where the user can choose individual files and/or folders to display in their slide show.

Default directory is the user's Pictures folder.

Note that double-clicking a folder moves into it. A folder can be chosen for a slide show by selecting to highlight it, and pressing **Open**. Folders are processed recursively.

*Currently supported file extensions are jpg, jpeg, png, gif, svg, and webp.*

## Controls
*All these defaults can be changed via config.ini.*

The slide show timer can be toggled on and off by pressing **P**.
The default state is off and the interval between images is 6 seconds.

Moving left and right between images is performed by pressing **J** and **K**, respectively.

Mouse controls include arrows on left and right edges on the window and a button row in the middle bottom area (the latter is disabled by default).

The file picker can be opened for a new slide show with **Ctrl+O**.

A slide show and the application can be closed by pressing **Ctrl+Q**.
