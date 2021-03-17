# MissingValues

Within the process of Data Cleaning, we face a problem with datasets that have missing values that could be not recorded or they were corrupted. 
in Data Clearning we try to replace this missing values by different methods.. Sometimes we replace with the avg or the median...etc. 

In this simple project we will try to replace missing data by using a different method which let us have more accurate results.

Here is the data that we will work on : 

 |Country     |  Age       |  Salary    | Purchased  |
 |------------|------------|------------|------------|
 |France      |44.0        |72000.0     |     No     |
 |  Spain     | 27.0       | 48000.0    |     Yes    |
 | Germany    | 30.0       | 54000.0    |      No    |
 |  Spain     |38.0        | 61000.0    |    No      |
 |Germany     | 40.0       |     NaN    |   Yes      |
 | France     | 35.0       | 58000.0    |  Yes       |
 |  Spain     |  NaN       | 52000.0    |No          |
 | France     | 48.0       | 79000.0    |  Yes       |
 |Germany     | 50.0       | 83000.0    |     No     |
 | France     | 37.0       | 67000.0    |  Yes       |
 
 if we can notice in our data is that line 18 has Nan value in Age Column. Also, in Line 16,there is Nan Value in Salary Column. 
 so How Can We Replace Missing Values with Good Way ? 
 
 The answer is : by using a method called : **Interpolation**
 
Interpolation is a technique in Python with which you can estimate unknown data points between two known data points. It is commonly used to fill missing values in a table or a dataset using the already known values.Interpolation is a technique that is also used in image processing. While expanding an image you can estimate the pixel value for a new pixel using the neighbouring pixels.

Interpolation could be linear and we can apply it by this code : 
`df.interpolate()`

Simply, Linear interpolation involves estimating a new value by connecting two adjacent known values with a straight line. 
Linear interpolation is a straight line fit between two data point 

the result of this type is: 

 |Country     |  Age       |  Salary    | Purchased  |
 |------------|------------|------------|------------|
 |France      |44.0        |72000.0     |     No     |
 |  Spain     | 27.0       | 48000.0    |     Yes    |
 | Germany    | 30.0       | 54000.0    |      No    |
 |  Spain     |38.0        | 61000.0    |    No      |
 |Germany     | 40.0       | 59500.0    |   Yes      |
 | France     | 35.0       | 58000.0    |  Yes       |
 |  Spain     |  41.5      | 52000.0    |No          |
 | France     | 48.0       | 79000.0    |  Yes       |
 |Germany     | 50.0       | 83000.0    |     No     |
 | France     | 37.0       | 67000.0    |  Yes       |

There are more that this type we also can use: 

**Polynomial interpolation** ,  Polynomial interpolation requires you to specify an order.
`df.interpolate(method='polynomial', order=2)`

**Interpolation through padding** , Interpolation through padding means copying the value just before a missing entry.
While using padding interpolation, you need to specify a limit. The limit is the maximum number of nans the method can fill consecutively.

`df.interpolate(method='pad', limit=2)`

Pandas offers a nice tutorial to get used on different interpolate methods, you can access from here : 
(https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html)























