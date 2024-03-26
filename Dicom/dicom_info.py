import argparse
import os
from tqdm import tqdm
import pandas as pd
from common import read_dicom


def run():
    parser = argparse.ArgumentParser(description="dicom data info")
    parser.add_argument("--dicom_file", type=str, default="../data/dicom/xxx.dicom", help="the dicom data")
    args = parser.parse_args()

    data_info = read_dicom(args.dicom_file)
    print("dicom_info:", data_info)
    print(f"***Done***")


def save_csv(data_list, save_file):
    result_data =pd.DataFrame(data_list, columns=["name", "WL", "WW"])
    result_data.to_csv(save_file, index=False)


def check_data_window():
    parser = argparse.ArgumentParser(description="dicom data info")
    parser.add_argument("--dicom_dir", type=str, default="dir", help="the dicom data")
    parser.add_argument("--save_file", type=str, default="csv", help="the result info")
    args = parser.parse_args()
    result_list = []
    folder_list = os.listdir(args.dicom_dir)
    pbar = tqdm(total=len(folder_list))
    for folder in folder_list:
        folder_dir = os.path.join(args.dicom_dir, folder)
        data_info = read_dicom(folder_dir)
        WW = data_info["WW"]
        WL = data_info["WL"]
        result_list.append([folder, WL, WW])

        pbar.update(1)
    pbar.close()
    save_csv(result_list, args.save_file)

    print(f"***Done***")


if __name__ == '__main__':
    # run()
    check_data_window()
