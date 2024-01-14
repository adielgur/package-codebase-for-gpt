import os
import argparse
import utils

def concatenate_files(source_repo, output_file):
    excluded_folders = {'node_modules', 'public'}
    excluded_files = {'package-lock.json'}  # Set of excluded files
    included_extensions = {'.js', '.ts', '.json', '.jsx', '.tsx'}  # Set of included files

    # Create the output directory if it doesn't exist
    output_folder = os.path.dirname(output_file)
    os.makedirs(output_folder, exist_ok=True)

    # Open the output file
    with open(output_file, 'w') as output:
        structure = utils.generate_file_structure(source_repo, excluded_folders, excluded_files, included_extensions)
        output.write(f"Codebase Structure:\n{structure}\n\n")
        
        for root, dirs, files in os.walk(source_repo, topdown=True):
            dirs[:] = [d for d in dirs if d not in excluded_folders]

            for file in files:
                if file in excluded_files:
                    continue

                if any(file.endswith(ext) for ext in included_extensions):
                    # Check if the file is in an excluded folder
                    if any(excluded_folder in root for excluded_folder in excluded_folders):
                        continue

                    source_file = os.path.join(root, file)
                    relative_path = os.path.relpath(source_file, source_repo)
                    print(f"{relative_path}")

                    output.write(f"File: {relative_path}\n\n")

                    with open(source_file, 'r') as f:
                        contents = f.read()
                        output.write(contents + "\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Concatenate .json, .js, .ts, .jsx, and .tsx files from a repository into a specified text file with headers for each file’s relative path.')
    parser.add_argument('source_repo', type=str, help='Path to the source repository')
    parser.add_argument('output_file', type=str, help='Full path to the output file including filename')

    args = parser.parse_args()
    concatenate_files(args.source_repo, args.output_file)
