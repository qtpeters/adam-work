
CREATE TABLE IF NOT EXISTS Foundation (
  ein LONG PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Recipient (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Giving_Category (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS FGrant (
  amount INTEGER NOT NULL,
  year INTEGER NOT NULL,
  description TEXT,
  contact TEXT,
  telephone TEXT,
  foundation_id LONG NOT NULL,
  recipient_id INTEGER NOT NULL,
  giving_cat_id INTEGER NOT NULL,
  FOREIGN KEY( foundation_id ) REFERENCES Foundation( ein ),
  FOREIGN KEY( recipient_id ) REFERENCES Recipient( id )
  FOREIGN KEY( giving_cat_id ) REFERENCES Giving_Category( id )
);

