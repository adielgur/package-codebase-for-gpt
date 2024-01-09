import argparse
import subprocess
import os

def is_text_file(filename):
    # List of textual file extensions
    text_extensions = ['.txt', '.py', '.js', '.json', '.ts', '.jsx', '.tsx' '.cpp', '.h', '.hpp', '.swift']
    return any(filename.endswith(ext) for ext in text_extensions)

def get_changed_files(target_branch, source_branch):
    # Get a list of changed files between the target branch and the source branch
    changed_files = subprocess.check_output(
        ["git", "diff", "--name-only", f"{target_branch}...{source_branch}"]).decode().splitlines()
    # Filter out non-textual files
    return [f for f in changed_files if is_text_file(f)]

def get_file_content(branch, file):
    try:
        return subprocess.check_output(["git", "show", f"{branch}:{file}"]).decode()
    except subprocess.CalledProcessError:
        return None

def write_file_contents(file_list, target_branch, source_branch, output_file):
    with open(output_file, 'w') as output:
        for file in file_list:
            # Write file header
            relative_path = os.path.relpath(file)
            output.write(f"---\nFile: {relative_path}\n---\n")

            # Write 'before' content
            before_content = get_file_content(target_branch, file)
            output.write("### Before\n")
            if before_content is not None:
                output.write(before_content + "\n")
            else:
                output.write("FILE NOT PRESENT IN THIS BRANCH\n\n")

            # Write 'after' content
            after_content = get_file_content(source_branch, file)
            output.write("### After\n")
            if after_content is not None:
                output.write(after_content + "\n")
            else:
                output.write("FILE REMOVED FROM THIS BRANCH\n\n")

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

    # Write file contents
    write_file_contents(changed_files, args.target_branch, args.source_branch, args.output_file)

if __name__ == "__main__":
    main()
