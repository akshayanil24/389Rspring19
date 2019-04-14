# Writeup 7 - Binaries I

Name: Akshay Anil
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Akshay Anil

## Assignment Writeup

### Part 1 (90 Pts)

```c
int main()
{
  int dword1 = 0x1ceb00da;
  int dword2 = 0xfeedface;

  printf("%s\n", dword2);
  printf("%s\n", dword1);

  dword1 = dword1 ^ dword2;
  dword2 = dword2 ^ dword1;
  dword1 = dword1 ^ dword2;

  printf("%s\n", dword2);
  printf("%s\n", dword1);
  
  return 0;
}
```

### Part 2 (10 Pts)

This program computes a series of xors between two variables to while updating their values each time. The value of the variables are displayed both before and after the xors.
