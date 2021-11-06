from random import randint, sample
from string import ascii_letters, digits

test_link = ('http://', 'https://', 'ftp://')

def gen_keys():
	return (''.join(sample(ascii_letters+digits,randint(5,7))))


def testWeb(links):
	for i in test_link:
		if not links.startswith(i):
			continue
		return True  

def short_link(links):
		if testWeb(links):
			return(gen_keys())

