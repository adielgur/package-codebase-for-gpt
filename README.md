# package-codebase-for-gpt
A Python script for generating a single file representing an entire codebase for Custom GPTs


Usage-
python <package script>.py <path-to-codebase> <output-file-path>


When generating a new custom GPT make sure to include instructions on how to parse the attached document (knowledge base) and its name.

E.g.
When interpreting the 'codebase.txt' document, I recognize the structure --- File: <filename> --- as the header for each file within the codebase, followed by the contents of that file. This enables me to provide context-specific advice based on the specific files and code segments referenced in the document.
