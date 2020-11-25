# Istagram Page.
An Instagram page developed using django framework

## Author and contact details
* Dorcas Wanjiku
Email: smallwanjiku@gmail.com

# Project Description
A user of the application should be able to:

1. Sign in to the application to start using.
2. Upload their pictures to the application.
3. See their profile with all the pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.
A search functionality is implemented where one can search for the different users  and their images.

# SetUp and installation requirements
You need to have the following installed:
* Python3+
* Create the virtual environment.
* Activate the virtual environment
* pip install Django
* Get all requirements ```pip freeze > requirements.txt```

### Running the server
```python manage.py runserver```

# Behaviour Driven Development

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit the site| Various images are displayed  | User can comment and like images |
| Click on image| Image expand with details displayed | Image details displayed |
| Search user | Images for user are displayed | App gets the images for the searched user |
| Visit profile | Images posted by user are displayed | App gets images for user |
| Visit Admin | Prompts for admin credentials | Admin dashboard displayed |


## Technologies used
* python 3.8
* Django framework
* Javascript
* Html
* Bootstrap 3 & 4
* PostgreSQL

# Development
It would be so great to have your contributions! Just follow the instructions below.

Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above)
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!

## Known Bugs
The applications comments and followers are not working
One can view all images for all users in the app


## License
* [[License: MIT]](LICENSE.md)
* Copyright (c) 2020 **Dorcas Wanjiku**