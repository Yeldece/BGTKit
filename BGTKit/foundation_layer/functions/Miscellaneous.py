import pyperclip,sys,time,os,threading
from win32com.shell import shell
import pygame
pygame.init()
def clipboard_copy_text(text):
	try:
		pyperclip.copy(text)
	return True
	except:
		return False
def clipboard_read_text():
	return pyperclip.paste()
def exit():
	sys.exit()
def is_admin():
	return shell.IsUserAnAdmin()
def is_active():
	return pygame.display.get_active()
def show_game_window(title):
	try:
		size=[600,800]
		pygame.set_display_mode(size)
	pygame.display.set_caption(title)
		return True
	except:
		return False
def wait(miliseconds):
	try:
		time.sleep(miliseconds/1000)# this function needs time in seconds
		return True
	except:
		return False
def read_environment_variable(variable):
	return os.environ.get(variable)
def run(filename,command_line,wait_for_completion,background):
	