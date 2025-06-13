import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:\\Users\\M4zz\\PycharmProjects\\PythonProject2\\Example exercises\\dest\\compressed.zip",
                    "C:\\Users\\M4zz\\PycharmProjects\\PythonProject2\\Example exercises\\dest")