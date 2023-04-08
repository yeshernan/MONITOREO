2create database peticioncambio;
use peticioncambio
create table formato(
proyecto varchar(100) not null,
numero varchar(10) not null,
solicitante varchar(50) not null,
fecha varchar(15) not null,
cambio_solicitud varchar(1000) not null,
analizadorcambio varchar(30) not null,
componentes_afectados varchar(70) not null,
componentes_asociados varchar(70) not null,
fecha_analisis varchar(15) not null,
valoracion_cambio varchar(1000) not null,
prioridad_cambio varchar(6) not null,
implementacion_cambio varchar(500) not null,
esfuerzo_estimado varchar(23) not null, 
fecha_equipo varchar(15) not null,
fecha_decision varchar(15) not null,
decision varchar (500) not null,
implementador_cambio  varchar (50) not null,
fecha_decambio varchar (50) not null,
fecha_envioQA varchar (15) not null, 
decisionQA varchar (50) not null,
fecha_envioCM varchar (15) not null,
comentarios varchar (50) null,
primary key ('proyecto')
foreign key ('numero')

);