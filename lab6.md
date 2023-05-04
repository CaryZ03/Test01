## Task 1

```mysql
create table account
(
    a_name varchar(30) not null
        primary key,
    a_pass varchar(10) not null,
    check (a_pass regexp _utf8mb4'[a-zA-Z0-9]{4,10}')
);

create table book
(
    b_isbn char(12)      not null
        primary key,
    b_name varchar(30)   not null,
    b_num  int default 0 null
);

create table record
(
    r_aname varchar(30) not null,
    r_bisbn char(12)    not null,
    r_ltime date        not null,
    r_etime date        not null,
    r_rtime date        null,
    primary key (r_aname, r_bisbn),
    foreign key (r_aname) references account (a_name),
    foreign key (r_bisbn) references book (b_isbn)
);
```

### Task 1-1

```mysql
DELIMITER $$

CREATE PROCEDURE update_password(
    in user_name varchar(30),
    in password_old varchar(20),
    in password_new varchar(20),
    in action int
)
	BEGIN
	    declare user_exists int default 0;
        declare user_cursor cursor for select count(*) from account where a_name = user_name and a_pass = password_old;
        open user_cursor;
        fetch user_cursor into user_exists;
        close user_cursor;
        if user_exists = 0 then
            select false;
        elseif action = 1 then
            select true;
        elseif action = 2 then
            if password_new regexp '^[a-zA-Z0-9]{4,10}$' then
                update account set a_pass = password_new where a_name = user_name;
                select true;
            else
                select false;
            end if;
        end if;
	END$$
DELIMITER ;
```

![image-20230504174308562](D:\Programs\Test01\image-20230504174308562.png)![image-20230504174343273](D:\Programs\Test01\image-20230504174343273.png)![image-20230504174410976](D:\Programs\Test01\image-20230504174410976.png)

### Task 1-2

```mysql
DELIMITER $$

CREATE PROCEDURE borrow_book(
    in user_name varchar(30),
    in isbn varchar(12)
)
	BEGIN
	    declare num int;
        select b_num from book where b_isbn=isbn into num;
	    if not exists(select * from book where b_isbn=isbn) or num=0 or
	       not exists(select * from account where a_name=user_name) or
	       exists(select * from record where r_aname=user_name and r_bisbn=isbn and r_rtime=null) then
            select false;
        else
	        insert into record(r_aname, r_bisbn, r_ltime, r_etime, r_rtime)
	            values (user_name, isbn, curdate(), date_add(curdate(), interval 30 day), null);
	        update book set b_num=num-1 where b_isbn=isbn;
        end if;
	END$$
DELIMITER ;
```

### Task 1-3

```mysql
DELIMITER $$

CREATE PROCEDURE return_book(
    in user_name varchar(30),
    in isbn varchar(12)
)
	BEGIN
	    declare num int;
	    if not exists(select * from record where r_aname=user_name and r_bisbn=isbn) then
            select false;
        else
	        update record set r_rtime=curdate() where r_aname=user_name and r_bisbn=isbn;
	        select b_num from book where b_isbn=isbn into num;
	        update book set b_num=num+1 where b_isbn=isbn;
        end if;
	END$$
DELIMITER ;
```

### Task 1-4

```mysql
DELIMITER $$

CREATE PROCEDURE check_record(
    in user_name varchar(30)
)
	BEGIN
	    select r_aname, r_bisbn, r_etime from record where r_aname=user_name and r_rtime=null;
	END$$
DELIMITER ;
```

