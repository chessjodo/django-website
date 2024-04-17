Topic:
Site with Newspaper style articles on conspiracy theories.

To setup the website, install the requirements from the requirements.txt file.
Run the website using "./manage.py runserver".

Functionality:
- Home Page:
  - List of articles with title, publication date, a preview of the text and
  given tags.
  - List of Authors
- Articles Page:
  - List of articles with title, publication date, a preview of the text and
  given tags.
Both the Home Page and the Articles Page can be sorted by publication date,
  alphabetically, or by views. The articles can also be filtered by a specified tag.
- Authors Page:
  - List of Authors with picture, name, number of articles written and a short
    bio
- Author Detail Page:
  - picture, name, bio and titles of articles written
- Article Detail Page:
  - Title, publication date, author, number of views, tags and the text
  - Option to post an anonymous comment with a heading and a text
  - Display of previously submitted comments


Sources:

List of Django models fields:
https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
