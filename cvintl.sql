
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
  description TEXT,
  contact TEXT,
  telephone TEXT,
  foundation_id LONG,
  recipient_id INTEGER,
  FOREIGN KEY( foundation_id ) REFERENCES Foundation( ein ),
  FOREIGN KEY( recipient_id ) REFERENCES Recipient( id )
);

