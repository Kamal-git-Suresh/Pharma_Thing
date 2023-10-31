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
      ![The login page with the top bar from base.html and a login form](/assets)
      
  
