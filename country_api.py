
import argparse

from countries import *

avaiable_commands = ["Currency", "Name", "Population"]

def IndexOfArgument(argv, arg):
    try:
        return argv.index(arg)
    except ValueError:
        print("The command \'{}\' doesn't exist\n".format(arg))
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='country_api', description='Get informormation from any country')
    parser.add_argument('command', help='Chose what command should execute', choices=avaiable_commands)
    parser.add_argument('-c', '--country', help='Complete or part of a country name', default=None)
    parser.add_argument('-f', '--full', help='Enforce country full name', action='store_true')
    parser.add_argument('-m', '--max', help='Max number of results', action='store')
    args = parser.parse_args()
    try: 
        match(avaiable_commands.index(args.command)):
            case 0:
                print(GetCountriesCurrency())
            case 1:
                print(GetCountriesNamesList(args.country, args.full))
            case 2:
                print(GetCountryPopulation())
            case _:
                pass

    except Exception as e:
        print(e)
        
    