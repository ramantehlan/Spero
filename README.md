<p align="center">
    <img src="https://ramantehlan.github.io/Spero/app/static/img/sperolo.png" >
</p>

# Welcome to Project Spero
**Spero** is an open source decentralized job marketplace for refugees, asylums, NGOs and governments. we leverage blockchain and artificial intelligence to connected about 65.6 million refugees to jobs around the world. This project was created in December 2017 for the biggest [**Global Virtual GovHack**](http://hackathon.govtechprize.ae/) hackathon organized by **UAE Government** in 2017.

Here are some problems which were tackled while creating Spero.

**Not all refugees are educated or have a mobile/computer, can still they use Spero?**

* Refugees can register themselves or through other asylums, NGOs and governments, they can also ask the experienced or educated refugees to register them.

**Employers often lack trusts in a refugee's legal status, qualification, experience, language skills, the list goes on, how can Spero tackle that? Also how you ensure and protects the rights and fair treatment of refugees?**
 
* Each refugee has to register before he can access jobs, his experience is stored in his public blockchain which validates his experience, qualification and identity. 
* He can report an employer and each refugee is asked to give ratings to employers, ratings and reports are used as metrics to give points to employers.
*  points can be later exchanged for discounts and gifts from our sponsors. it encourages employers to treat refugees positively and also allows government bodies or private-sector sponsors to contribute to refugee resettlement.

**what about the distressed and depressed refugees?**

* An in-app AI assistant,"Amica", is also there to help and motivate all the refugees to start a new life by navigating available career options and resources independently. it also gives tips to manage distress and reminders for completing job applications. 
* It is of Latin origin, and the meaning of Amica is "loved friend". In Italian "amica" means "friend".

**How is spero secure, reliable and accessible?**

* Spero use IPFS and Smart contracts.
* Posted jobs by employers are stored using IPFS to ensure the identity of the information. whereas refugee identity, application of jobs, employer points, ratings are all stored using Ethereum smart contract to ensure that the information is tamper-proof.

**Why is the meaning of Spero?**

* Spero means "I Hope" in Italian.
* It is also a part of Latin proverb: Dum Spiro Spero (While I Breathe, I Hope)


## Design
*This is the first design/prototype which was created for Spero, the current design might differ from it.*
     
<p align="center">
       <img src="https://ramantehlan.github.io/Spero/app/static/Design/WelcomePage.png" width="500" border="5">
</p>
<p>
<img src="https://ramantehlan.github.io/Spero/app/static/Design/Register.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/EmployerRegister.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/LoginPage.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/DashboardPage.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/ProfilePage.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/PostJobsPage.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/SearchPage.png" width="430" border="5">
<img src="https://ramantehlan.github.io/Spero/app/static/Design/SettingsPage.png" width="430" border="5">
</p>



## Demo Video
*This is the final submission video for [**Global Virtual GovHack**](http://hackathon.govtechprize.ae/) hackathon.*

<a href="https://www.youtube.com/watch?v=OQjC_p12kL0" target="blank"><img src="https://image.ibb.co/nBZHSG/pict.jpg"
alt="Start Demo" width="430" border="5" /></a>

## Requirements
* python 2.7
* linux, unix, mac, windows(with attachments)
* git
* Flask
* [IPFS](https://dist.ipfs.io/#go-ipfs)

## Installation

1. **Fork** the reposistory from Github and rename to your project.

2. If working on a **local machine**, then clone the repo from your terminal.

``` bash
git clone https://github.com/ramantehlan/Spero
source setup.sh
ipfs daemon (this will be running on localhost:8080)
python app.py (this will be running on localhost:8081)
```
You can now check your localhost to see if it deployed correctly.

## File Hierarchy
```
- Project Name
   - App
      -static
      -templates
        -start.html
      - __init__.py
      - allImports.py
      - config.yaml
      - models.py             #all your database models should be created in here
      - start.py # this an example of a python file that renders a page
   - Data
       - spero.sqlite
   - Venv
   - app.py
   - create_db.py                #run this to create your database
   - setup.sh
```
Above you will find the file structure for the flask template. You will be mostly working with the app/ directory.
Some **important** files and directories.

* models.py - This file contains the database schema or the tables and columns that will be in database.
If you want to make a new table then you will add a class to this file, see the example in the models.py file.
Once you are done making changes to this file run create_db.py to make the changes in the database.

* App/ directory - This directory will contain a python module. In order for python files to be recognized they must be added to the \_\_init\_\_.py file in this directory.

* start.py - This file is a very quick example of a python file that will render a page. This file processes and renders the start.html file located under templates.


## Reading and Writing to the database

In order to read from a database you will need to make a query to get the data. You can find out more about queries at [the peewee site](http://docs.peewee-orm.com/en/latest/peewee/querying.html)
one quick example of a query would be the following:
```
query = tableName.get( condition = something )
```
This will return a python object that will have the data as attributes. You can pass this object to the html file. You can access this data by typing query.Column.

## Contribution

Feel free to add your own features or improve any current feature, any kind of help is appreciated.

The core team of this project is following:
* [Raman Tehlan](https://github.com/ramantehlan)
* [Sher Sanginov](https://github.com/sanginovs)
* [Luyao Luisa Ji](https://github.com/luluissaa)

## License

GNU General Public License v3.0

## Documentation

* [Jinja](http://jinja.pocoo.org/)
* [Peewee](http://docs.peewee-orm.com/en/latest/)
* [Git](https://git-scm.com/documentation)
* [Flask](http://flask.pocoo.org/docs/0.10/)
