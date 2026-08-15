-- Students must have:
--  Evil and cunning
--  Brave but not evil
--  Studious or intelligent
--  Hufflepuff or hufflepuff
​
SELECT * FROM students WHERE 
      (
        quality1 = 'hufflepuff' OR
        quality1 = 'studious' OR
        quality2 = 'hufflepuff' OR
        quality2 = 'intelligent'
      ) 
      OR
      (
        quality1 = 'evil' AND
        quality2 = 'cunning'
      )
      OR
      (
        quality1 = 'brave' AND
        quality2 != 'evil'
      )
      ORDER BY id ASC;