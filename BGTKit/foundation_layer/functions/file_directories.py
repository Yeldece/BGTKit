import os
import shutil
def directory_create(path):
	try:
		os.mkdir(path)
		return True
	except:
		return False
	def directory_delete(path):
	try:
		os.rmdir(path)
		return True
	except:
		return False
def directory_exists(path):
	return os.path.isdir(path)
def file_exists(path):
	return os.isfile(path)
def find_files(path):
	l=[]
	for each in os.listdirs(path):
		if os.path.isfile(each):
			l.append(each)
	return l
def find_directories(path):
	l=[]
	for each in os.listdirs(path):
		if os.path.isdir(each):
			l.append(each)
	return l
def file_copy(path,dest,overwrite=False):
	if overwrite==False and os.path.isfile(path):
		return False
	else:
	shutil.copy(path,dest)
		return True
def file_delete(path):
	if os.path.isfile(path):
		os.remove(path)
		return True
	else:
		return False
