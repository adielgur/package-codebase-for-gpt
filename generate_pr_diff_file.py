import argparse
import subprocess
import os

def is_text_file(filename):
    # List of textual file extensions
    text_extensions = ['.txt', '.py', '.js', '.json', '.ts', '.jsx', '.tsx', '.cpp', '.h', '.hpp', '.swift']
    return any(filename.endswith(ext) for ext in text_extensions)

def get_changed_files(target_branch, source_branch):
    # Get a list of changed files between the target branch and the source branch
    changed_files = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=AM", f"{target_branch}...{source_branch}"]).decode().splitlines()
    # Filter out non-textual files
    return [f for f in changed_files if is_text_file(f)]

def get_file_diff(target_branch, source_branch, file):
    try:
        # Using git diff to get differences for each file
        diff = subprocess.check_output(
            ["git", "diff", f"{target_branch}...{source_branch}", "--", file]).decode()
        return diff
    except subprocess.CalledProcessError:
        return "Error getting diff."

def print_modified_files(file_list):
    print("Modified Files:")
    for file in file_list:
        print(file)
    print("\n")

def write_file_contents(file_list, target_branch, source_branch, output_file):
    with open(output_file, 'w') as output:
        for file in file_list:
            # Write file header
            relative_path = os.path.relpath(file)
            output.write(f"File: {relative_path}\n\n")

            # Write file diff
            file_diff = get_file_diff(target_branch, source_branch, file)
            output.write(file_diff + "\n")

def main():
    parser = argparse.ArgumentParser(description="Compare files in two Git branches.")
    parser.add_argument("codebase_path", help="Local path to the codebase")
    parser.add_argument("target_branch", help="The target branch (against which to compare)")
    parser.add_argument("source_branch", help="The source branch (with the new changes)")
    parser.add_argument("output_file", help="Output file to write the differences")

    args = parser.parse_args()

    # Change directory to the specified codebase path
    os.chdir(args.codebase_path)

    # Get list of changed files
    changed_files = get_changed_files(args.target_branch, args.source_branch)

    # Print modified files
    print_modified_files(changed_files)

    # Write file contents
    write_file_contents(changed_files, args.target_branch, args.source_branch, args.output_file)

if __name__ == "__main__":
    main()
