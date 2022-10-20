def dec1(func):
    def nowexec():
        print("Module starting")
        func()
        print("Ending")
    return nowexec

@dec1
def command():
    print("This is a test command")

command()