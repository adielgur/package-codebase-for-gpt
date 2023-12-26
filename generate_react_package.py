import os
import argparse

def concatenate_files(source_repo, output_folder):
    excluded_folders = {'node_modules', 'public'}
    excluded_files = {'package-lock.json'}  # Set of excluded files

    # Create the output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Paths for the two output files
    output_file_js = os.path.join(output_folder, 'codebase-js.ts.txt')
    output_file_tsx = os.path.join(output_folder, 'codebase-jsx.tsx.txt')


    # Open both files
    with open(output_file_js, 'w') as output_js, open(output_file_tsx, 'w') as output_tsx:
        for root, dirs, files in os.walk(source_repo, topdown=True):
            dirs[:] = [d for d in dirs if d not in excluded_folders]

            for file in files:
                if file in excluded_files:
                    continue

                if file.endswith(('.js', '.ts', '.json')):
                    output = output_js
                elif file.endswith(('.jsx', '.tsx')):
                    output = output_tsx
                else:
                    continue

                if any(excluded_folder in root for excluded_folder in excluded_folders):
                    continue

                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(source_file, source_repo)
                print(f"Processing: {relative_path}")

                output.write(f"---\nFile: {relative_path}\n---\n")

                with open(source_file, 'r') as f:
                    contents = f.read()
                    output.write(contents + "\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Concatenate .json, .js, .ts, .jsx and .tsx files from a repository into separate text files for .js/.ts/.json and .jsx/.tsx with headers for each file’s relative path.')
    parser.add_argument('source_repo', type=str, help='Path to the source repository')
    parser.add_argument('output_folder', type=str, help='Path to the output folder')

    args = parser.parse_args()
    concatenate_files(args.source_repo, args.output_folder)
