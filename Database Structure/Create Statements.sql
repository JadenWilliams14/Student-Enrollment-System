CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	major VARCHAR(50),
	enrollment_date DATE
);

CREATE TABLE courses (
	course_id VARCHAR(6) PRIMARY KEY CHECK (course_id ~ '^[A-Za-z]{3}[0-9]{3}'),
	course_name VARCHAR(100),
	credits INTEGER CHECK (credits BETWEEN 1 AND 4)
);

CREATE TABLE enrollments (
	student_id INTEGER REFERENCES students(student_id),
	course_id VARCHAR(6) REFERENCES courses(course_id),
	semester VARCHAR(6),
	grade NUMERIC CHECK (grade BETWEEN 0.00 AND 100.00)
);

CREATE TABLE instructors (
	instructor_id INTEGER PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	department VARCHAR(100)
);

CREATE TABLE classes (
	class_id VARCHAR(4) PRIMARY KEY,
	course_id VARCHAR(6) REFERENCES courses(course_id),
	instructor_id INTEGER REFERENCES instructors(instructor_id),
	schedule VARCHAR(50)
);