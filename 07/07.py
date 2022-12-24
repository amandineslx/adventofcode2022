INPUT_FILE = '07-input.txt'

class Folder:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = {}
        self.files = {}

    def add_folder(self, folder_name):
        self.folders[folder_name] = Folder(self, folder_name)

    def add_folders(self, folders):
        for folder in folders:
            self.add_folder(folder)

    def add_file(self, file):
        self.files[file.name] = file

    def add_files(self, files):
        for file in files:
            self.add_file(file)

    def get_parent(self):
        return self.parent

    def get_folder(self, folder_name):
        return self.folders[folder_name]

    def get_file(self, file_name):
        return self.files[file_name]

    def to_string(self, indentation=0):
        result = ''
        if len(self.files.keys()) > 0:
            result += '\n' + get_indentation(indentation) + 'files: ' + ', '.join(self.files.keys())
        for folder_name in self.folders.keys():
            result += '\n' + get_indentation(indentation) + folder_name
            result += self.folders[folder_name].to_string(indentation+1)
        return result

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def get_indentation(indentation=0):
    if indentation == 0:
        return ''
    else:
        return ' ' * 2 * indentation

def create_arborescence():
    arborescence = Folder(None, '/')
    with open(INPUT_FILE) as f:
        current = arborescence
        files = []
        folder_names = []
        for line in f.readlines():
            print(f'{current.name} > {line}')
            if line.startswith('$'):
                if files:
                    print('Add files')
                    current.add_files(files)
                    files = []
                if folder_names:
                    print(f'Add folders to {current.name}')
                    current.add_folders(folder_names)
                    folder_names = []
            if line.startswith('$ cd /'):
                continue
            elif line.startswith('$ ls'):
                continue
            elif line.startswith('$ cd ..'):
                print('back to parent')
                current = current.parent
            elif line.startswith('$ cd'):
                print('going to folder')
                line_parts = line.split()
                current = current.get_folder(line_parts[2])
            elif line.startswith('dir '):
                line_parts = line.split()
                folder_names.append(line_parts[1])
            else:
                line_parts = line.split()
                files.append(File(line_parts[1], line_parts[0]))
    return arborescence

print(create_arborescence().to_string())
