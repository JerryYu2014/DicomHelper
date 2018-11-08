
import io
import sys
import os
import datetime
import json

import pydicom
from pydicom.data import get_testdata_files
from pydicom.dataset import Dataset, FileDataset, DataElement

import numpy as np
from PIL import Image

# 命令行传入json字符串格式："{\"status\": \"ok\"}"

def writeDicom(dataset, outfilename):

    # print(type(dataset))

    # datasetObj = json.loads(dataset)

    # print(type(datasetObj))
    # print(type(datasetObj['status']))

    filename = get_testdata_files('color-px.dcm')[0]

    ds = pydicom.dcmread(filename)

    # print("Setting file meta information...")
    # Populate required values for file meta information
    # file_meta = Dataset()
    # file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
    # file_meta.MediaStorageSOPInstanceUID = "1.2.3"
    # file_meta.ImplementationClassUID = "1.2.3.4"
    # file_meta.TransferSyntaxUID = "1.2.840.10008.1.2.5"

    # file_meta = ds.file_meta
    # file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
    # file_meta.MediaStorageSOPInstanceUID = "1.2.3"
    # file_meta.ImplementationClassUID = "1.2.3.4"
    # file_meta.TransferSyntaxUID = "1.2.840.10008.1.2.5"

    # Pixel Data
    img = Image.open('123.bmp')
    nparr = np.asarray(img)

    # ds[0x7FE0, 0x0010] = DataElement(0x7FE00010, 'OW', img.tobytes())
    ds.PixelData = nparr.tobytes()

    # print("Setting dataset values...")
    # Create the FileDataset instance (initially no data elements, but file_meta supplied)
    # ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0" * 128)

    # ds.PatientID = "123456"
    # ds.PatientName = "Test^Firstname"

    # Patient's Name
    # ds[0x0010, 0x0010] = DataElement(0x00100010, 'PN', PersonNameUnicode(b"Wang^XiaoDong=\xcd\xf5\x5e\xd0\xa1\xb6\xab=", [default_encoding, 'GB18030']))
    ds[0x0010, 0x0010] = DataElement(0x00100010, 'PN', '张无忌'.encode('GB18030'))
    # Patient ID
    ds[0x0010, 0x0020] = DataElement(0x00100020, 'LO', '123456')
    # Patient's Birth Date
    ds[0x0010, 0x0030] = DataElement(0x00100030, 'DA', '20010101')
    # Patient's Sex
    ds[0x0010, 0x0040] = DataElement(0x00100040, 'CS', '男'.encode('GB18030'))
    # Study Date
    ds[0x0008, 0x0020] = DataElement(0x00080020, 'DA', '20181108')
    # Study Time
    ds[0x0008, 0x0030] = DataElement(0x00080030, 'TM', '201309')
    # Accession Number
    ds[0x0008, 0x0050] = DataElement(0x00080050, 'SH', '6257')
    # Study Instance UID
    # ds[0x0020, 0x000D] = DataElement(0x0020000D, 'UI', '1.2.840.1.2.8.236.511020181107')
    # Study ID
    ds[0x0020, 0x0010] = DataElement(0x00200010, 'SH', '6257')
    # Patient's Age
    ds[0x0010, 0x1010] = DataElement(0x00101010, 'AS', '34')
    # Series Date
    ds[0x0008, 0x0021] = DataElement(0x00080021, 'DA', '20181107')
    # Series Time
    ds[0x0008, 0x0031] = DataElement(0x00080031, 'TM', '120709')
    # Modality
    ds[0x0008, 0x0060] = DataElement(0x00080060, 'CS', 'US')
    # Performing Physician's Name
    ds[0x0008, 0x1050] = DataElement(0x00081050, 'PN', '')
    # Body Part Examined
    ds[0x0018, 0x0015] = DataElement(0x00180015, 'CS', '')
    # Series Instance UID
    # ds[0x0020, 0x000E] = DataElement(0x0020000E, 'UI', '1.2.840.1.2.8.236.51102018110715')
    # Series Number
    ds[0x0020, 0x0011] = DataElement(0x00200011, 'IS', '1')
    # Manufacturer
    ds[0x0008, 0x0070] = DataElement(0x00080070, 'LO', 'advoster')
    # Institution Name
    ds[0x0008, 0x0080] = DataElement(0x00080080, 'LO', '同仁堂'.encode('GB18030'))
    # Image Type
    ds[0x0008, 0x0008] = DataElement(0x00080008, 'CS', ['DERIVED', 'SECONDARY'])   # SECONDARY
    # Instance Number
    ds[0x0020, 0x0013] = DataElement(0x00200013, 'IS', '1')
    # # Pixel Data
    # img = Image.open('123.bmp')
    # nparr = np.asarray(img)

    # ds[0x7FE0, 0x0010] = DataElement(0x7FE00010, 'OW', nparr.tobytes())
    # # ds.PixelData = nparr.tobytes()

    # Window Center
    # ds[0x0028, 0x1050] = DataElement(0x00281050, 'DS', "127.0")
    # Window Width
    # ds[0x0028, 0x1051] = DataElement(0x00281051, 'DS', "255.0")
    # # SOP Class UID
    # ds[0x0008, 0x0016] = DataElement(0x00080016, 'UI', '1.2.840.10008.5.1.4.1.1.7')
    # # SOP Instance UID
    # ds[0x0008, 0x0018] = DataElement(0x00080018, 'UI', '1.2.840.1.2.8.236.511020181107154038')
    # # Instance Number
    # ds[0x0020, 0x0013] = DataElement(0x00200013, 'IS', 1)

    # Bits Allocated
    # ds[0x0028, 0x0100] = DataElement(0x00280100, 'US', 16)
    # Rows
    ds[0x0028, 0x0010] = DataElement(0x00280010, 'US', 480)
    # Columns
    ds[0x0028, 0x0011] = DataElement(0x00280011, 'US', 640)

    # # Series Instance UID
    # ds[0x0020, 0x000E] = DataElement(0x0020000E, 'UI', '1.2.840.10008.5.1.4.1.2.5')
    # # Study Instance UID
    # ds[0x0020, 0x000D] = DataElement(0x0020000D, 'UI', '1.2.840.10008.5.1.4.1.2.1')
    # Photometric Interpretation
    ds[0x0028, 0x0004] = DataElement(0x00280004, 'UI', 'RGB')
    # Samples Per Pixel
    ds[0x0028, 0x0002] = DataElement(0x00280002, 'US', 0)
    # Pixel Aspect Ratio
    ds[0x0028, 0x0034] = DataElement(0x00280034, 'IS', ['1', '1'])
    # Bits Stored
    # ds[0x0028, 0x0101] = DataElement(0x00280101, 'US', 1)
    # High Bit
    # ds[0x0028, 0x0102] = DataElement(0x00280102, 'US', 19)

    # dt = datetime.datetime.now()
    # ds.ContentDate = dt.strftime('%Y%m%d')
    # ds.ContentTime = dt.strftime('%H%M%S.%f')  # long format with micro seconds

    ds.save_as(outfilename)

    # pydicom.write_file(filename, ds)

    print('Load file {} ...'.format(outfilename))
    ds = pydicom.dcmread(outfilename)
    print(ds)
