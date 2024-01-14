import os

def generate_file_structure(root_dir, excluded_folders, excluded_files, included_extensions, indent=0):
    structure = ""
    for item in sorted(os.listdir(root_dir)):
        item_path = os.path.join(root_dir, item)

        # Skip excluded files
        if item in excluded_files:
            continue

        # Skip excluded folders (check if any part of the item's path is in excluded_folders)
        if any(excluded_folder in item_path.split(os.sep) for excluded_folder in excluded_folders):
            continue

        # Add indentation for better readability and list directories and files
        if os.path.isdir(item_path):
            structure += '    ' * indent + f"[Directory] {item}\n"
            structure += generate_file_structure(item_path, excluded_folders, excluded_files, included_extensions, indent + 1)
        elif any(item.endswith(ext) for ext in included_extensions):
            structure += '    ' * indent + f"{item}\n"

    return structure