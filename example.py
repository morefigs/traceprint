from printhack import link, unlink, suppress


print("this will print normally")
link()
print("these lines will print")
print("with a timestamp")

from time import sleep
sleep(.05)
print("and a link")
unlink()
print("this will print normally again")
suppress()
print("this won't print at all")
