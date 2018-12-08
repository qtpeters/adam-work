
CREATE TABLE IF NOT EXISTS Foundation (
  ein LONG PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Recipient (
  id INTEGER PRIMARY KEY,
  name TEXT,
  city TEXT NOT NULL,
  state TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Giving_Category (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE IF NOT EXISTS FGrant (
  amount INTEGER,
  year INTEGER,
  description TEXT,
  contact TEXT,
  telephone TEXT,
  foundation_id LONG,
  recipient_id INTEGER,
  giving_cat_id, INTEGER,
  FOREIGN KEY( foundation_id ) REFERENCES Foundation( ein ),
  FOREIGN KEY( recipient_id ) REFERENCES Recipient( id )
  FOREIGN KEY( giving_cat_id ) REFERENCES Giving_Category( id )
);

