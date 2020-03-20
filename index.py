import os
import sys

# Run using python3 index.py path [resultsToShow]
# Example python3 index.py /users/bobjones/Files 20
# Default resultsToShow=30

def calculate_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total = total + entry.stat().st_size
            elif entry.is_dir():
                total = total + calculate_directory_size(entry.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    except OSError:
        return 0
    return total

def sort_folders(folderDictionary):
    return sorted(folderDictionary.items(), key=lambda item: item[1], reverse=True)

def display_sorted_folders(sortedListOfTupples, resultsToShow):
    for key,value in enumerate(sortedListOfTupples):
        if(key<resultsToShow):
            print(value)

def main(basePath, resultsToShow):
    folderDict = {}
    for entry in os.scandir(basePath):
        if entry.is_dir() and entry.name != "Library":
            print(str(entry.name) + "...")
            # In gigabytes
            folderSize = round(calculate_directory_size(entry.path) / 1073741824, 2)
            folderDict[entry.name] = folderSize
            print(str(entry.name) + " -> Size = " + str(folderSize))

    sortedFolders = sort_folders(folderDict)

    display_sorted_folders(sortedFolders, resultsToShow)


basePath = sys.argv[1]
resultsToShow = sys.argv[2] if len(sys.argv) >= 3 else 30

main(basePath, resultsToShow)


