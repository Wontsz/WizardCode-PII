create database jogo;
use jogo;

select * from cadastro;CREATE DATABASE IF NOT EXISTS jogo;
use jogo;

CREATE TABLE IF NOT EXISTS cadastro(
    Nome TEXT,
    Email varchar(50),
    senha TEXT,
primary key(email));


CREATE TABLE IF NOT EXISTS Ranking(
    nome varchar(30),
    email varchar (50),
    Tempo_Total varchar(30),
    FOREIGN KEY (Nome, email) REFERENCES cadastro (Nome, email) ON DELETE CASCADE ON UPDATE CASCADE);


