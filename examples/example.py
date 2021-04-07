from printhack import link, unlink, suppress


print("this will print normally")

link()
print("these lines will print")
print("with a timestamp")
print("and a link")

unlink()
print("this will print normally again")

suppress()
print("this won't print at all")
