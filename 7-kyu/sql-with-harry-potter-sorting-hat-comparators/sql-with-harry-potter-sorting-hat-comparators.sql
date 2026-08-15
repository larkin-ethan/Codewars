-- Students must have:
--  Evil and cunning
--  Brave but not evil
--  Studious or intelligent
--  Hufflepuff or hufflepuff
​
SELECT * FROM students WHERE 
      (
        quality1 = 'hufflepuff' or
        quality1 = 'studious' or 
        quality2 = 'hufflepuff' or
        quality2 = 'intelligent'
      ) 
      or
      (
        quality1 = 'evil' and
        quality2 = 'cunning'
      )
      or
      (
        quality1 = 'brave' and
        quality2 != 'evil'
      )
      ORDER BY id asc;