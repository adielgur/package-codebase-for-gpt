import os
import argparse
import utils

def concatenate_files(source_repo, output_file):
    excluded_folders = {'node_modules', 'public', '.git'}
    excluded_files = {'package-lock.json'}  # Set of excluded files
    included_extensions = {'.js', '.ts', '.dockerfile', '.json'}  # Set of included files


    with open(output_file, 'w') as output:
        structure = utils.generate_file_structure(source_repo, excluded_folders, excluded_files, included_extensions)
        output.write(f"Codebase Structure:\n{structure}\n\n")

        for root, dirs, files in os.walk(source_repo, topdown=True):
             # Skip directories ending with .framework and specified excluded folders
            dirs[:] = [d for d in dirs if d not in excluded_folders]

            for file in files:
                if file in excluded_files:
                    continue

                if any(file.endswith(ext) for ext in included_extensions):
                    # Skip files within excluded directories
                    if any(excluded_folder in root for excluded_folder in excluded_folders):
                        continue

                    source_file = os.path.join(root, file)
                    # Get the relative path of the file from the source_repo
                    relative_path = os.path.relpath(source_file, source_repo)
                    print(f"{relative_path}")

                    # Write the relative file path as header
                    output.write(f"\nFile: {relative_path}\n\n")

                    # Write contents of the file
                    with open(source_file, 'r') as f:
                        contents = f.read()
                        output.write(contents + "\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Concatenate the contents of .json, .js, .ts files from a repository into a single text file with headers for each file’s relative path')
    parser.add_argument('source_repo', type=str, help='Path to the source repository')
    parser.add_argument('output_file', type=str, help='Path to the output text file')

    args = parser.parse_args()
    concatenate_files(args.source_repo, args.output_file)
