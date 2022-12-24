# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if its the initial module being run
import special_variables
print(__name__)
print(special_variables.__name__) #in this case the __name__ variable is the name of the imported module.

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running indirectly")





def hello():
    print("hello")


if __name__ == "__main__":
    hello()