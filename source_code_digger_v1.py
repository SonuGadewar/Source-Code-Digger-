import urllib2
from bs4 import BeautifulSoup
import time

def my_banner():
	print"\n*****************************************************************************************************************" 
	print '''
	  _____                                               _                _____ _       _     
	 |  __ \                                             (_)              / ____| |     | |    
	 | |__) | __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___  _ _ __   __ _  | |    | |_   _| |__  
	 |  ___/ '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` | | |    | | | | | '_ \ 
	 | |   | | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| | | |____| | |_| | |_) |
	 |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |  \_____|_|\__,_|_.__/ 
					   __/ |                                       __/ |                       
					  |___/                                       |___/                        
	
	''' 
	print"\n*****************************************************************************************************************"   
	print "\n                        Source-Code-Digger V1 : Sonu Gadewar"
	print"\n*****************************************************************************************************************" 
	

def full_source_code():
	print "\n++++++++++++++++++++++++++++++++++++++++++~Full Source Code~+++++++++++++++++++++++++++++++++++++++++++\n"
	print (soup1.prettify().encode("utf-8"))
	print "\n++++++++++++++++++++++++++++++++++++++++++~Full Source Code End~+++++++++++++++++++++++++++++++++++++++\n"
	time.sleep(2)
			

def all_link():
	print "\n++++++++++++++++++++++++++++++++++++++++++++++~All Links~++++++++++++++++++++++++++++++++++++++++++++++\n"
	for link in soup1.find_all('a'):
		print(link.get('href'))
	print "\n++++++++++++++++++++++++++++++++++++++++++++++~All Links End~++++++++++++++++++++++++++++++++++++++++++\n"
	time.sleep(2)
	

def my_body():
	print "\n+++++++++++++++++++++++++++++++++++++++++++++++++~Boby~++++++++++++++++++++++++++++++++++++++++++++++++\n"
	print (soup1.body.prettify().encode("utf-8"))
	print "\n+++++++++++++++++++++++++++++++++++++++++++++++++~Boby End~+++++++++++++++++++++++++++++++++++++++++++++\n"
	time.sleep(2)


new_website = 'y'

while new_website == 'y':
	
	my_banner()

	my_url= raw_input("Enter the perfect Url. : ")
	print "Doing Operation on -->" +"  " + my_url

	page = urllib2.urlopen(my_url)
	soup1 = BeautifulSoup(page,'html.parser')

	this_website = 'y'

	while this_website == 'y' : 
		print '''\n=========================================================================================================\n
			Operations:
			1.View Full HTML Code
			2.View all Links
			3.View only <body> 
			\n=========================================================================================================
			'''
		print "Doing Operation on -->" +"  " + my_url	
		ch= int(raw_input("\n        Enter your choice : "))
		print "\n========================================================================================================="

		if ch == 1 :
			
			full_source_code()
			
		elif ch == 2:
			all_link()
		
		else :
			my_body()
			
	
		this_website= raw_input("Do you want to continiue operation on this website ? '(y/n)' : ")
	
	time.sleep(2)
	print "\n========================================================================================================="
	new_website = raw_input("Do you want to scan a new Website? '(y/n)' : ") 

