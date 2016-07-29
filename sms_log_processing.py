import configparser
import os

import openpyxl


def convert_excel_to_dict(excl_file, sheet_name):
    header = []
    kpi_sum = []
    try:
        wb = openpyxl.load_workbook(filename=excl_file)
        sheet_ranges = wb[sheet_name]

        for index, row in enumerate(sheet_ranges.iter_rows(row_offset=0)):
            sum_element = {}
            for i in range(len(row)):
                if index == 0:
                    # header
                    if row[i].value is not None:
                        header.append(row[i].value.strip().upper())
                else:
                    # add expected data to kpi sum dictionary
                    if i < len(header):
                        sum_element[header[i]] = row[i].value
            if index > 0:
                kpi_sum.append(sum_element)
    except KeyError as keyerror:
        print(str(keyerror))
    return kpi_sum


if __name__ == '__main__':
    cf = configparser.ConfigParser()
    cf.read('setting.ini')
    template_folder = (cf['DEFAULT']['template_folder'])

    sms_template_files = [x for x in os.listdir(template_folder) if os.path.isfile(os.path.join(template_folder, x))]
    for f in sms_template_files:
        wb = openpyxl.load_workbook(os.path.join(template_folder, f))
        shs = wb.sheetnames()
        print (type(shs))
