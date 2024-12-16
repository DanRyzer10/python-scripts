import os
import argparse

def count_elements_in_directory(directory_path):
    try:
        elements = os.listdir(directory_path)
        return len(elements)
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
        return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of elements in a directory.")
    parser.add_argument("directory", type=str, help="The path to the directory.")
    args = parser.parse_args()
    num_elements = count_elements_in_directory(args.directory)
    print(f"The directory '{args.directory}' contains {num_elements} elements.")
    # out = os.path.join(args.directory, "out")
    # if not  os.path.exists(out):
    #     os.makedirs(out)
    # for element  in os.listdir(args.directory):
    #     name,ext    = os.path.splitext(element)
    #     if len(name) == 2 and name.isupper():
    #         src_path = os.path.join(args.directory,element)
    #         dist = os.path.join(out,element)
    #         if os.path.isfile(src_path):
    #             os.rename(src_path,dist)
        

    # num_elements = count_elements_in_directory(args.directory)
    # print(f"The directory '{args.directory}' contains {num_elements} elements.")
    # out_directory = os.path.join(args.directory, "out")
    # if not os.path.exists(out_directory):
    #     os.makedirs(out_directory)

    # for element in os.listdir(args.directory):
    #     if len(element) == 2 and element.isupper():
    #         source_path = os.path.join(args.directory, element)
    #         destination_path = os.path.join(out_directory, element)
    #         if os.path.isfile(source_path):
    #             os.rename(source_path, destination_path)