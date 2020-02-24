import sys, os
from webbot import Browser

credentials = {
	'mail': 'nitingoswami473@gmail.com',
	'password': 'saymemyname1',
	'username':'theuitown'
}

# log into github and create new repository
def main():
	reponame=input("Enter Reponame: ")
	web = Browser()
	# login to github
	web.go_to('github.com/login')
	web.type(credentials['mail'], into='Email', id='login_field')
	web.type(credentials['password'], into='Password' , id='password')
	web.click(tag='input', text='Sign in')
	# create new repository
	web.go_to('github.com/new')
	web.type(reponame, id='repository_name')
	web.type("This is the computer generated repository :fire: :heart: "+reponame, id='repository_description')
	web.click(id="repository_auto_init")
	web.click(id='repo-new-license-details')
	web.click(id='license-label-apache-2.0')
	web.click(tag='button', text='Create repository')

if __name__ == "__main__":
	main()
