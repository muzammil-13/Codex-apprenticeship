# Cheatsheet: Common Shell Commands

## * File and Directory management:

* ls : List directories
* cd [dir_name] : change dir
* pwd : print working dir
* mkdir [dir_name] : create a dir
* rmdir [dir_name] : remove a dir
* cp [source] [destination] : copy files/dir from source to destination
* mv [source] [destination] : move/rename file/dir
* rm [file_name] : remove files
* touch [file_name] : create empty file or update timestamp

## * File content management

* cat [file_name] : display file content
* more [file_name] : view file (more details)
* less [file_name] : view file (short details)

## * Permissions and Ownership

* chmod [permissions] [file_name] : change file permissions
  Eg.: chmod 755 script.sh : rwxr-xr-x
  chmod +x script.sh : Make executable
* chown [user]:[group] [file_name] : Change file owner/group

## * Package Management

* sudo apt update : Update pkg lists
* sudo apt install [pkg_name] : Install package

## * Process Managment

* kill [PID] : Terminate a process
* bg : Send process to background
* fg : Bring process to foreground

## * User managment

* whoami : Display current username
* sudo [cmd] : Execute cmd as superuser
* passwd [username] : Change user's password
