![Version](https://img.shields.io/static/v1?label=new-writing-project-voice-in&message=0.1&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# new-writing-project-voice-in: Generate Voice In commands for a new writing project

## Problem addressed

We assigned a project number to every writing project.
This number is stored in a sqlite database along with the project's directory name.
This number begins the name of the project's folder in the home directory.
By entering the project number and hitting tab we can tab complete the project folder name and move to it.
We use both the project number and the project directory name in various LaTeX macros that are mapped to voice commands for use with the Voice In Plus plug-in for Google Chrome.

We wrote another script for the reading of the database and writing out the Voice In commands for all the existing projects.
However, we needed something simpler when adding a new project.
The script above, `newproj.py`, generates these voice commands for a new project and writes them to a CSV file.
The contents of the CSV file can be copied and pasted in the window for the bulk add menu item In the Voice In Plus GUI.

The above script also prints to the terminal a protocol for setting up a new writing project as itemized list in LaTeX.
This serves as a reminder of the steps involved in setting up a new writing project.
The writing project resides in Overleaf where it has its own web page.
We map the URL for this web page to the Voice In command `overleaf <ProjID>` so that we can open the projects web page in Overleaf by using the voice command.
We likewise track the number of words written per day for a project and the time spent on the project in a Project Specific sheet inside of a Google Sheets workbook.
Each such project sheet has its own URL.
We map the voice command `sheet  <ProjID>` to this URL so that we can quickly pop open the corresponding project sheet for the entry of the day's writing progress on that particular project.

The above script is set up for LaTeX markup, but it could be easily converted for use with other markup languages such as Markdown, reStructuredText, org-mode, and HTML.
We intend to make such variants of the script when time permits.
