create table if not exists user(
  id integer primary key,
  email varchar(255) not null,
  password varchar(255) not null,
  creation_date datetime not null,
  is_active integer default 1,
  delete_date datetime null
);

create table if not exists client(
  id integer primary key,
  user_id integer references user(id),
  name varchar(255) not null,
  phone varchar(255) not null,
  address varchar(255) not null,
  zip_code varchar(255) not null,
  city varchar(255) not null,
  neighborhood varchar(255) not null,
  country varchar(255) not null,
  is_active integer default 1
);

create table if not exists book(
  id integer primary key,
  title varchar(255) not null,
  description varchar(5000) not null,
  quantity integer not null default 0
);

create table if not exists book_loan(
  id integer primary key,
  book_id integer references book(id),
  client_id integer references client(id),
  loan_date datetime not null,
  expeted_return_date datetime null,
  return_date datetime null,
  status bool not null default 0
);