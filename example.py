# Created by Sezer Bozkir<admin@sezerbozkir.com>

from PIL import Image
from pandas import ExcelFile
import os
from textAddtoImage import add_angle_text, add_multiline_text


def excel_to_dict(file: ExcelFile):
    content = {}
    for sheet_name in file.sheet_names:
        content[sheet_name] = file.parse(sheet_name).to_dict('records')
    return content


def create_sparkling(data):
    img_result = add_angle_text(str(data["ID"]), img=base_image, angle=270, position=(1055, 170))
    img_result = add_angle_text(str(data["Name"]), img=img_result, angle=270, position=(1015, 120))
    img_result = add_multiline_text(str(data['Name']), img_result, position=(220, 90))
    img_result = add_multiline_text(str(data["Note"]),
                                    img_result,
                                    (110, 150), split_loop_size=62)
    img_result = add_multiline_text(str(data["Owner"]),
                                    img=img_result,
                                    position=(290, 540))
    img_result = add_angle_text(str(data["VOUCHER"]), img=img_result, angle=270, position=(1035, 530), color="#FFF")
    img_result.save(f"output/{data['Name']}_{data['Type']}.png")


if __name__ == '__main__':
    # excel_file = ExcelFile("Example.xlsx")
    excel_file = ExcelFile("sample_excel.xlsx")
    # base_image = Image.open("template.jpg").convert("RGBA")
    base_image = Image.open("sample_template.png").convert("RGBA")
    file_content = excel_to_dict(excel_file)
    file_content = file_content['Name List']

    if not os.path.exists("output"):
        os.makedirs("output")

    for row in file_content:
        create_sparkling(row)
        print(f"{row['Name']} sparkling created.")
