from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

find_me_password_dictionary = [chr(num1) + chr(num2) for num1 in range(97, 123) for num2 in range(97, 123)]

for combo in find_me_password_dictionary:
	if unzip_with_7z(zip_file_path, dest_path, combo + "bcmpda") == True:
		break
