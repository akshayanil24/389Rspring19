# Writeup 2 - OSINT

Name: Akshay Anil
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Akshay Anil

## Assignment Writeup

### Part 1 (45 pts)

>What is `v0idcache`'s real name?

__Elizabeth Moffet__ goes by the name `v0idcache`.
- - - -
>Where does `v0idcache` work? What is the URL to their website?

`v0idcache` works __[13/37th National Bank](http://1337bank.money/)__.
- - - -
>List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.

Source  | What was Discovered
------------ | -------------
[Pastebin](https://pastebin.com/WghDuAr7) | A simple search for 'v0idcache' on Google brought up only one result. The link sent me to a conversation between `v0idcache` and `fl1nch`, pasted on Pastebin. `fl1nch` might be a possible contact.
[Twitter](http://twitter.com/v0idcache)  | Seeing that `v0idcache` is a username, I checked Twitter to see if there was a profile for this account. The account is linked to a person named __Elizabeth Moffet__ who is the __CEO of 13/37th National Bank__. She has experience in __cybersecurity__, __blockchain__, and __finance__. Moffet lives in the __Netherlands__.
whois | Running `whois -h whois.namecheap.com "1337bank.money"` on a terminal provided several pieces of registerant information. Email: __v0idcache@protonmail.com__, Address: __Leeteinde 12, Broek, Waterland, 1151 AK__, and Phone: __+1.323331__.
[Github](https://github.com/v0idcache) | `v0idcache` has a profile on Github. There are no public repositories / contributions for this account.
- - - -
>List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

IP Address  | Location  | DNS History  | How it was discovered  
------------ | ------------- | ------------- | -------------
142.93.136.81  | Netherlands  | N/A  | Running `nmap 1337bank.money` provided the ip address associated with the domain. The location was retrieved using iplocation.net. I was not able to find any DNS History using [SecurityTrails' DNS-Trails](https://securitytrails.com/domain/1337bank.money/dns).
- - - -
>List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.
* [CMSC389R-{h1ding_fil3s_in_r0bots_L0L}](http://1337bank.money/secret_directory)
* [CMSC389R-{h1dd3n_1n_plain_5ight}](view-source:http://1337bank.money/)
- - - -
>What ports are open on the website? What services are running behind these ports? How did you discover this?

Port  | Service  | How it was discovered  
------------ | ------------- | -------------
22  | ssh  | `nmap -p- 142.93.136.81`
80 | http | `nmap -p- 142.93.136.81`
1337 | waste | `nmap -p- 142.93.136.81`
- - - -
>Which operating system is running on the website? How did you discover this?

[Censys](https://censys.io/) tells me that the operating system is __Ubuntu__.
- - - -
>**BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)

* [CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}](https://www.ultratools.com/tools/dnsLookupResult)
* CMSC389R-{YWX4H3d3Bz6dx9lG320dv0JZh} (Contents of the AB4300.txt file mentioned in the conversation on Pastebin. Found within `/home/files/` after brute force attack.)

### Part 2 (75 pts)

>Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.
Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.
Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.
Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

The __stub.py__ file suggested trying combinations of IP addresses with open ports to find an access to a system shell. I already knew the IP address so I went through ports 22, 80, and 1337 to find a login portal. Running `nc 142.93.136.81 1337` prompted me for a username and password combination. I assumed the username would be `fl1nch` because I didn't have to use it anywhere else, so I edited __stub.py__ to attempt logging in with the passwords in `rockyou.txt`. An hour or so passed without any successful logins, so I changed the username to `v0idcache`. The script told me that a combination of username `v0idcache` with password `linkinpark` granted access to the shell. A simple `cd home` followed by `ls` showed me the flag file. Text editors such as __nano__ and __vim__ were disabled, so I called `cat flag.txt` to print the contents of the file. This gave me the flag __CMSC389R-{brut3_f0rce_m4ster}__.
