
import xlrd
import sqlite3

ein_set = set([])
rname_set = set([])
gc_name = set([])

def insert_foundation( ein, name, city, state, c ):
  
  if ( not ( ein in ein_set ) ):
    ein_set.add( ein )
    query = 'INSERT INTO Foundation ( ein, name, city, state )'
    query = query + ' values ( %d, "%s", "%s", "%s" );' % ( int( ein ), 
                                                          name, city, state )
    c.execute( query )

  c.execute( "SELECT last_insert_rowid();" )
  return c.fetchone()[0]

def insert_recipient( name, city, state, c ):
  query = 'INSERT INTO Recipient ( name, city, state )'
  query = query + ' values ( "%s", "%s", "%s" );' % ( name, 
                                                      city, 
                                                      state )
  c.execute( query )
  c.execute( "SELECT last_insert_rowid();" )
  return c.fetchone()[0]

def insert_giving_category( name, c ):
  query = 'INSERT INTO Giving_Category ( name )'
  query = query + ' values ( "%s" );' % name 
  c.execute( query )
  c.execute( "SELECT last_insert_rowid();" )
  return c.fetchone()[0]

def insert_grant( amt, year, desc, contact, tele, ein, rid, gc_id, c ):

  print( "Amt: %s" % amt )
  query = 'INSERT INTO FGrant ( amount, year, description, '
  query = query + 'contact, telephone, foundation_id, recipient_id, giving_cat_id  )'
  query = query + ' values ( %d, %d, "%s", "%s", "%s", %d, %d, %d );' % ( int( amt ), int( year ), desc, 
                                                      contact, tele, int( ein ), 
                                                      int( rid ), int( gc_id ) )
  c.execute( query )
  c.execute( "SELECT last_insert_rowid();" )
  return c.fetchone()[0]

def main():
  workbook = xlrd.open_workbook( "Adam-Spreadsheet.xlsx" )
  sheet = workbook.sheet_by_name( u"Conservation + Int'l Data" ) 
  conn = sqlite3.connect( 'cvintl.db' )
  c = conn.cursor()

  itr = sheet.get_rows()
  next( itr )

  for row in itr:

    if ( not row[0].value ): 
      continue

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

  conn.commit()
  conn.close()

main()
