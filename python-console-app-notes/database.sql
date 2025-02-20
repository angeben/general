CREATE DATABASE IF NOT EXISTS python;
use python;

CREATE TABLE users(
    id int(25) auto_increment not null,
    user_name varchar(100),
    email varchar(255) not null,
    user_password varchar(255) not null,
    user_date date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE notes(
    id int(25) auto_increment not null,
    user_id int(25) not null,
    note_title varchar(255) not null,
    note_desc MEDIUMTEXT,
    note_date date not null,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
) ENGINE=InnoDb;