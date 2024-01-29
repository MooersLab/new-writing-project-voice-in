#!/usr/bin/env python3
import sys

def writeCSV(ProjID,ProjDirectory):
    """This function writes out voice commands for the Voice In Plus software that incorporte 
    the project number and project name from the terminal.
    The project number is used in the voice command by the user to invoke an action that is 
    executed in terms of the insertion of text that has LaTeX code and the project name incorporated.
    The output file consists of a comma separated values file.
    """
    home = '/Users/blaine/6003TimeTracking/cb/'
    output1 = open(home + ProjID + '.csv', 'w')
    outp1 = 'project ' + ProjID + ',' + ProjDirectory + '\n'
    output1.write(outp1)

    outp2 = 'index ' + ProjID + ',\index{' + ProjDirectory + '!  }\n'
    output1.write(outp2)

    outp3 = 'to do ' + ProjID + ',***TODO [#A6] (2) ' + ProjDirectory + ':  }\n'
    output1.write(outp3)

    outp31 = 'section ' + ProjID + ',\section{' + ProjDirectory + ':  }\n'
    output1.write(outp31)

    outp4 = 'subsection ' + ProjID + ',\subsection{' + ProjDirectory + ':  }\n'
    output1.write(outp4)
    
    outp5   = 'subdex ' \
            + ProjID \
            + ',\subsection{' \
            + ProjDirectory \
            + ':  }' \
            + '\index{' \
            + ProjDirectory \
            + '!  }\n'
    output1.write(outp5)

    outp6 = 'sub sub section ' + ProjID + ',\subsubsection{' + ProjDirectory + ':  }\n'
    output1.write(outp6)

    outp6 = 'sub sub section ' + ProjID + ',\subsubsection{' + ProjDirectory + ':  }\n'
    output1.write(outp6)


    outp7 = 'double subdex '   + ProjID \
                               + ',\subsubsection{' \
                               + ProjDirectory \
                               + ':  }' \
                               + '\index{' \
                               + ProjDirectory \
                               + '!  }\n'
    output1.write(outp7)

    outp8 = 'caption ' + ProjID \
                       + ',\caption{' \
                       + ProjDirectory \
                       + ':  \label{' \
                       + ProjDirectory \
                       + '}}\n'
    output1.write(outp8)

    outp9 = 'label '   + ProjID \
                       + ',\label{' \
                       + ProjDirectory \
                       + '}\n'
    output1.write(outp9)

    outp10 = 'ref '    + ProjID \
                       + ',\\ref{' \
                       + ProjDirectory \
                       + '}\n'
    output1.write(outp10)

    outp11 = 'item '   + ProjID \
                       + ',\item ' \
                       + ProjDirectory \
                       + ': <capitalize> \n'
    output1.write(outp11)

    outp12 = 'description '   + ProjID \
                       + ',\item [  ] ' \
                       + ProjDirectory \
                       + ': <capitalize> \n'
    output1.write(outp12)

    outp13 = 'double sub decks '   + ProjID \
                               + ',\subsubsection{' \
                               + ProjDirectory \
                               + ':  }' \
                               + '\index{' \
                               + ProjDirectory \
                               + '!  }\n'
    output1.write(outp13)
    
    outp14 = 'overleaf ' + ProjID + ',<open: >\n'
    output1.write(outp14)
    
    outp14 = 'sheet ' + ProjID + ',<open: >\n'
    output1.write(outp14)
    
    print("Add to the open commmand for overleaf and sheets the urls for the project on overleaf and for its workbook sheet. In Voice In, say 'protocol for new writing project' to print the protocol.")
    
    print("""\subsection{Protocol for setting up a new writing project}
\begin{itemize}+ \n\
  \item Assign an index number to project in the project database.
  \item Create a directory for this project in the home directory.
  \item Create the project in Overleaf.
  \item Edit the associated main.tex file to include the correct title and paste in any text that has been generated already.
  \item Edit the associated writing log for the project by updating the title and adding a entry in the daily log and updating the word count.
  \item Make an entry for this project in the Google Sheets workbook.
  \item Run the new-writing-proj.py script to generate the LaTeX commands in a csv file from the project index number and directory name.
  \item Edit the csv file to include the urls for the Overleaf project and the Google Sheets project.
  \item Make voice commands for opening the Overleaf project, the Google sheet for the project, and the LaTeX commands that use the project number.
  \item Make a link to Overleaf project in the index.html file.
\end{itemize}""")

    output1.close()
    return


if __name__ == '__main__':
    ProjID = sys.argv[1]
    ProjDirectory = sys.argv[2]
    writeCSV(ProjID,ProjDirectory)