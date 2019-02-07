import base64
from num2words import num2words
def ascii_to_character(code):
	return chr(code)
def character_to_ascii(char):
	return ord(char)
def hex_to_string(hex):
	return string.decode("hex")
def number_to_hex_string(number):
	hex(number)
def number_to_words(number):
	return num2words(number)
def string_base64_decode(string):
	string=string.encode()
	return base64.b64.decode(string).decode()
def string_base64_encode(string):
	string=string.encode()
	return base64.b64.encode(string).decode()
def string_contains(the_string,the_search):
	try:
		return the_string.index(the_search)
	except:
		return -1
def string_is_alphabetic(the_string):
	return the_string.isalpha()
def string_is_alphanumeric(the_string):
	return the_string.isalnum()
def string_is_digits(the_string):
	return the_string.isdigit()
def string_is_lower_case(the_string):
	return the_string.islower()
	def string_is_upper_case(the_string):
	return the_string.isupper()
def string_left(the_string, count):
	if count<=0:
		return ""
	elif count>len(the_string):
		return the_string
	else:
		return the_string[0:count]
def string_len(the_string):
	return len(the_string)
def string_mid(the_string,start_position,count):
	if count <1:
		return ""
	elif count>len(the_string):
		return the_string[start_position:]
	elif start_position<1:
		the_string=the_string[::-1]#string is reversed
		return the_string[start_position:count]
	elif start_position>len(the_string):
		return ""
	else:
		return the_string[start_position:count]
def string_replace(the_string, the_search,replacement,replace_all):
	if replace_all=False:
		return the_string.replace(the_search,replacement)
	else:
		return the_string.replace(the_search,replacement,1)
def string_reverse(the_string):
	return the_string[::-1]
def string_right(the_string,count):
	if count >len(the_string):
		return ""
	else:
		return the_string[count:]
def string_split(the_string,the_delimiter):
	return the_string.split(the_delimiter)
def string_to_hex(the_string):
	the_string=the_string.encode()
	return the_string.hex()
def string_to_lower_case(the_string):
	return the_string.lower()
def string_to_number(the_string):
	try:
		return int(the_string)
	except:
		return -1
def string_to_upper_case(the_string):
	return the_string.upper()
def string_trim_left(the_string,count):
	if count<1:
		return the_string
	elif count>len(the_string):
		return ""
	else:
		return the_string[count:len(the_string)]
def string_trim_right(the_string,count):
	if count<1:
		return the_string
	elif count>len(the_string):
		return ""
	else:
		return the_string[:len(the_string)-count]
