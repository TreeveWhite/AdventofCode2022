
class Dir:

    def __init__(self, name, parent=None) -> None:
        self.children = []
        self.parent = parent
        self.name = name
        self.size = 0

    def add_child(self, child_name):
        child = Dir(child_name, self)
        self.children.append(child)
    
    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
        self.add_child(child_name)
        return self.get_child(child_name)
    
    def add_file(self, file):
        self.children.append(file)
        self.size += file.size

    def __str__(self, level=0):
        ret = "  "*level+repr(self.name)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

class File:

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __str__(self, level=0) -> str:
        ret = "  "*level+repr(self.size)+" "+repr(self.name)+"\n"
        return ret


def run_command(cmd, dir : Dir, current_dir : Dir):
    cmd = cmd.split()
    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "/":
                current_dir = dir
            elif cmd[2] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child(cmd[2])
        if cmd[1] == "ls":
            pass
    elif cmd[0] == "dir":
        current_dir.add_child(cmd[1])
    else:
        new_file = File(cmd[1], int(cmd[0]))
        current_dir.add_file(new_file)
    
    return current_dir


def get_sizes(dir):
    sizes = []

    if isinstance(dir, File):
        return []

    sizes.append(dir.size)

    for child in dir.children:
        child_sizes = get_sizes(child)
        for size in child_sizes:
            sizes.append(size)
    
    return sizes


def task1(sizes):
    total = 0

    for size in sizes:
        if size <= 100000:
            total += size
    
    return total

def main():

    with open("data.txt", "r") as file:
        data = file.readlines()

    directory = Dir("/")
    current_dir = directory

    for line in data:
        current_dir = run_command(line, directory, current_dir)

    print(directory)

    print(task1(get_sizes(directory)))



    

if __name__ == "__main__":
    print(main())
