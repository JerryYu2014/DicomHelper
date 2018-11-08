import argparse
from scripts.writeDicom import WriteDicom

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    writeDicom = WriteDicom(subparser, "WriteDicom", "Write Dicom file.")
    
    arguments = parser.parse_args()
    try:
        arguments.func(arguments)
    except:
        parser.print_help()