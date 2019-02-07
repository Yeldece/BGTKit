import GuiLibrary,pygame
from accessible_output2.outputs import auto
pygame.init()
def alert(title,message):
	try:
		GuiLibrary.MessageBox(title,message)
			return True
	except:
		return False
def input_box(title,message):
	return GuiLibrary.InputBox(title,message)
def key_pressed(key_to_check):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key==key_to_check:
			return True
		else:
			return False
def key_down(key_to_check):
	if pygame.key.get_pressed()[key_to_check]:
		return True
	else:
		return False
