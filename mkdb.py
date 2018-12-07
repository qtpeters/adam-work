
import xlrd

workbook = xlrd.open_workbook( "Adam-Spreadsheet.xlsx" )
sheet = workbook.sheet_by_name( u"Conservation + Int'l Data" ) 

itr = sheet.get_rows()

for row in itr:
  print( row )
