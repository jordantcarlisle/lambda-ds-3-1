# my-lambdata-pt4/my_mod.py

def enlarge(n):
    return n * 100



if __name__ == '__main__':
# only if run from command line, invoke the following code

    print("junk")
    print('GLOBAL SCOPE')

    y = float(input("Plaeas input a number to enlarge: "))

    print(enlarge(y))
