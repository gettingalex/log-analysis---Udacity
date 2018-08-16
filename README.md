# log-analysis---Udacity
Logs Analysis - Udacity Full Stack Nanodegree
Alexandre Deschenes ar_creation@hotmail.com


This project uses three PostgreSQL views (included under installation) integrated with Python DBAPI. The project queries the database news (not included in submission as per the instructions) for information regarding the tables articles, authors and log. The SQL queries output are reformatted into a string for clearer output. The questions are outputted above each query output.


Code Style
Python pycodestyle (a.k.a. pep8)


Tech/framework used
This project uses:
	•	Python
	•	PostgreSQL
	•	VirtualBox(Vagrant)


Installation:
In order to run this python program, you must run a virtual environment. This project was developed with VirtualBox and Vagrant. Once in the virtual environment, run the python code log_analysis.py. 

This assumes that the database is already installed and the following views were created:

View top_three (Question 1)
create view top_three as 
select format('%s %s %s %s', articles.title,'-', count(log.path), 'views') 
from log 
join articles 
on replace(log.path,'/article/','') = articles.slug 
group by articles.title 
order by count(log.path) desc 
limit 3;

View pop_authors (Question 2)
create view pop_authors as 
select format('%s %s %s %s', authors.name, '-', count(log.path), 'views') 
from articles 
join authors 
on authors.id = articles.author 
join log 
on articles.slug = replace(log.path,'/article/','') 
group by authors.name 
order by count(log.path) desc;

View error_day (Question 3)
create view error_day as 
select format('%s %s %s%% %s', to_char(s1.date, 'FMMonth FMDD, YYYY'), '-', round(s1.errors * 100.0 / s2.all_data, 2), 'errors')
from (select date(log.time) as date, count(id) as errors
	from log
	where status='404 NOT FOUND'
	group by date(log.time)) as s1
inner join (select date(log.time) as date, count(id) as all_data 
	from log 
	group by date(log.time)) s2
on s1.date = s2.date
where (s1.errors * 100.0 / s2.all_data) >= 1.0
group by s1.date, s1.errors, s2.all_data;


How to use?
1-Connect to a virtual machine
2-In the command shell, cd to the project file and execute python3 log_analysis.py
3-This will execute the three python procedures connected to the database news.
4-Each of which will send a single SQL query to the database and return a tuple, which python transforms into a list, and then into strings to print to the command line.

