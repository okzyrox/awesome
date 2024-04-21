import sys, getopt, os

from awesome import runner


def main(argv):
     inputfile = ''
   
     if not len(argv) > 1:
          print("Usage: awesome -i <inputfile.aw>")
          exit()

     try:
          opts, args = getopt.getopt(argv,"hi:o:",["infile="])
     except getopt.GetoptError:
          print("Usage: awesome -i <inputfile>")
          sys.exit(2)
     for opt, arg in opts:
          if opt == '-h':
               print("Awesome: the only good programming language")
               print("Usage: awesome -i <inputfile>")
               sys.exit()
          elif opt in ("-i", "--infile"):
               if os.path.exists(arg):
                    inputfile = arg
     

     runner.fromFile(inputfile)
     exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])