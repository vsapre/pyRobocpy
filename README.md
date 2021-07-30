# pyRobocpy
Script to make automated backups of Chosen folders.  
Robocopy is a Microsoft Windows Command which can be used to copy file/s over from one location to other. 
It includes many powerful options to control the copying process and allows multi-threaded copying.

This python script invokes robocopy to copy files from one location to another, with appropriate source and desitnation options and other copying options.
Each copy activity is considered a task and bunch of tasks can be specified using YAML format. 
The script looks for 'cpycfg.yaml' file located in the working directory, containing all copy tasks.
The typical format (YAML) for copy tasks is as follows:

```YAML
- backup:
    
    source: F:\test_dir\
    
    destin: H:\test_dir\
    
    fTypes: [rar]
    
    ropts : /MIR
    
- backup:
    
    source: F:\test_dir\
    
    destin: H:\test_dir\
    
    fTypes: [*]
    
    ropts : /MIR
```
Each copy task is delimited with the "- backup" specifier. Since it is preceded by a dash "-", it makes for a YAML list and hence the tasks are executed
in the sequence they are written down. This allows the script to make sequenced copies where users can prioritize some copy task over others.
The "fTypes" option can be further customized in the script to contain specific file name extensions. As of now its simply passed to Robocopy as it is.
"rOpts" are run time options that are passed to Robocopy verbatim. Please see Robocopy documentation for more details.

The user account running the script must have read/write priviledges for the source and destination folders to execute copy tasks.

Usecases:

1. Backup of multiple folders across machines or drives. Very useful for taking scheduled backups of data across machines.
2. Sequencing of copy tasks, based on priority or importance of data.
