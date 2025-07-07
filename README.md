# Student-Enrollment-System

## Added Django Rest Framework

## API url: /api/students

## Currently, only the Student model is exposed via the API

## Instructions on testing API
* In terminal, start the server using: `$ python manage.py runserver`
* Navigate to `http://127.0.0.1:8000/accounts/login/` and login
* You can now go to `http://127.0.0.1:8000/api/students/` to see the list of students as well as filtering and CRUD options
* What is displayed is the first 5 students in terms of 'student' id. This is because the pagination is set to 5 students per page, you can see the next 5 students in the database, by typing `?page=2` and so on.
* To filter the shown list of students, you can use the 'filters' button to only show specific entries; for 'name' and 'student' id, terms that are present in either the name or major field, or order how the list is displayed.

  *  You can filter the list for a specific 'name' or 'student' id by using the url and providing a case-sensitive field and value (`http://127.0.0.1:8000/api/students/?name=John+Doe` or `http://127.0.0.1:8000/api/students/?student=1`)
  *  You can search for a term in 'name' or 'major' of a student by using `http://127.0.0.1:8000/api/students/?search=term` such as `http://127.0.0.1:8000/api/students/?search=Doe`
  *  You can order the list by 'student' id or 'enrollment_date' using `http://127.0.0.1:8000/api/students/?ordering=-student` (student id's descending) or `http://127.0.0.1:8000/api/students/?ordering=enrollment_date` (enrollment_date ascending)
  *  You can combine filters by adding & between them :`http://127.0.0.1:8000/api/students/?ordering=enrollment_date&search=e`
  *  You can create a new student by adding their 'name', 'major', 'enrollment_date' and pressing post.
        *  The student will be added to the list with the highest number by 1.
* You can get a specific Student by adding their id after /students/ in URL: `http://127.0.0.1:8000/api/students/2/`
* At this point if you are the user that created that student, you can either put or patch an update to that student or delete that student using the buttons on the page.
* If you are not logged in as the one that created the student, you will only be able to view the details.

