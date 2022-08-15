# Mission-to-Mars
Web Scraping to Extract Online Data:  Tools: MongoDB, BeautifulSoup, Splinter and Flask
For this project, I used Flask web application that scrapes a website for data related to the Mars Mission and displays the information in a single HTML page.

The main goal of this project is to give more functionality to the Robin's web app. To do so, we have added images of Mars’s hemispheres by scraping the website. Robin requiered to include all four of the hemisphere images. For this project, we have used BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

# Resources 

- Data Source: Mission_to_Mars.ipynb, app.py, scraping.py and index.html
- Data Tools: Jupyter Notebook, Python and MongoDB
- Software: MongoDB, Python 3.8.3, Visual Studio Code 1.50.0, Flask Version 1.0.2

# Results

- Devliverable 1 - The full-resolution images of the hemispheres are added to the dictionary.

![hemis](https://github.com/acegal1/Mission-to-Mars/blob/main/images/hemis.png)

The components of the deliverables are as follows;
![all](https://github.com/acegal1/Mission-to-Mars/blob/main/images/all.png)



### Using Bootstrap 3 to modify the html file

- The webpage is mobile-responsive
Changed everything to col-xs, which is the smallest option. Everything will scale up from the mobile phones size to the larger desktop sizes.

Mobile View

![Mobile_400](https://github.com/acegal1/Mission-to-Mars/blob/main/images/mobile_400.png)


Two additional Bootstrap 3 components are used to style the webpag

- Changed the button(scrape new data) color and style. 

- Changed the colors of various areas, adjusted some heights, and added a striped table pattern.

![web_mars](https://github.com/acegal1/Mission-to-Mars/blob/main/images/web_mars_image.png)
