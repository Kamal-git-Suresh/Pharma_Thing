# Pharma_Thing

> All the files in this repo are ment to be examples. Not the final thing

## Frontend Structure
  + HTML files should be in the templates folder
  + The frontend should have a base html file which has the top bar and other stuff common across all pages
  + All the other HTML files should extend from the base.HTML file
  + I will deal with all the extending stuff. Just design the pages
  + Base.html
    + Top bar : The name of the website and some crucial links
    + Maybe a footer section for some random info
    + Use the templates/base.html file in this repo as an example
    + For lines like this just add the html tags. dont worry about the stuff in the curly brackets
      ```
      <a href= "{{ url_for('main') }}"> Pharma Thing </a>
      ```
    + Leave this block as it is
      ```
      <div class = "content">
        {% block content %} {% endblock %}  
      </div>
      ```
    + For designing other pages
      + Use this basic structure
        ```
        {% extends "base.html" %}
        {% block content %}
          put the contents of the page in this section
        {% endblock %}
        ```
      + Check templates/homepage as an example

## Demo images
  ### Login Page
  ![alt text](https://github.com/Kamal-git-Suresh/Pharma_Thing/blob/main/Demo_Images/login_page.png "Login page")

  ### Homepage
  ![alt text](https://github.com/Kamal-git-Suresh/Pharma_Thing/blob/main/Demo_Images/homepage.png "Login page")

  ### Just the base html file
  ![alt text](https://github.com/Kamal-git-Suresh/Pharma_Thing/blob/main/Demo_Images/base_html_stuff.png "Login page")  
  + This is the base html file. Currently holds only the top bar
  + Base.html should be extended by all the other html files
  + When extended the contents of the base.html should appear on all pages
     
  
      
  
