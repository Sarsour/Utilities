import os
import sys

path = 'C:\\Users\\Nidal\\Documents\\Resumes\\Portfolio\\Rosalind'
folders = os.listdir(path)

for folder in folders:
	if 'Rosalind - ' in folder:
		new_name = folder.replace('Rosalind - ', '')
		os.rename(os.path.join(path, folder), os.path.join(path, new_name))