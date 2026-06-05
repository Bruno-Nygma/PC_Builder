CREATE TABLE IF NOT EXISTS Account(
	id_account SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	surname VARCHAR(20) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(200) NOT NULL,
	role VARCHAR(20) NOT NULL DEFAULT 'user'
);
	
CREATE TABLE IF NOT EXISTS Build(
	id_build SERIAL PRIMARY KEY,
	id_account INT NOT NULL,
	price NUMERIC(7,2) NOT NULL,
	FOREIGN KEY (id_account) REFERENCES Account(id_account)
);

CREATE TABLE IF NOT EXISTS Component(
	id_component SERIAL PRIMARY KEY,
	price NUMERIC(6,2) NOT NULL,
	manufacturer VARCHAR(50) NOT NULL,
	model VARCHAR(50) NOT NULL,
	"type" VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Includes(
	id_build INT NOT NULL,
	id_component INT NOT NULL,
	number INT NOT NULL,
	FOREIGN KEY (id_build) REFERENCES Build(id_build),
	FOREIGN KEY (id_component) REFERENCES Component(id_component),
	PRIMARY KEY (id_build, id_component)
);

CREATE TABLE IF NOT EXISTS Cpu_cooler(
	id_component INT PRIMARY KEY,
	fan_rpm INT NOT NULL,
	water_cooled BOOL NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Form_factor(
	id_form_factor SERIAL PRIMARY KEY,
	type VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS Tower_case(
	id_component INT PRIMARY KEY,
	type VARCHAR(20) NOT NULL,
	max_video_card_length INT NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Compatible_with(
	id_component INT,
	id_form_factor INT,
	FOREIGN KEY (id_component) REFERENCES Tower_case(id_component),
	FOREIGN KEY (id_form_factor) REFERENCES Form_factor(id_form_factor),
	PRIMARY KEY (id_component, id_form_factor)
);

CREATE TABLE IF NOT EXISTS Psu(
	id_component INT PRIMARY KEY,
	wattage INT NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Storage(
	id_component INT PRIMARY KEY,
	capacity VARCHAR(10) NOT NULL,
	type VARCHAR(10) NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Gpu(
	id_component INT PRIMARY KEY,
	tdp INT NOT NULL,
	VRAM INT NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Memory(
	id_component INT PRIMARY KEY,
	form_factor VARCHAR(20) NOT NULL,
	speed INT NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Cpu(
	id_component INT PRIMARY KEY,
	clock VARCHAR(20) NOT NULL,
	integrated_graphics BOOL NOT NULL,
	tdp INT NOT NULL,
	socket VARCHAR(50),
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);

CREATE TABLE IF NOT EXISTS Mobo(
	id_component INT PRIMARY KEY,
	form_factor VARCHAR(20) NOT NULL,
	socket VARCHAR(10) NOT NULL,
	chipset VARCHAR(10) NOT NULL,
	memory_type VARCHAR(10) NOT NULL,
	memory_slots INT NOT NULL,
	pcie_slots INT NOT NULL,
	FOREIGN KEY (id_component) REFERENCES Component(id_component)
);