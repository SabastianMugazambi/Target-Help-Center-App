drop table if exists wimpers;
create table wimpers (
    id integer primary key autoincrement,
    num text not null,
    name text not null,
    message text not null,
    employee text not null,
    status text not null
);
