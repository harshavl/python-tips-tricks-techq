
from __future__ import print_function
import argparse
import os,fnmatch

__authors__ = ["harsha"]
__date__ = 20102017
__description__ = "Directory tree walker"



def gen_find( file_pat, top ):
	for path, dirlist, filelist in os.walk(top):
	#	print( filelist)
		for name in fnmatch.filter(filelist,file_pat):
			yield os.path.join(path, name) 


def main():

	parser = argparse.ArgumentParser(description= __description__, epilog="Developed by %r on %r"%( __authors__, __date__ ) )

	parser.add_argument( "DIR_PATH", help="Path to Directory" )
	args = parser.parse_args()

	path_to_scan =args.DIR_PATH

	out = gen_find("test.py", path_to_scan )
	print(out)
	print(list(out))



if __name__ == "__main__":
	main()

