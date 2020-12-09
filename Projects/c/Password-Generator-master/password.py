import secrets
import string
import datetime
import os
import sys, argparse

def return_password(length = 20, has_numbers = False, has_punctuation = False):
    letter_set = string.ascii_letters
    if has_numbers:
        letter_set += string.digits
    if has_punctuation:
        letter_set += string.punctuation
    return_str = ''
    for i in range(length):
        return_str += secrets.choice(letter_set)
    return return_str

def get_digit(prompt=''):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
            
def get_boolean(prompt=''):
    while True:
        b = input(prompt)
        if b.lower() == 'y':
            return True
        elif b.lower() == 'n':
            return False
        
def return_time():
    return datetime.datetime.now().strftime("%d %b %Y - %H:%M:%S")
        
def append_file(file_name= '', time='', description='', password=''):
    try:
       file = open(file_name, "a") 
    except FileNotFoundError:
        print("Error creating file")
        sys.exit(-1)
    file.write("\n{:s}\n".format(time))
    if len(description) > 0:
        file.write("{:s}: {:s}\n".format(description, password))
    else:
        file.write("{:s}\n".format(password))
    print("Password successfully saved at: {:s}\{:s}".format(os.getcwd(), file_name))
    file.close()
    
def input_parse():
    parser = argparse.ArgumentParser(description="A program for generating passwords")
    parser.add_argument("-f", "--filename", metavar="file_name", help="File will be saved as passwords.txt by default.") 
    parser.add_argument("-d", "--description", metavar="password_description", help="password_description: your password")
    parser.add_argument("-n", "--numbers", help="have numbers in your password", action="store_true")
    parser.add_argument("-p", "--punctuation", help="have punctuation in your password",action="store_true")
    parser.add_argument("password_length")
    return parser
    
def main(argv):
    file_name = "passwords.txt"
    password_description = "password"
    numbers = False
    punctuation = False
    password_length = 0
    parser = input_parse()
    args = parser.parse_args(argv)
    
    if args.filename:
        file_name = args.filename
    if args.description:
        password_description = args.description
    if args.numbers:
        numbers = True
    if args.punctuation:
        punctuation = True
    
    if args.password_length.isdigit():
        password_length = int(args.password_length)
    else:
        print("Invalid length input!")
        sys.exit(-1)
    
    time = return_time()
    password = return_password(password_length, numbers, punctuation)
    append_file(file_name, time, password_description, password)
    
if __name__ == "__main__":
    main(sys.argv[1:])
        
