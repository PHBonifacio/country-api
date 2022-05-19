import sys

from countries import *

avaiable_commands = ["Currency", "Name", "Population"]

def PrintHelp():
    print("Usage Country API: python country_api.py command")
    for cmd in avaiable_commands:
        print("\t {}".format(cmd))

def IndexOfArgument(argv, arg):
    try:
        return argv.index(arg)
    except ValueError:
        print("The command \'{}\' doesn't exist\n".format(arg))
        return 0


if __name__ == "__main__":
    if 1 == len(sys.argv):
        PrintHelp()
    else:
        try:
            cmd = avaiable_commands.index(sys.argv[1])
            match(cmd):
                case 0:
                    print(GetCountriesCurrency())
                case 1:
                    print(GetCountriesNamesList())
                case 2:
                    print(GetCountryPopulation())
                case _:
                    pass
        except ValueError:
            print("The command \'{}\' doesn't exist\n".format(sys.argv[1]))
            PrintHelp()
        except Exception as e:
            print(e)
        
    