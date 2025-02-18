SELECT * from world.city;

--Join
Select CountryCode,country.name,count(city.Name) as q_cityname
from world.country 
join world.city on country.Code=city.CountryCode
GROUP BY country.Name
ORDER BY q_cityname DESC;

select GovernmentForm,LifeExpectancy,Language,Name from world.country
inner join world.countrylanguage on country.code=countrylanguage.CountryCode
where GovernmentForm like '%republic%' and LifeExpectancy>70 AND IsOfficial like 'T';

select customerName,productName from classicmodels.orders
join classicmodels.customers on orders.customerNumber = customers.customerNumber
join classicmodels.orderdetails on orders.orderNumber = orderdetails.orderNumber
join classicmodels.products on orderdetails.productCode = products.productCode
where customerName like 'Atelier graphique';

select name,language,percentage as contolingue,
from world.countrylanguage
join world.country on countrylanguage.CountryCode=country.Code;