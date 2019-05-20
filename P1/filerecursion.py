import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    matching_files = []
    for dir, _, files in os.walk(path):
        for f in files:
            if f.endswith(suffix):
                matching_files.append(os.path.join(dir, f))
    return matching_files

files = find_files('.c', '.')
print(files)
