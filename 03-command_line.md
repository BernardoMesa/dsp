# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > CHEAT SHEET
* pwd
* mkdir directoryName
* rm -r directoryName
* touch filename.et\xt
* rm filename.ext
* mv originFile.ext destinationFile.ext
* ls -a
* cp originFile.ext directoryPath/destinationFile.ext
* display contents of a file
    * cat filename.ext
* redirect output of command to file
    * cat originFile.ext > destinationFile.ext
* redirect output (append) of command to file
    * cat originFile.ext >> destinationFile.ext
* sort file lines
    * sort fileName.ext
* redirects output of command to input of another command
    * cat fileName.ext | sort > sorted-fileName.ext
* deletes adjacent repeated lines
    * unique fileName.ext
* find and replace first instance
    * sed 's/findString/replaceString/' fileName.txt
    * find and replace all instances in a line
        * sed 's/findString/replaceString/g' fileName.txt
    
---

### Q2.  List Files in Unix   

What do the following commands do:  

`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
* list contents of directory
* include hidden directories
* use long format/permissions
* include long format and readable file size
* include hidden directories, use long format and readable file size
* list contents sorted by time and date
* lists long format (suppreses owner) and adds a '/' at the end of directories

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
-m | displays names as comma separated list
-- | --
-r | displays files in reverse order
-- | --

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

