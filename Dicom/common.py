import glob
import os.path

import pydicom


def read_dicom(dicom: str):
    """
    # read dicom file, and get data info
    :param dicom:dicom data
    :return: dicom info
    """

    data_info_dict = {}
    if os.path.isfile(dicom) and dicom.endswith(".dcm"):
        dcm = pydicom.dcmread(dicom, force=True)
    elif os.path.isdir(dicom):
        dicom_files = glob.glob(f"{dicom}/*")
        dcm = pydicom.dcmread(dicom_files[0], force=True)
    else:
        print("please check your input, input mast be the dir or file of .dcm")
        return

    # 显示dicom文件中存在哪些属性
    # print(dcm.__dir__())

    if "WindowWidth" in dcm.__dir__():
        WW = dcm.WindowWidth
        WL = dcm.WindowCenter
        data_info_dict["WW"] = WW
        data_info_dict["WL"] = WL
    return data_info_dict
