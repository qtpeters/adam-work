#!/usr/bin/env python

import fileinput as fi

for line in fi.input():
    record = line.split( '|' )
    foundation = record[0]
    years = record[1].split( ',' )
    recipients = record[2].split( ',' )
    amounts = record[3].split( ',' )

    print( foundation )
    for i in range( 0, len( years ) ):
        print( '\t%s %s %s' % ( years[i], recipients[i], '${:,.0f}'.format( int( amounts[i] ) ) ) )
    print
