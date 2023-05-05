```
create table tableA(
    id mediumint unsigned primary key auto_increment,
    sparse mediumint unsigned not null check ( 0 <= sparse <= 5000000 ),
    dense tinyint not null check ( 0 <= dense <= 9 )
);
```

```
create procedure insert_tableA(
    in count int
)
BEGIN
    declare i int default 1;
    while i <= count do
        insert into tablea(sparse, dense) values (FLOOR(RAND() * 5000001), FLOOR(RAND() * 10));
        set i=i+1;
        end while;
end;
```

![image-20230506003401852](D:\Programs\Test01\image-20230506003401852.png)
