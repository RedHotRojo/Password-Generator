# Common passwords

Here are possible passwords I found in Kali Linux's files. rockyou.txt (ISO-8859-1) was converted to rockyou_utf-8.txt (UTF-8) using a command I found on [StackOverflow](https://stackoverflow.com/a/42187267). Then, all of the files were combined into one using the Linux command:

`cat common.txt passwords.lst rockyou_utf-8.txt wordlist.txt > cmnpswd.txt`

I found that exact syntax somewhere, though I forgot where.

I then ran minimize.py to reduce that list to passwords that were at least 8 characters long. That file was then moved to the parent directory.
