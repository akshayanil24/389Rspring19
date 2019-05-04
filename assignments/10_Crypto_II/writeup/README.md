# Crypto II Writeup

Name: Akshay Anil
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Akshay Anil

## Assignment Writeup

### Part 1 (70 Pts)
message.txt.gpg contained the flag CMSC389R-{m3ss@g3_!n_A_b0ttl3}
### Part 2 (30 Pts)
ECB:

![ECB](https://github.com/akshayanil24/389Rspring19/blob/master/assignments/10_Crypto_II/ecb.bmp)

CBC:

![CBC](https://github.com/akshayanil24/389Rspring19/blob/master/assignments/10_Crypto_II/cbc.bmp)

Both pictures are made up primarily of red, green, and blue blobs. 
CBC mode encryption builds upon all previous plaintext blocks that were processed. ECB mode encryption doesn't do this, therefore blocks noticibly similar to the original. This similarity makes it less secure than the CBC mode block cipher.
