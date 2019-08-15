import getpass
import sys
import telnetlib

HOST = "localhost"
user = raw_input("Enter your username account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("Int loop 0 \n")
tn.write("ip addresss 10.10.10.1 255.255.255.0 \n"
tn.write("end\n")
tn.write("exit\n")
print tn.read_all()