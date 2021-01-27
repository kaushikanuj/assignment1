create table User(username varchar(30)NOT NULL,
                  password varchar(30),
                  address varchar(50));
Select username,password,address
from User where username <> '';