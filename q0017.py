# xls 转 xml
import xlrd
import xml

if __name__ == '__main__':
    template = '''<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
}
</students>
</root>'''

    xls = xlrd.open_workbook(excel_path)
    sheet1 = xls.sheet_by_index(0)
    sheet1.

