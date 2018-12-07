
import xlrd
import sqlite3

workbook = xlrd.open_workbook( "Adam-Spreadsheet.xlsx" )
sheet = workbook.sheet_by_name( u"Conservation + Int'l Data" ) 
conn = sqlite3.connect( 'cvintl.db' )
c = conn.cursor()

itr = sheet.get_rows()
next( itr )

einset = set([])

for row in itr:

  ein = row[0].value
  if ( not ein ): 
    break

  if ( ein in einset ):
    continue

  einset.add( ein )

  name = row[1].value
  city = row[2].value
  state = row[3].value
  
  query = 'INSERT INTO Foundation ( ein, name, city, state )'
  query = query + ' values ( %d, "%s", "%s", "%s" );' % ( int( ein ), 
                                                          name, 
                                                          city, 
                                                          state )
  c.execute( query )
  print( query )

conn.commit()
conn.close()
