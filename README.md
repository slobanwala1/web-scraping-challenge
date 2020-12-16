# Web Scraping Homework - Mission to Mars

**Data Analysis For Web Scraping Homework - Mission to Mars by Shanil Lobanwala**

## Links to files

The Jupyter Notebook file, app, and the scrape files are located in: [Missions_to_Mars](https://github.com/slobanwala1/web-scraping-challenge/tree/main/Missions_to_Mars). The HTML file is 
located in [HTML File](https://github.com/slobanwala1/web-scraping-challenge/blob/main/Missions_to_Mars/templates/index.html). The table html code example is in [Mars Facts Table](https://github.com/slobanwala1/web-scraping-challenge/tree/main/Missions_to_Mars/Resources). All the screen shots of the app are in: [Images](https://github.com/slobanwala1/web-scraping-challenge/tree/main/Images).

### Scraping Analysis:

We scrape multiple pages of the Nasa news website for Mars. We grabbed the most current news title, content, featured image, as well as facts about Mars, and the hemispheres. We compiled this data using 
BeautifulSoup and Splinter and using pandas for creating dataframes for tables as well as reading in tables. We then imported the code into Flask and created an application that would scrape the web pages
and update the app with the right information. Heres an example of a scrape on the webpage:

<br>
<br>
<img src="https://github.com/slobanwala1/web-scraping-challenge/blob/main/Images/Screenshot_1.PNG" width="681">

<br>
<br>
<img src="https://github.com/slobanwala1/web-scraping-challenge/blob/main/Images/Screenshot_2.PNG" width="681">

<br>
<br>
<img src="https://github.com/slobanwala1/web-scraping-challenge/blob/main/Images/Screenshot_3.PNG" width="681">


Thats a quick summary of the work, it was very frustrating at times, but I learned a lot out of it. Thanks for the oppurtunity to learn how to use selenium tests with Splinter to grab live data and then strip it for the correct info and finally display it in a real world application.