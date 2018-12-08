
import xlrd
import sqlite3

ein_set = set([])
rname_set = set([])
gc_name_set = set([])

def insert_foundation( ein, name, city, state, c ):
 
  ein = int( ein )

  if ( not ( ein in ein_set ) ):
    ein_set.add( ein )
    query = "INSERT INTO Foundation ( ein, name, city, state )"
    query = query + " values ( ?, ?, ?, ? );" 
    c.execute( query, ( ein, name, city, state ) )

  return ein

def insert_recipient( name, city, state, c ):

  if ( not ( name in rname_set ) ):
    rname_set.add( name ) 
    query = "INSERT INTO Recipient ( name, city, state )"
    query = query + " values ( ?, ?, ? );"
    c.execute( query, ( name, city, state ) )
  
  c.execute( "SELECT id FROM Recipient WHERE name = ?", ( name, ) )
  return c.fetchone()[0]

def insert_giving_category( name, c ):
  
  if ( not ( name in gc_name_set ) ):
    gc_name_set.add( name ) 
    query = "INSERT INTO Giving_Category ( name ) values ( ? );"
    c.execute( query, ( name, ) )
  
  c.execute( "SELECT id FROM Giving_Category WHERE name = ?", ( name, ) )
  return c.fetchone()[0]

def insert_grant( amt, year, desc, contact, tele, ein, rid, gc_id, c ):
  
  amt = int( amt )
  year = int( year )
  ein = int( ein )
  rid = int( rid )
  gc_id = int( gc_id )

  print( "< %d >, < %d >, < %s >, < %s >, < %s >, < %d >, < %d >, < %d >" 
          % ( amt, year, desc, contact, tele, ein, rid, gc_id ) )

  query = 'INSERT INTO FGrant ( amount, year, description, '
  query = query + 'contact, telephone, foundation_id, recipient_id, giving_cat_id  )'
  query = query + ' values ( ?, ?, ?, ?, ?, ?, ?, ? );' 

  c.execute( query, ( amt, year, desc, contact, tele, ein, rid, gc_id ) )

def main():
  workbook = xlrd.open_workbook( "Adam-Spreadsheet.xlsx" )
  sheet = workbook.sheet_by_name( u"Conservation + Int'l Data" ) 
  conn = sqlite3.connect( 'cvintl.db' )
  c = conn.cursor()

  itr = sheet.get_rows()
  next( itr )

  i = 0

  for row in itr:

    i = i + 1

    if ( not row[0].value ): 
      break

    ein = insert_foundation( row[0].value, row[1].value, row[2].value, row[3].value, c )
    r_id = insert_recipient( row[4].value, row[5].value, row[6].value, c )
    gc_id = insert_giving_category( row[7].value, c )
    insert_grant( 
      row[8].value, 
      row[9].value, 
      row[10].value, 
      row[11].value, 
      row[12].value,
      ein, r_id, gc_id, c )

  print( "Loop iterated %d times" % i )
  conn.commit()
  conn.close()

main()
