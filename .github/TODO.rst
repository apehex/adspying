####
TODO
####

******
GLOBAL
******

- [x] replace the '-' in the package name
- [x] move the wrangling scripts into the data folder
- [x] use poetry for dep management, instead of pipenv
- [x] move the scraping scripts into the data folder
- [x] keep only the modules in adspying
- [ ] move the serialized data out of the project
- [ ] save all the data in mongodb
- [ ] move relevant sections to README (workflow, overall steps)
- [ ] put all the initiation steps on a jupyter notebook
- [ ] create a dashboard in dash / bokeh
- [ ] move the referential in the python package
- [ ] init script / notebook
- [ ] verify the types with typical / typing

*******
WORFLOW
*******

- [ ] collect / update referentials
- [ ] collect / update ads
- [ ] define project
- [ ] rate & rank ads
- [ ] view the ads : select the relevant offers, refine project
- [ ] complete the data (call the sellers, correct the data errors)
- [ ] buy the perfect van !

*******************
STEPS TO VANLIFE :)
*******************

- [x] data collection
- [x] data cleaning & merging
- [x] ad scraping & alerts
- [ ] filtering & ranking tools
- [ ] project dashboard
- [ ] sharing datasets : kaggle, open datasets => loop back on gh
- [ ] contact, verification of ads
- [ ] & finally buying ! and begining a new chapter !..
- [ ] diy conversion : electricity, internet, solar, water, bedding, furniture, insulation

***************
DATA COLLECTION
***************

- [ ] replace the datasets with a download script, in the repo
- [ ] car (especially van) size (volume)
- [ ] car lifespan
- [ ] fuel costs per region (country most likely)
- [x] van mpg & emissions
- [ ] insurance prices database / scraping
- [x] van / utility list
- [ ] repairs costs
- [ ] conversion costs
- [ ] parking costs

************
ADS SCRAPING
************

- [x] referential :
  - [x] regions
  - [x] cities
  - [x] ad categories
  - [x] url formats by categories => parameters dict (cat => param => url parts)
  - [x] xpath to data
- [x] configure search : date, max price, min & max years, mileage
- [x] extract informations :
  - [x] by fixing filtering input (location, price etc)
  - [x] by scraping the html
    - [x] manufacturer
    - [ ] model
    - [x] location
    - [x] price
    - [x] mileage
    - [ ] contact
    - [x] ad age
    - [ ] ad update count
- [ ] fill the gaps by asking the seller

*********
WRANGLING
*********

- [ ] filter out the cars & trucks : keep only vans ?
- [ ] list all vans & utilities
- [ ] distance between ads:
  - [ ] identify repost of the same content
- [ ] remove the samples with 0 / NULL data
- [x] swap the mpg / lpkm confusion errors
- [ ] switch the metric / imperial measures when there's a mistake

*******
MERGING
*******

- [x] define the headers
- [ ] common units
- [ ] merge consumption / size
- [ ] merge ads with referential (complete the ad infos)
- [ ] put unrecognized ads in a separate file
