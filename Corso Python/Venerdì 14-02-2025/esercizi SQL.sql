--VIEW
create view TopCountries as
select Name,Population
from world.city
where Population>=5000000;

create view NazioneCapitaleLingua as
SELECT language as 'Lingua',country.Name as 'Nazione',city.Name as 'Capitale' from country
inner join city on country.Capital = city.ID
inner join countrylanguage on city.CountryCode = countrylanguage.CountryCode
where isOfficial LIKE 'T';

CREATE VIEW spesautenti AS
SELECT customers.customerName, SUM(payments.amount) AS total_spent
FROM classicmodels.payments
INNER JOIN classicmodels.customers ON payments.customerNumber = customers.customerNumber
GROUP BY customers.customerName;