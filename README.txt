What Program Does
-----------------
1) Program checks for valid commandline inputs. 
-> Valid input is as follows: cat filename | ./password_validator.py filename 
-> If do not provide valid commandline args, will throw error and exit program 
-> If do not provide stdin, will hang (unsure how to fix)

2) Using the text file provided in commandline arg 2, program will create a list 
of all weak_passwords for instant searching later.

3) For each password in the text file provided by stdin, program will check if input 
password meets criteria by calling 4 functions. 
-> check_char_min_len - if the input password is 8 or more characters, returns true. Otherwise, returns false.
-> check_char_max_len - if input password is below 64 characters, return true. Otherwise, return false.
-> check_is_ascii - if input password is ascii returns true. Otherwise returns false.
-> check_is_common_pwd - if input password is found in weak_passwords list, returns true. Otherwise returns false.

4) If one of the 4 function conditions is false and does not meet the password criteria, program will print error, 
stop checking other criteria and proceed with checking next input password until end of file.


How to Use/Build Program locally
------------------
1) Download SRE_Takehome folder
2) Make sure have Python 3.x on system, if not please Download
3) On Windows, open Command prompt navigate inside SRE_Takehome and execute the following:
-> python password_validator.py weak_passwords_file < input_passwords_file

On linux/unix, open terminal and navigate inside SRE_Takehome and execute the following:
-> cat input_passwords_file | ./password_validator.py weak_passwords_file

4) Program will display passwords that DO NOT meet criteria above, will not display passwords that do meet criteria 

To run tests on Windows/Linux/Unix execute the following: python test.py