/*
    Observações:
        - IDs possuem AUTO_INCREMENT
        - Codes devem ser enviados na mão
*/

-- CREATE DATABASE ArudacipGame;
CREATE TABLE StartGame
(
    ID int AUTO_INCREMENT primary key,
    NomeJogador varchar(250) not null,
    StartGameTime DateTime not null
);

CREATE TABLE CaminhoJogo
(
    ID int AUTO_INCREMENT primary key,
    ID_StartGame int not null,
    CodeFase int not null,
    FaseStartTime DateTime not null
);

CREATE TABLE Fim_Jogo
(
    ID int AUTO_INCREMENT primary key,
    ID_StartGame int not null,
    EndGameTime DateTime not null
);

CREATE TABLE Fases
(
    Code int primary key,
    CorFase varchar(50) not null,
    ShapeFase varchar(50) not null,
    NomeFase varchar(250) not null,
    LabelFase varchar(20) not null,
    Texto CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL

);

CREATE TABLE FaseLigacoes
(
    ID int AUTO_INCREMENT primary key,
    CodeFaseAtual int not null,
    CodeProximaFase int not null
);

CREATE TABLE Buttons
(
    Code int primary key,
    ButtonDescription varchar(20) not null,
    CodeFase int not null
);

Create TABLE Actions
(
    ID int AUTO_INCREMENT primary key,
    CodeButton int not null,
    ActionDescription varchar(25) not null
);