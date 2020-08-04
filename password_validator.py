#! /usr/bin/env python
import sys
import fileinput
import os

#checks 8 char min, 
def check_char_min_len(pwd):
    return len(pwd) >= 8

#checks 64 char max     
def check_char_max_len(pwd):
    return len(pwd) <= 64
        
#checks if ASCII char
def check_is_ascii(pwd):
    return all(ord(char) < 128 for char in pwd)
       
#checks for common pswd in weak_pwd list
def check_is_common_pwd(pwd, weak_pswd_list):
    return pwd in weak_pswd_list

def check_valid_cmdline_args():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Please provide 2 args')
        exit()
    elif not os.path.isfile(sys.argv[1]):
        print('Please provide a file as arg 2')
        exit()

def main():
    check_valid_cmdline_args()
   
    weak_pswd_list = []

    #create list of weak_passwords from file
    weak_pwds_file = open(sys.argv[1], 'r')
    pwds = weak_pwds_file.readlines()
    for weak_pswd in pwds:
        weak_pswd_list.append(weak_pswd.rstrip())


    #checks each password in input file against criteria 
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


if __name__ == "__main__":
    main()











        

        

    
    

