# Writeup 6 - Forensics

Name: Akshay Anil
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Akshay Anil

## Assignment Writeup

### Part 1 (45 Pts)
> Warmup: what IP address has been attacked?

**142.93.136.81** was attacked
> What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

Tools such as **nmap** might have been used to access the victim machine. Inspection of netlog.pcap shows the attacker using [**Juniper Networks** which can be used for packet capture](https://kb.juniper.net/InfoCenter/index?page=content&id=KB11709). This might just be something else though.

>What are the hackers' IP addresses, and where are they connecting from?

The hackers' IP address is **159.203.113.181**. This address is associated with a physical address in [**Clifton, New Jersey**](https://whatismyipaddress.com/ip/159.203.113.181).

>What port are they using to steal files on the server?

Port **21** was used to steal files from the server. This was found by looking for packets with labeled **FTP** (File Transfer Protocol).

>Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,
a) What kind of file is it?
b) Where was this photo taken? Provide a country and city in your answer.
c) When was this photo taken? Provide a timestamp in your answer.
d) What kind of camera took this photo?
e) How high up was this photo taken? Provide an answer in meters.

The stolen file was an **image** named find_me.jpg. The photo was taken in **Punta del Este, Uruguay** on **December 23, 2018** at **17:16:24** with an **Apple iPhone 8**. The altitude reads roughly **4.5 meters below sea level**.

>Which file did the attackers leave on the server?

The attackers left a file named **greetz.fpff**

>What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.

This kind of intrusion can be prevented by enabling two-factor authentication to prevent adversaries from connecting to the service in the first place.
### Part 2 (55 Pts)
The parser for this part can be found as **/writeup/parser.py**. In addition to the default libraries bundled with Python, you will need to install **Pillow** via `pip install Pillow` as well as **ImageMagick** with `sudo apt-get install imagemagick`.

> When was `greetz.fpff` generated?

This file was generated on **March 27, 2019** at **12:15:05 AM**.

>Who authored `greetz.fpff`?

**fl1nch** was the author of this file.

>List each section, giving us the data in it *and* its type.

-SECTION 1-

Length: 24

Type: ASCII

Value: Hey you, keep looking :)


-SECTION 2-

Length: 16

Type: COORD

Value: (52.336035, 4.880673)


-SECTION 3-

Length: 202776

Type: PNG

Value: Displayed in pop-up **(shows up when script is run)**


-SECTION 4-

Length: 44

Type: ASCII

Value: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC


-SECTION 5-

Length: 80

Type: ASCII

Value: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=


>Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.

CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak} was found on the PNG parsed from `greetz.fpff`.
