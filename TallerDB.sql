CREATE DATABASE TallerDB;


USE TallerDB;

-- tabla Estudiantes
CREATE TABLE Estudiantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    edad INT
);

-- tabla Cursos
CREATE TABLE Cursos (
    id INT PRIMARY KEY,
    nombre_curso VARCHAR(255),
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id)
);


