# latest-episode-check-GogoAnime-

To use this program you can schedule the batch file in the task scheduler to run for some amount of time
or on linux you can use cronjobs to schedule the program to run periodically

to add to the database you need to enter the name of the anime and the link of the anime homepage from the gogoanime website 

ADD FUNCTIONALITY (change log):
Determine the awaiting ep and update it (use external file for this maybe?)
    --update (28/12/21):
        Used database using sqlite3 in python to maintain a database that keeps track of the latest episodes,
        name of anime and the url(GogAnime)
    --update(05/02/22):
	Made a command line based menu and a method to look at current shows in the database
        >todo:- maybe make a gui for the insertion of the information 

the batch file itself is 
<location of python.exe>
<location of python script>
pause #stops the cmd window from closing (Removed this because I wanted the process to disappear)
The batch shortcut makes it so that the batch file executes minimized (not working)
