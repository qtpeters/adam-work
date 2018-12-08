
--  foundations that have made grants to at least three separate organizations
SELECT dfn, COUNT( * ) AS dfc FROM (
	SELECT 
	  DISTINCT( f.name ) AS dfn, 
	  g.recipient_id rid 
	FROM Foundation f, FGrant g 
	WHERE f.ein=g.foundation_id 
	ORDER BY f.name
) GROUP BY dfn 
  HAVING dfc >= 3 
  ORDER BY dfn;
