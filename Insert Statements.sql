INSERT INTO students(student_id,name,major,enrollment_date) VALUES
(1,'John Doe', 'English','2020-09-02'),
(2,'Jane Doe', 'History','2021-09-05'),
(3,'Travis Scott', 'Music','2020-09-02'),
(4,'Peter Smith', 'Theatre','2022-11-12'),
(5,'Sam Burns', 'Music','2019-02-26');

INSERT INTO courses(course_id,course_name,credits) VALUES
('ThA101','Introduction to Acting',4),
('ENG102','College Composition',2),
('HIS101','World War II',4),
('HIS301','The Roman Empire',3),
('MuA101','Composition',4),
('MuA401','Modern Jazz',1);

INSERT INTO enrollments(student_id,course_id,semester,grade) VALUES
(1,'ENG102','Fall',95.00),
(1,'MuA101','Spring',80.00),
(2,'HIS101','Fall',100.00),
(2,'HIS301','Spring',100.00),
(2,'MuA401','Summer',70.00),
(3,'MuA101','Fall',100.00),
(3,'ENG102','Fall',89.00),
(3,'HIS101','Spring',90.00),
(4,'ThA101','Fall',80.00),
(4,'MuA101','Fall',100.00),
(4,'ENG102','Spring',65.00),
(5,'MuA101','Fall',40.00),
(5,'MuA101','Spring',92.00),
(5,'ENG102','Fall',70.00),
(5,'MuA401','Fall',87.00);

INSERT INTO instructors(instructor_id,name,department) VALUES
(1,'Thomas Jones','Fine Arts'),
(2,'Carroll Summers','History'),
(3,'David Connects','English'),
(4,'Matthew Murphy','Theatre Arts'),
(5,'Jackson Nelson','Music');

INSERT INTO classes(class_id,course_id,instructor_id,schedule) VALUES
(1101,'ENG102',3,'Monday, Friday'),
(1102,'ENG102',3,'Tuesday, Thursday'),
(9653,'ThA101',4,'Monday, Wednesday, Friday'),
(9654,'ThA101',1,'Monday, Tuesday, Thursday'),
(2124,'HIS101',2,'Tuesday, Thursday'),
(4115,'MuA101',1,'Wednesday, Friday'),
(4116,'MuA101',5,'Tuesday, Thursday'),
(3482,'HIS301',2,'Monday, Wednesday, Friday'),
(7654,'MuA401',5,'Friday');
