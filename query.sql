
-- foundations that have made grants to at least three separate organizations
-- in the last three years
-- for less than $250,000
SELECT dfn, GROUP_CONCAT( year ), GROUP_CONCAT( recipient_name ), GROUP_CONCAT( amt ),  COUNT( * ) AS dfc FROM (
	SELECT 
	  f.name AS dfn, 
	  r.name AS recipient_name, 
	  g.year AS year, 
	  g.amount AS amt
	FROM Foundation f, FGrant g, Recipient r 
	WHERE f.ein=g.foundation_id
	AND g.recipient_id=r.id
        AND year > 2015	
  	AND amt < 250000
	ORDER BY f.name
) GROUP BY dfn 
  HAVING dfc >= 3 
  ORDER BY dfn;
