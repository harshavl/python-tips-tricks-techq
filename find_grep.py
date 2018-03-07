

import fnmatch,os,re

def gen_find( pattern, top ):
	for path,dirlist, filelist in os.walk(top):
		for name in fnmatch.filter( filelist, pattern):
			yield os.path.join( path, name )




def gen_opener(filenames):
	for filename in filenames:
		
		if filename.endswith('.gz'):
			f = gzip.open(filename, 'rt')
		elif filename.endswith('.bz2'):
			f = bz2.open(filename, 'rt')
		else:
			f = open(filename, 'rt')
			yield f
		f.close()


def gen_cat( itera ):
	for it in itera:
		yield from it



def ge_grep( pattern, lines ):
	pat = re.compile( pattern )
	for line in lines:
		if pat.search(line):
			yield line



def main():
	log = gen_find( 'in.csv','/Users/admin/harsha/books' )
	print(list(log))
	files= gen_opener( log )
	print(list(files))



main()
	
		

