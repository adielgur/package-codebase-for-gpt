# package-codebase-for-gpt
A Python script for generating a single file representing an entire codebase for Custom GPTs


Usage:

`python <package script> <path-to-codebase> <output-file-path>`

E.g.
`python generate_node_package.py ./my-codebase ./codebase.txt`

When generating a new custom GPT make sure to include instructions on how to parse the attached document (knowledge base) and its name.

For instance-

When interpreting the 'codebase.txt' document,  
I recognize the structure --- File: <**filename**> --- as the header for each file within the codebase,  
followed by the contents of that file.  
This enables me to provide context-specific advice based on the specific files and code segments referenced in the document.  
This is the file list:   
<**output from running the python script**>