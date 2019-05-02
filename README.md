## Blog application

This is a great application description


## User stories

As a user, I would like to:

1. View the blog posts on the site
2. Comment on blog posts
3. View the most recent posts
4. Get an email alert when a new post is made by joining a subscription.
5. See random quotes on the site
6. Sign in to the blog.
7. Create a blog from the application.
8. Delete comments that I find insulting or degrading.
9. Update or delete blogs I have created.


## Set-up Requirements

### Prerequisites
* python3.7
* Flask 1.0
* Virtualenv


### Technologies

-Bootstrap4
-CSS3

### Cloning
* In your terminal:
        
        $ git clone https://github.com/GabrielOduori/Blog-Post
        $ cd Blog-Post

## Running the Application
* Creating the virtual environment

        $ python3 -m pip install --user virtualenv ( on a Mac)
        $ python3 -m virtualenv env
        $ source env/bin/activate
        $(For other operating systems, see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
        
* Installing Flask and other Modules
- While in the virtalenvironment install all the requirements by running 
$ pip install -r requirements.txt

        
* Setting up the quotes base url

        
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.7 manage.py tests

## Known bugs
* The comment functionality is currently not routing as expected and will be fixed in the next iteration.    
        

## License information

Bloggy Blogs is Copyright 2019 Gabriel Oduori licensed under GNU avaliable at http://www.gnu.org/licenses.

## Contact

gabriel.oduori@gmail.com
