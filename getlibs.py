import os

def find_lib_files(directory, output_file):
    # List to store .lib file paths
    lib_files = []

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.lib'):
                # Add full path of the .lib file to the list
                lib_files.append(os.path.join(root, file))
    
    # Write the list of .lib files to the output file
    with open(output_file, 'w') as f:
        for lib_file in lib_files:
            # Replace backslashes with forward slashes
            lib_file = lib_file.replace('\\', '/')
            f.write(lib_file + '\n')
    
    print(f"Found {len(lib_files)} .lib files. List saved to {output_file}")

# Example usage
directory_to_search = 'C:/vcpkg/installed/x64-windows/debug/lib'
output_txt_file = 'lib_files_list.txt'
find_lib_files(directory_to_search, output_txt_file)