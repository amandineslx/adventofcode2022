INPUT_FILE = '07-input.txt'
MAX_SIZE = 100000
FILE_SYSTEM_SIZE = 70000000
FREE_SPACE_NEEDED = 30000000

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

    def get_size(self):
        size = 0
        for file in self.files.keys():
            size += self.get_file(file).size
        for folder in self.folders.keys():
            size += self.get_folder(folder).get_size()
        return size

    def get_subfolder_sizes(self, subfolder_sizes):
        current_folder_size = self.get_size()
        subfolder_sizes.append(current_folder_size)
        for folder in self.folders.keys():
            self.get_folder(folder).get_subfolder_sizes(subfolder_sizes)

    def to_string(self, indentation=0):
        result = ''
        if len(self.files.keys()) > 0:
            result += '\n' + get_indentation(indentation) + 'files: ' + ', '.join(self.files.keys())
        for folder_name in self.folders.keys():
            result += '\n' + get_indentation(indentation) + folder_name
            result += self.get_folder(folder_name).to_string(indentation+1)
        return result

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

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
            #print(f'{current.name} > {line}')
            if line.startswith('$'):
                if files:
                    #print('Add files')
                    current.add_files(files)
                    files = []
                if folder_names:
                    #print(f'Add folders to {current.name}')
                    current.add_folders(folder_names)
                    folder_names = []
            if line.startswith('$ cd /'):
                continue
            elif line.startswith('$ ls'):
                continue
            elif line.startswith('$ cd ..'):
                #print('back to parent')
                current = current.parent
            elif line.startswith('$ cd'):
                #print('going to folder')
                line_parts = line.split()
                current = current.get_folder(line_parts[2])
            elif line.startswith('dir '):
                line_parts = line.split()
                folder_names.append(line_parts[1])
            else:
                line_parts = line.split()
                files.append(File(line_parts[1], line_parts[0]))
        # take into account the last file and folders even if there is no command starting with $ after
        if files:
            current.add_files(files)
        if folder_names:
            current.add_folders(folder_names)
    return arborescence

def compute_small_folder_sizes(arborescence):
    subfolder_sizes = []
    arborescence.get_subfolder_sizes(subfolder_sizes)
    small_folder_sizes = [folder for folder in subfolder_sizes if folder < MAX_SIZE]
    return sum(small_folder_sizes)

def find_folder_to_free_space(arborescence):
    missing_free_space = FREE_SPACE_NEEDED - FILE_SYSTEM_SIZE + arborescence.get_size()
    print(missing_free_space)
    subfolder_sizes = []
    arborescence.get_subfolder_sizes(subfolder_sizes)
    print(subfolder_sizes)
    print(len(subfolder_sizes))
    small_folder_sizes = [folder for folder in subfolder_sizes if folder >= missing_free_space]
    print(small_folder_sizes)
    return min(small_folder_sizes)

arborescence = create_arborescence()
print(arborescence.to_string())
#print(compute_small_folder_sizes(arborescence))
print(find_folder_to_free_space(arborescence))
