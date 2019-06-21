# Worl2ITM-coordinates
convert world coordinates to ITM ("New Israel Net") and vice versa 
This code includes a function that analitically converts world coordinates (lng, lat)  to ITM coordinates (x, y) 
and another function, that iteratively (using the first function) converts ITM to world coordinates.
Notes: the accuracy is far from perfect, with about 20 meters error in Haifa, for example. Good enough for my purposes. You are welcome to use if this accuracy is good enough for you as well.
       Accuracy increases as you get closer to x0,y0 which is a bit south-east from Jerusalem

The analytic calculation is based on this file (found on the web):
https://www.mapi.gov.il//productcatalog/documents/פרמטרי%20התמרה,%20הסברים%20ונוסחאות.pdf
