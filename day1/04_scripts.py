import argparse
import sys

"""
The above are import statements. They import funtionality from other
python libraries. In the specific cases above, the imported modules
are from the python standard library. They are always available and
require no installation...provided you're using the correct
version of python.
"""

def parseArgs():
    print " ".join(sys.argv)
    print 
    parser = argparse.ArgumentParser()

    parser.add_argument("req1", type=int)
    parser.add_argument("req2", type=str)

    parser.add_argument("--bool", action="store_true", default=False)
    parser.add_argument("--int", action="store", default=0, type=int)
    parser.add_argument("--opt", action="store", default="foo")

    args = parser.parse_args()
    return args

def main():
    args = parseArgs()
    if args.bool:
        print (args.int + args.req1)
    else:
        print args.opt + args.req2



#This is a standard and good trick for making sure main only runs
#if this is a scipt. It also means you can import this module into
#other code.
if __name__ == "__main__":
    main()
