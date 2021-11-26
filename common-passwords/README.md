# Common passwords

Here are possible passwords I found in Kali Linux's files. rockyou.txt (ISO-8859-1) was converted to rockyou_utf-8.txt (UTF-8) using a command I found on [StackOverflow](https://stackoverflow.com/a/42187267). Then, all of the files were combined into one using the Linux command:

`cat common.txt passwords.lst rockyou_utf-8.txt wordlist.txt > commonpasswords.txt`

I found that exact syntax somewhere, though I forgot where. It was probably a geeksforgeeks article.

I then ran minimize\_passwords.py to reduce that list to passwords that were at least 8 characters long. The new file (common\_passwords.min.txt) file was then moved to the "generator" directory.
