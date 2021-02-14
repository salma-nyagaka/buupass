# BuuPass API

This API implements a role based access system between a House Owner and a House Nanny

### Clone the repository
    git clone -b https://github.com/salma-nyagaka/buupass
    cd into assignment

### Create a virtual environment
  `virtualenv venv`

### Activate the virtual environment
 `source venv/bin/activate`
 
### Install the dependancies
`pip3 install -r requirements.txt`

### Run the app
 `python manage.py runserver`
 

## REST API ENDPOINTS
| Request  | Endpoint |
| ------------- | ------------- |
| Owner signup  | http://127.0.0.1:8000/api/v1/signup/owner |
| Nanny signup  | http://127.0.0.1:8000/api/v1/signup/nanny |
| User login  | http://127.0.0.1:8000/api/v1/signin  |
| Create chore  | http://127.0.0.1:8000/api/v1/chores  |
| Get all chores  | http://127.0.0.1:8000/api/v1/chores  |
| Delete a chore  | http://127.0.0.1:8000/api/v1/chores/<str:pk>  |
| Get a specific chore  | http://127.0.0.1:8000/api/v1/chores/<str:pk>   |
| Update chore as owner  | http://127.0.0.1:8000/api/v1/chores/<str:pk>   |
| Update chore status  | http://127.0.0.1:8000/api/v1/chores/<str:pk>   |
