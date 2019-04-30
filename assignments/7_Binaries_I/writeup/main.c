/*
 * Name: Akshay Anil
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Akshay Anil
 */


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
