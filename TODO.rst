####
TODO
####

******
GLOBAL
******

- [x] replace the '-' in the package name
- [ ] move the wrangling scripts into the data folder
- [ ] keep only the modules in wild
- [ ] move relevant sections to README (workflow, overall steps)

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

- [ ] stacking money
- [x] data collection
- [ ] data cleaning & merging
- [ ] ad scraping & alerts
- [ ] filtering & ranking tools
- [ ] project dashboard
- [ ] sharing datasets : kaggle, open datasets => loop back on gh
- [ ] contact, verification of ads
- [ ] & finally buying ! and begining a new chapter !..
- [ ] diy conversion : electricity, internet, solar, water, bedding, furniture, insulation

**********
COLLECTION
**********

- [ ] replace the datasets with a download script, in the repo
- [ ] car (especially van) size (volume)
- [ ] car lifespan
- [ ] fuel costs per region (country most likely)
- [x] van mpg & emissions
- [ ] insurance prices database / scraping
- [x] van / utility list
- [ ] repairs costs
- [ ] scraping leboncoin
  - [ ] referential :
    - [ ] regions
    - [ ] cities
    - [ ] ad categories
    - [ ] url formats by categories => parameters dict (cat => param => url parts)
    - [ ] xpath to data
  - [ ] configure search : date, max price, min & max years, mileage
  - [ ] extract informations :
    - [ ] by fixing filtering input (location, price etc)
    - [ ] by scraping the html
      - [ ] manufacturer
      - [ ] model
      - [ ] location
      - [ ] price
      - [ ] mileage
      - [ ] contact
- [ ] fill the gaps by asking the seller

*********
WRANGLING
*********

- [ ] filter out the cars & trucks : keep only vans
- [ ] merge data & alerts
- [ ] list all vans & utilities
- [ ] remove the samples with 0 / NULL data
- [ ] swap the mpg / lpkm confusion errors
- [ ] switch the metric / imperial measures when there's a mistake

*******
MERGING
*******

- [ ] define the headers
- [ ] common units
- [ ] merge consumption / size
- [ ] merge ads with referential (complete the ad infos)
- [ ] put unrecognized ads in a separate file

*******
DATAVIZ
*******

- [ ] plot the ad price vs most characteristics
- [ ] plot the averages / stds

******
MINING
******

- [ ] plot consumption vs emission (by fuel type)
- [ ] linear regression mpg vs emission
- [x] estimation from combustion chemistry

*************
CAR VALUATION
*************

- [ ] age & mileage
- [ ] fuel efficiency / current models
- [ ] reparation cost
- [ ] conversion cost
- [ ] equipment cost
- [ ] actual cost (price_new + all)
- [ ] fuel & electricity price
- [ ] cost at 0 & 100 000 km

*******
RANKING
*******

- [ ] normalize each column used for rating
- [ ] metric for fuel consumption
- [ ] metric for co2, co, nox, pm emissions
- [ ] metric for habitable space
- [ ] metric for mileage
- [ ] metric for the cost
- [ ] overall priority for each metric
- [ ] global rating
- [ ] rank all the potential vehicles
- [ ] rank all the ads

*******
HONESTY
*******

- [ ] compare the informations from the seller to the ref

*********
DASHBOARD
*********

- [ ] Project :
  - [ ] habitable space : min x, y, z, V
  - [ ] budget : fuel, diy, van, insurance
  - [ ] miles / months, year, total
  - [ ] priorities (relative weights) : price, space, (mile)age, 
  - [ ] ranges : consumption (from budget vs miles)
- [ ] Costs :
  - [ ] kW/h
  - [ ] diesel
  - [ ] lpg
  - [ ] insurance
- [ ] highlight ads

************
VERIFICATION
************

- [ ] mileage
- [ ] technical checkup
- [ ] papers

**************
DIY CONVERSION
**************

- [ ] cost of diy materials / tools / etc
- [ ] planning & tracking of the conversion
- [ ] satellite dish => internet connection
