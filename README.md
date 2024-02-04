# rent_check

Check average rent from different cities in the world. Thanks to [numbeo](https://www.numbeo.com/).

```
## pip install -r requirements.txt

# python rent_check.py -h
usage: rent_check.py [-h] -c CITYNAME -b {1,3} -C CITYCENTER

Find monthly rent.

options:
  -h, --help            show this help message and exit
  -c CITYNAME, --cityname CITYNAME
                        Name of the city
  -b {1,3}, --bedroom {1,3}
                        Number of bedrooms. Options are 1 or 3
  -C CITYCENTER, --citycenter CITYCENTER
                        In or outside city center. true or false
```          

For example,

```
# python rent_check.py -c potsdam -b 3 -C true
Price for Apartment (3 bedrooms) in Potsdam in City Centre: 1,733.33 €
```