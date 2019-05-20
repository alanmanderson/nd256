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
    if path.startswith(os.sep):
        full_path = path
    else:
        full_path = os.path.realpath(path)
    queue = [os.path.realpath(queue[i]) for i in os.listdir(path)]
    print(queue)
    while len(queue) > 0:
        print(queue)
        next_file = queue.pop()
        full_path = os.path.realpath(next_file)
        if os.path.isfile(full_path):
            if next_file.endswith('.c'):
                matching_files.append(full_path)
        else:
            queue += os.listdir(full_path)
    return matching_files

files = find_files('.c', '.')
print(files)
