import os
import argparse

def concatenate_files(source_repo, output_file):
    excluded_folders = {'Pods', 'Frameworks', '.bundle', 'libraries'}
    accept_folders = { 'fastlane' }

    with open(output_file, 'w') as output:
        for root, dirs, files in os.walk(source_repo, topdown=True):
             # Skip directories ending with .framework and specified excluded folders
            dirs[:] = [d for d in dirs if not d.endswith('.framework') and d not in excluded_folders]

            for file in files:
                if file.endswith('.swift') or file.endswith('.m') or file.endswith('.h') or file.endswith('.mm') or file.endswith('.c') or file.endswith('.cpp') or any(accept_folder in root for accept_folder in accept_folders):
                    # Skip files within excluded directories
                    if any(excluded_folder in root for excluded_folder in excluded_folders):
                        continue

                    source_file = os.path.join(root, file)
                    # Get the relative path of the file from the source_repo
                    relative_path = os.path.relpath(source_file, source_repo)
                    print(f"{relative_path}")

                    # Write the relative file path as header
                    output.write(f"---\nFile: {relative_path}\n---\n")

                    # Write contents of the file
                    with open(source_file, 'r') as f:
                        contents = f.read()
                        output.write(contents + "\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Concatenate the contents of .swift, .m, .h, .mm, .c, and .cpp files from a repository into a single text file with headers for each file’s relative path, excluding files in Pods and Frameworks directories.')
    parser.add_argument('source_repo', type=str, help='Path to the source repository')
    parser.add_argument('output_file', type=str, help='Path to the output text file')

    args = parser.parse_args()
    concatenate_files(args.source_repo, args.output_file)
