sudo -i -u postgres

psql

--users students:
CREATE TABLE students(
 id serial PRIMARY KEY,
 name VARCHAR(20) NOT NULL,
 age INTEGER NOT NULL,
 gender VARCHAR(6) NOT NULL,
 nationality TEXT
);

--audience table:
CREATE TABLE audience(
 id serial PRIMARY KEY,
 student_id INTEGER REFERENCES students(id),
 lesson VARCHAR(20) NOT NULL,
 floor INTEGER NOT NULL,
 square INTEGER NOT NULL
);

-- fill students table
INSERT INTO students (name, age, gender, nationality)
VALUES
  ('Vlad', 25, 'male', 'belarus'),
  ('Elen', 32, 'female', 'ukrainian'),
  ('Philip', 25, 'male', 'germany');

-- fill audience table:
INSERT INTO audience (lesson, floor, square)
VALUES
  ('chemisty', 5, 15),
  ('history', 2, 12),
  ('english', 3, 17);

SELECT * FROM students JOIN audience ON students.id = audience.student_id;