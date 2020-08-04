#! /usr/bin/env python
import sys
import fileinput
import os

def check_char_min_len(pwd):
    return len(pwd) >= 8
  
def check_char_max_len(pwd):
    return len(pwd) <= 64
        
def check_is_ascii(pwd):
    return all(ord(char) < 128 for char in pwd)
       
def check_is_common_pwd(pwd, weak_pswd_list):
    return pwd in weak_pswd_list

def check_valid_cmdline_args():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Please provide 2 args')
        exit()
    elif not os.path.isfile(sys.argv[1]):
        print('Please provide a file as arg 2')
        exit()

def create_list_weak_pwds():
    weak_pswd_list = []
    weak_pwds_file = open(sys.argv[1], 'r')
    pwds = weak_pwds_file.readlines()

    for weak_pswd in pwds:
        weak_pswd_list.append(weak_pswd.rstrip())

    return weak_pswd_list

def check_each_pwd_meets_criteria(weak_pswd_list):
    for input_pswd in sys.stdin:
        input_pswd = input_pswd.rstrip()

        if not check_char_min_len(input_pswd):
            print(input_pswd + " -> Error: Too Short")
            continue
        elif not check_char_max_len(input_pswd):
            print(input_pswd + ' -> Error: Too Long')
            continue
        elif not check_is_ascii(input_pswd):
            print('*** -> Error: Invalid Characters')
            continue
        elif check_is_common_pwd(input_pswd, weak_pswd_list):
            print(input_pswd + ' -> Error: Too Common')

def main():
    check_valid_cmdline_args()
   
    weak_pswd_list = create_list_weak_pwds()

    check_each_pwd_meets_criteria(weak_pswd_list)


if __name__ == "__main__":
    main()











        

        

    
    

