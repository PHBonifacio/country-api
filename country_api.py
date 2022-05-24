
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
                result = GetCountriesCurrency(args.country, args.full)
                print("GetCountriesCurrency")
                if result :
                    for country in result:
                        print("\t >> {} : {}".format(country[0], country[1]))
                else:
                    print("\t >> Not found")
            case 1:
                result = GetCountriesNamesList(args.country, args.full)
                print("GetCountriesNamesList")
                if result :
                    for name in result:
                        print("\t >> {}".format(name))
                else:
                    print("\t >> Not found")
            case 2:
                result = GetCountryPopulation(args.country, args.full)
                print("GetCountryPopulation")
                if result :
                    for country in result:
                        print("\t >> {} : {}".format(country[0], country[1]))
                else:
                    print("\t >> Not found")
            case _:
                pass

    except Exception as e:
        print(e)
        
    