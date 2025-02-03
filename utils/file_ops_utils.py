class FileOps:
    def read_file(self, file):
        with open(file, 'r') as f:
            return f.read()

    def write_file(self, file, data):
        with open(file, 'w') as f:
            return f.write(data)