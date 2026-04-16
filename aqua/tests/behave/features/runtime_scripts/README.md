# AquaDrop Runtime Scripts Folder

Place all the aquadrop scripts into this folder. All the contents of this folder are automatically being copied to AquaDrop agents at run time.

Notes:

* Copies all contents of \runtime_scripts folder (files & folders)
* The copying is one-way: from AQUA to AquaDrop Agents
* Copying is occurring at script run-time.
* The files are copied only to agents that are activelly participating in a test
* The copying is occurring just-in time (just before a specfic agent step is invoked)
