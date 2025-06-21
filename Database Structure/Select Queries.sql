-- All the courses each student enrolled in
SELECT s.name, c.course_name 
	FROM students s
	JOIN enrollments e
	ON s.student_id = e.student_id
	JOIN courses c
	ON e.course_id = c.course_id;

-- Class information for classes thaught by instructor #1
SELECT c.class_id, c.course_id, c.instructor_id, i.name, c.schedule  
	FROM classes c
	LEFT JOIN instructors i 
	ON c.instructor_id = i.instructor_id
	WHERE i.instructor_id = 1;