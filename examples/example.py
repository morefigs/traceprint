import printstack


print("Hello world")
print("Hola mundo")


def func(i=None):
    print(f'Hello from func, {i=}')


def func_with_loop():
    for i in range(5):
        func(i)


func()
func_with_loop()
