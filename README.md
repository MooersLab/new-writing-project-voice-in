# new-writing-project-voice-in: Generate Voice In commands for a new writing project

* Problem addressed
* 
We assigned a project number to every writing project.
This number is stored in a sqlite database along with the project's directory name.
This number begins the name of the project's folder in the home directory.
By entering the project number and hitting tab we can tab complete the project folder name and move to it.

We use both the project number and the project directory name in various LaTeX macro that are mapped to voice commands for use with the Voice In Plus plug-in for Google Chrome. 
The script above, `newproj.py`, generates these voice commands for a new project and writes them to a CSV file.
The contents of the CSV file can be copied and pasted in the window for the bulk add menu item In the Voice In Plus GUI.

The above script also print to the terminal a protocol as itemized list in LaTeX.
This serves as a reminder of the steps involved in setting up a new writing project.
The writing project resides in Overleaf where it has its own web page.
We map the \url{https://www.overleaf.com/project/659eaf3a5a122987aef346fb} for this web page to the Voice In command `overleaf <ProjID>` so that we can open the projects web page in Overleaf by using the voice command.
We likewise track the number of words written per day for a project and the time spent on the project in a Project Specific sheet inside of a Google Sheets workbook.
Each such project sheet has its own URL.
We map the voice command `sheet  <ProjID>` to this url.

The above script is set up for \LaTeX markup, but it could be easily converted for use with other markup languages such as Markdown, reStructuredText, org-mode, and HTML.
We intend to make such variants of the script when time permits.
