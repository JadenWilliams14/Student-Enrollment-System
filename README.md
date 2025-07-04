# Student-Enrollment-System

## CRUD implemented for Student Model

## BASE url: myapp/

## How to navigate CRUD operations:
From the Student list page, you can click on the 'Create Student' link in order to utilize the CREATE operation.
Also from the Student list page, you can click on a previously created student in order to READ that students information.
From the student_detail page, you can click on links to either UPDATE or DELETE that specific student.

## How to Set up Google OAuth:
* Go to the [Google Cloud Console](https://console.cloud.google.com/).
* Create a **New Project** or select an existing one.
* Navigate to **APIs & Services** -> **Credentials**.
* Click **Create Credentials** -> **OAuth client ID**.
* If prompted, configure the **OAuth consent screen** first:
    * Select **External** user type.
    * Fill in the required fields (App name, User support email, Developer contact information).
    * On the **Scopes** page, click **Add or Remove Scopes**. Find and add the `.../auth/userinfo.email` and `.../auth/userinfo.profile` scopes (and potentially `openid`). Click **Update**.
    * Add your email address as a **Test user** while the app is in testing status.
    * Save and continue back to credential creation.
* Select **Web application** as the Application type.
* Give it a name (e.g., "My Django App Auth").
* Under **Authorized redirect URIs**, click **Add URI** and enter:
    `http://127.0.0.1:8000/accounts/google/login/callback/`
    *(Adjust the domain and port if you are not using the default development server)*.
    *(Remember that for deployment (e.g., to AWS EC2), you will need to return to the Google Cloud Console and add your production redirect URI (e.g., `http://<your-ec2-ip>/accounts/google/login/callback/` or `https://your-domain.com/...`) to the OAuth client settings.)*
* Click **Create**. Copy the **Client ID** and **Client Secret** that appear.
* Create GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET variables in your .env file and set them equal to the copied ID and Secret.

## How to Test login:
* Go to http://127.0.0.1:8000/accounts/signup/ and either enter an email and password or use the google third-party link.
* Go to http://127.0.0.1:8000/accounts/login/ and login using that email and password. You will be redirected to student list page.


## How to Test permission restrictions:
* If you login using a regular user, you should be able to see the student list. If you click on any student, you will be able to see that student's details
* If you login using a superuser, you will be able to see the Create Student link on the student list page. If you click on a student, you will be able to see the links to the Update and Delete pages and be able to do that as necessary. You will see any students that you delete missing from the student list and any updates will reflect on the detail page.
