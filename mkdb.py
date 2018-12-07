
import pandas as pd

spreadsheet = pd.ExcelFile( "Adam-Spreadsheet.xlsx" )
tab = spreadsheet.parse( u"Conservation + Int'l Data" ) 

help( tab )
