# package-codebase-for-gpt
A collection of python scripts that iterate on a codebase and generate GPT ready text files for custom GPTs "knowledge base"

# Codebase Generation

Usage:
`python <package script> <path-to-codebase> <output-file-path>`

E.g.
`python generate_node_package.py ./my-codebase ../codebase.txt`

When generating a new custom GPT make sure to include instructions on how to parse the attached document (knowledge base) and its name.

For instance-

When interpreting the 'codebase.txt' document,  
I recognize the structure-
Codebase Structure: <**codebase directory and file tree**>
File: <**file path**> as the header for each file within the codebase, followed by the contents of that file.  
This enables me to provide context-specific advice based on the specific files and code segments referenced in the document.  
This is the file list:   
<**output from running the python script**>

# PR diff file
Usage:
`python <package script> <path-to-codebase> <target branch name> <feature-branch> <output-file-path>`

E.g.
`python generate_pr_diff_file.py ./my-codebase main feature-branch ../output.txt`

