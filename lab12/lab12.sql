.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  SELECT seven,denero FROM students ;

CREATE TABLE smallest_int AS
  SELECT time,smallest FROM students WHERE smallest > 8 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT a.date, a.number, a.pet, a.color, b.color  FROM students AS a, sp16students AS b WHERE a.date = b.date AND a.number=b.number AND a.pet = b.pet;

CREATE TABLE sevens AS
  select s.seven from students as s, checkboxes as c
    where s.time = c.time and s.number = 7 and c."7" = "True";

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color from students as a, students as b
    where a.pet = b.pet and a.song = b.song and a.time < b.time;
