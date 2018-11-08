
import io
import sys
import os
from lib.writeDicom import writeDicom

__version__ = '1.0.1'

class WriteDicom(object):
    arguments = None
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变默认的标准输出

    def __init__(self, subparser, command, description='default'):
        self.parse_arguments(description, subparser, command)
    
    def parse_arguments(self, description, subparser, command):
        parser = subparser.add_parser(
            command,
            help="Write Dicom file",
            description=description
        )

        parser.add_argument("-d", "--dataset", dest="dataset", default='', help="dataset for write dicom file")
        parser.add_argument("-f", "--filename", dest="filename", default='', help="filename for write dicom file")
        parser.add_argument("-v", '--version', action='version', version="WriteDicom version" + __version__)

        parser = self.add_optional_arguments(parser)
        parser.set_defaults(func=self.process_arguments)

    def add_optional_arguments(self, parser):
        # Override this for custom arguments
        return parser

    def process_arguments(self, arguments):
        self.arguments = arguments

        try:
            if self.arguments.dataset and self.arguments.filename:
                writeDicom(self.arguments.dataset, self.arguments.filename)
            
        except Exception as e:
            print(e)

        self.process()
    
    def process(self):
        return