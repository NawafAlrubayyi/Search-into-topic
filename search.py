# def search_in_file(file_path, search_value):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         matching_lines = [line.rstrip('\n') for line in lines if search_value in line]
#         return matching_lines

# # Example usage
# search_value = '"Product":"Holmes HEPA Air Purifier"'
# matching_lines = search_in_file("output.txt", search_value)
# print(matching_lines)

import argparse

def search_in_file(file_path, search_value):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matching_lines = [line.rstrip('\n') for line in lines if search_value in line]
        return matching_lines

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for a value in a file.')
    parser.add_argument('file_path', help='Path to the file to be searched.')
    parser.add_argument('search_value', help='Value to search for in the file.')

    args = parser.parse_args()

    matching_lines = search_in_file(args.file_path, args.search_value)
    print(matching_lines)