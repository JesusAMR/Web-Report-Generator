CREATE DATABASE Sigma;

USE [Sigma]

CREATE TABLE usuarios(
    id_usuario INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    nombre VARCHAR(15) NOT NULL,
    ap_Paterno VARCHAR(15) NOT NULL,
    ap_Materno VARCHAR(15) NOT NULL,
    fecha_Nacimiento date NOT NULL CHECK(fecha >= GETDATE()),
    contrasena VARCHAR(20) NOT NULL
)