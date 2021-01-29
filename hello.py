def print_hello():
    for i in range(1,10+1):
	if i%2==0:
            print("Hello, git for {}th times(s)!".format(i))
        else:
            print('nope, i is odd.')

if __name__=='__main__':
    print_hello()
