## Django Rest Framework Project for Birthday Wishes

**1. Project Setup:**

* Create a virtual environment to isolate our package dependencies locally:
    * `python -m venv env`
    * `source env/bin/activate`  # On Windows use `env\Scripts\activate`
* Install dependencies: `pip install django djangorestframework`
* Create a new Django project:
    * `django-admin startproject birthday_wishes`
    * `cd birthday_wishes`
    * `cd birthday_wishes`

**2. Application Creation:**

* Create a Django app for customers: `python manage.py startapp customers`

**3. Customer Model:**

* Define a `Customer` model in `customers/models.py`

**4. Serializers:**

* Create a serializer for `Customer` in `customers/serializers.py`

**5. API Views:**

* Create a basic view for customer registration in `customers/views.py`

**6. Scheduled Task for Birthday Wishes:**

* Install `django-background-task` for background tasks.
* Create a task function in `customers/tasks.py`

* Update `settings.py` with a scheduler configuration.

**7. Running the Project:**

* Migrate the database: `python manage.py migrate`
* Start the development server: `python manage.py runserver`

**8. Using Postman:**

* Open Postman and set the base URL to `http://localhost:8000/api/`.
* Create a POST request to `customer/register/`.
* In the Body tab, select "raw" and set the data type to JSON.
* Provide the customer data in JSON format, for example:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "birthday": "1990-01-01"
}
```

**Note:** This is a basic implementation that simulates email sending. Replace the printing logic with a proper email sending library like `django-allauth-email` when integrating with real email services. 