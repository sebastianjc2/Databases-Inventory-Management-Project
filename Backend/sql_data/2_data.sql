-- Base table values
INSERT INTO warehouse (wname, wcountry, wregion, wcity, wstreet, wzipcode, wbudget) VALUES
('Aguadilla Logistics Center', 'USA', 'Caribbean', 'Aguadilla', 'Calle del Sol Esmeralda', '00603', 800000.00),
('Mayagüez Distribution Nexus', 'USA', 'Caribbean', 'Añasco', 'Avenida de la Selva Encantada', '00610', 1100000.00),
('Fajardo Storage Solutions', 'USA', 'Caribbean', 'Humacao', 'Avenida de las Olas Relucientes', '00791', 750000.00),
('Bayamon Storage NonSolutions', 'USA', 'Caribbean', 'Bayamon', 'Avenida de las Aguas Frias', '00953', 1000000.00),
('Las Montañas Aseguradoras', 'USA', 'Caribbean', 'Cayey', 'Avenida del Valle', '00736', 500000.00),
('Bayamon Database Centers', 'USA', 'Caribbean', 'Bayamon', 'Callejon de las Aguas Calientes', '00953', 100000.00),
('Arecibo Aviation DataCenter', 'USA', 'Caribbean', 'Arecibo', 'Arecibo Plazoleta de la Esquina', '00612', 750000.00),
('Las Montañas No-Aseguradoras', 'USA', 'Caribbean', 'Cayey', 'Avenida del Valle', '00736', 1000.00),
('El Campo Storage Solution', 'USA', 'Caribbean', 'Morovis', 'La Cuneta del Ocho', '00687', 450000.00),
('Los Altísimos de Almacenamiento', 'USA', 'Caribbean', 'Vega Alta', 'Calle de los Altos', '00646', 70000.00),
('El Morro Ancient Storage', 'USA', 'Caribbean', 'San Juan', 'Calle de la Catedral Basícila', '00901', 9500000.00),
('Mojo Dojo Casa House', 'USA', 'Caribbean', 'San Juan', 'Avenida no Money', '00765', 0.00),
('Mojo Dojo Casa House', 'USA', 'Caribbean', 'Mayaguez', 'Avenida no Money', '00864', 0.00),
('CRUD Scrum', 'USA', 'Caribbean', 'San Juan', '420 La Fortaleza', '00766', 2.00);


INSERT INTO racks (rname, rcapacity) VALUES
-- Power Tools
('Power Drill Rack', 50),
('Circular Saw Rack', 40),
('Screwdriver Set Rack', 30),
('Angle Grinder Rack', 25),
('Jigsaw Rack', 50),
('Tool Battery Rack', 20),
('Impact Wrench Rack', 15),
('Rotary Tool Rack', 25),
('Heat Gun Rack', 50),
('Bench Grinder Rack', 30),

-- Plumbing
('Pipe Fittings Rack', 200),
('Plunger Rack', 100),
('Pipe Wrench Rack', 70),
('Torch Kit Rack', 220),
('Pipe Cutter Rack', 350),

-- Paint
('Paintbrush Rack', 200),
('Paint Roller Rack', 300),
('Painter Tape Rack', 250),
('Spray Paint Rack', 150),
('Paint Tray Rack', 70),

-- Misc.
('Toolbox Rack', 100),
('Safety Equipment Rack', 120),
('Measuring Tools Rack', 150),
('Hardware Organizer Rack', 70),
('Cord Management Rack', 300),
('Flashlight Rack', 100),
('Tool Belt Rack', 200),
('Work Gloves Rack', 300),
('Ladder Rack', 50),
('Extension Cord Rack', 100),
('Toolbox Accessories Rack', 60),

-- Outdoor Tools
('Lawn Mower Rack', 60),
('Leaf Blower Rack', 110),
('Hedge Trimmer Rack', 100),
('Garden Hose Rack', 200),
('Wheelbarrow Rack', 55),

-- Lighting
('Ceiling Light Fixtures Rack', 600),
('Table Lamps Rack', 400),
('Floor Lamps Rack', 500),
('Wall Sconces Rack', 500),
('Outdoor Lighting Rack', 150),

-- Extra/Not connected Racks
('Left For Dead Rack', 12),
('Spaghetti Rack', 10000),
('Mood Lights Rack', 200),
('Tech Gadgets Rack', 150),
('Outdoor Adventure Rack', 180),
('Kitchen Essentials Rack', 100),
('Fitness Gear Rack', 120),
('Entertainment Center Rack', 250),
('Pet Supplies Rack', 120),
('Book Lovers Rack', 150),
('Smart Home Devices Rack', 200),
('DIY Tools Rack', 160),
('Travel Accessories Rack', 140),
('Art and Craft Supplies Rack', 130);


INSERT INTO parts (pname, pcolor, pmaterial, MSRP) VALUES
-- Power Tools
('Power Drill', 'Blue', 'Metal', 129.99),
('Circular Saw', 'Red', 'Metal', 89.99),
('Screwdriver Set', 'Green', 'Metal', 49.99),
('Angle Grinder', 'Black', 'Metal', 99.99),
('Jigsaw', 'Orange', 'Metal', 74.99),
('Tool Battery', 'Gray', 'Lithium Ion', 59.99),
('Impact Wrench', 'Yellow', 'Metal', 119.99),
('Rotary Tool', 'Silver', 'Metal', 69.99),
('Heat Gun', 'Yellow', 'Metal', 49.99),
('Bench Grinder', 'Gray', 'Metal', 79.99),

-- Plumbing
('Pipe Fittings Assortment', 'Assorted', 'Metal', 24.99),
('Plunger', 'Red', 'Rubber', 12.99),
('Pipe Wrench', 'Silver', 'Metal', 29.99),
('Torch Kit', 'Black', 'Metal', 39.99),
('Pipe Cutter', 'Blue', 'Metal', 34.99),

-- Paint
('Paintbrush Set', 'Assorted', 'Nylon', 14.99),
('Paint Roller Set', 'Assorted', 'Plastic', 9.99),
('Painters Tape', 'Blue', 'Paper', 4.99),
('Spray Paint Assortment', 'Assorted', 'Aerosol', 7.99),
('Paint Tray', 'Black', 'Plastic', 5.99),

-- Outdoor Tools
('Gas Lawn Mower', 'Green', 'Metal', 199.99),
('Cordless Leaf Blower', 'Red', 'Plastic', 89.99),
('Electric Hedge Trimmer', 'Orange', 'Metal', 59.99),
('Heavy-Duty Garden Hose', 'Black', 'Rubber', 24.99),
('Steel Wheelbarrow', 'Yellow', 'Metal', 49.99),

-- Lighting
('Modern Ceiling Light Fixture', 'Silver', 'Metal', 59.99),
('Table Lamp Set', 'Bronze', 'Metal', 39.99),
('Adjustable Floor Lamp', 'Black', 'Metal', 49.99),
('Wall Sconce Pair', 'Gold', 'Metal', 34.99),
('Outdoor Solar Lights Set', 'Stainless Steel', 'Metal', 29.99),

-- Misc.
('Toolbox', 'Red', 'Metal', 59.99),
('Safety Glasses', 'Clear', 'Plastic', 9.99),
('Measuring Tape', 'Yellow', 'Metal', 14.99),
('Hardware Organizer', 'Gray', 'Plastic', 19.99),
('Cord Organizer', 'Black', 'Plastic', 7.99),
('Flashlight', 'Black', 'Metal', 12.99),
('Tool Belt', 'Brown', 'Fabric', 15.99),
('Work Gloves', 'Brown', 'Leather', 19.99),
('Step Ladder', 'Gray', 'Metal', 39.99),
('Extension Cord', 'White', 'Copper', 12.99),
('Toolbox Accessories Kit', 'Assorted', 'Metal', 29.99),
('Mystery', 'Silver', 'Amorphous', 69.99),
('Left For Dead 2', 'Green', 'Flesh', 19.99),
('Spaghetti', 'Pasta' , 'Italian', 7.99),
('Mood Lights' , 'RGB', 'Glass', 19.99),
('Switch 2 OLED', 'Silver', 'Plastic', 399.99);


INSERT INTO supplier (sname, scountry, scity, sstreet, szipcode, sphone) VALUES
('Island Builders Supply', 'USA', 'San Juan', 'Calle del Mar Caribe', '00901', '787-523-1234'),
('Caribbean Tools Co.', 'USA', 'Aguadilla', 'Avenida del Sol Radiante', '00603', '939-423-5678'),
('Puerto Rico Hardware Emporium', 'USA', 'Ponce', 'Calle de la Luna Mágica', '00716', '787-173-9101'),
('Island Undestroyers Supply', 'USA', 'Arecibo', 'Calle de las Buenas', '00612', '787-402-9967'),
('Los Caimanes Construyentes', 'USA', 'Bayamon', 'Avenida del Sol Radiante', '00953', '939-425-1278'),
('Los Suppliers sin na', 'USA', 'Bayamon', 'Avenida del Sol Radiante', '00953', '939-132-5678'),
('Superficial Super Suppliers', 'USA', 'Fajardo', 'Bahia 710', '00646', '939-666-4321');

INSERT INTO customer (cfname, clname, czipcode, cphone) VALUES
('Luis', 'Martinez', '00610', '787-213-1234'),
('Ana', 'Rodriguez', '00603', '939-534-5678'),
('Carlos', 'Gonzalez', '00610', '787-632-2345'),
('Sofia', 'Diaz', '00603', '939-645-6789'),
('Javier', 'Rivera', '00610', '787-133-3456'),
('Maria', 'Ortiz', '00603', '939-222-7890'),
('Raul', 'Perez', '00745', '787-432-4567'),
('Elena', 'Lopez', '00791', '787-876-5678'),
('Roberto', 'Hernandez', '00610', '939-987-8901'),
('Carmen', 'Torres', '00907', '787-765-1234'),
('Pedro', 'Gomez', '00603', '939-654-2345'),
('Isabel', 'Ramos', '00610', '787-888-5678'),
('Moises', 'Robles', '00610', '999-311-5532'),
('Manuel', 'Rodriguez', '00610', '999-312-4332'),
('Sebastian', 'Estrada', '00542', '954-321-3124');

-- Relational table values
-- Supplies
INSERT INTO supplies (sid, pid, stock) VALUES
-- Supplier: Island Builders Supply
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Power Drill'), 100),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Circular Saw'), 150),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Screwdriver Set'), 200),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Angle Grinder'), 50),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Jigsaw'), 75),

-- Supplier: Caribbean Tools Co.
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Tool Battery'), 300),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Impact Wrench'), 100),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Rotary Tool'), 150),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Heat Gun'), 80),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Bench Grinder'), 120),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Pipe Fittings Assortment'), 40),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Wall Sconce Pair'), 20),

-- Supplier: Puerto Rico Hardware Emporium
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Plunger'), 30),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Pipe Wrench'), 50),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Torch Kit'), 5),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Pipe Cutter'), 75),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Paintbrush Set'), 10),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Paint Roller Set'), 3),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Painters Tape'), 5),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Spray Paint Assortment'), 5),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Heat Gun'), 65),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Adjustable Floor Lamp'), 30),


-- Supplier: Los Caimanes Construyentes
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Toolbox'), 200),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Bench Grinder'), 50),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Hardware Organizer'), 75),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Cord Organizer'), 100),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Flashlight'), 150),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Tool Belt'), 80),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Table Lamp Set'), 80),


-- Supplier: Island Undestroyers Supply
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Work Gloves'), 150),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Step Ladder'), 80),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Extension Cord'), 120),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Screwdriver Set'), 5),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Paintbrush Set'), 65),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Modern Ceiling Light Fixture'), 40),

((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Paint Tray'), 40);


-- Users
INSERT INTO users (ufname, ulname, username, uemail, upassword, wid) VALUES
('Sofía', 'Martínez', 'sofiam', 'sofia@email.com', 'securepass123', (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('Alejandra', 'López', 'alejandral', 'alejandra@email.com', 'strongpass456', (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('Carlos', 'Hernández', 'carlosh', 'carlos@email.com', 'mypassword789', (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('Isabella', 'García', 'isabellag', 'isabella@email.com', 'isapass321', (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('Juan', 'Pérez', 'juanp', 'juan@email.com', 'juanpass654', (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('Mariana', 'Rodríguez', 'marianar', 'mariana@email.com', 'maripass987', (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('Sebastian', 'Medina', 'sebas', 'sebastian@email.com', 'mypassword789', (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('Daniel', 'Lopez', 'dan', 'daniel@email.com', 'danpass321', (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('Yadiel', 'Lugo', 'yaya', 'yadiel@email.com', 'yayapass654', (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('Jean', 'Castro', 'jean', 'jean@email.com', 'jeanpass654', (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('Michael', 'Jackson', 'mj', 'michael@email.com', 'hehepass654', (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('Conejo', 'Malo', 'badbunny', 'badbunny@email.com', 'badpass654', (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('Eddie', 'Halen', 'eddie', 'eddie@email.com', 'vanpass654', (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('Yari', 'Alex', 'yarmer', 'yari@email.com', 'yari69', (SELECT wid FROM warehouse WHERE wname = 'Mojo Dojo Casa House' AND wcity = 'San Juan')),
('Juan', 'del Pueblo', 'juanpueblo', 'juanpueblo@email.com', 'juanp69', (SELECT wid FROM warehouse WHERE wname = 'CRUD Scrum')),
('Manuel', 'Rodriguez', 'mrod', 'mrod@email.com', 'mrod_upr', (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'));


-- Transactions
INSERT INTO transactions (tdate, part_amount, pid, uid, wid) VALUES
('2019-11-14', 5, (SELECT pid FROM parts WHERE pname = 'Circular Saw'), (SELECT uid FROM users WHERE uemail = 'sofia@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2023-11-15', 3, (SELECT pid FROM parts WHERE pname = 'Painters Tape'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('2022-11-16', 10, (SELECT pid FROM parts WHERE pname = 'Spray Paint Assortment'), (SELECT uid FROM users WHERE uemail = 'carlos@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2022-11-17', 8, (SELECT pid FROM parts WHERE pname = 'Toolbox'), (SELECT uid FROM users WHERE uemail = 'isabella@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2021-11-19', 15, (SELECT pid FROM parts WHERE pname = 'Step Ladder'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2021-11-20', 4, (SELECT pid FROM parts WHERE pname = 'Jigsaw'), (SELECT uid FROM users WHERE uemail = 'sebastian@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2021-11-21', 7, (SELECT pid FROM parts WHERE pname = 'Tool Belt'), (SELECT uid FROM users WHERE uemail = 'daniel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2023-11-23', 11, (SELECT pid FROM parts WHERE pname = 'Plunger'), (SELECT uid FROM users WHERE uemail = 'jean@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2023-11-25', 1, (SELECT pid FROM parts WHERE pname = 'Jigsaw'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2023-11-26', 1, (SELECT pid FROM parts WHERE pname = 'Jigsaw'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2021-08-22', 6, (SELECT pid FROM parts WHERE pname = 'Heat Gun'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2022-02-27', 8, (SELECT pid FROM parts WHERE pname = 'Circular Saw'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers')),
('2022-06-05', 3, (SELECT pid FROM parts WHERE pname = 'Cord Organizer'), (SELECT uid FROM users WHERE uemail = 'sebastian@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Las Montañas No-Aseguradoras')),
('2022-09-18', 7, (SELECT pid FROM parts WHERE pname = 'Screwdriver Set'), (SELECT uid FROM users WHERE uemail = 'sebastian@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2022-12-25', 5, (SELECT pid FROM parts WHERE pname = 'Safety Glasses'), (SELECT uid FROM users WHERE uemail = 'daniel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter')),
('2019-03-07', 12, (SELECT pid FROM parts WHERE pname = 'Pipe Wrench'), (SELECT uid FROM users WHERE uemail = 'carlos@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions')),
('2019-06-15', 2, (SELECT pid FROM parts WHERE pname = 'Extension Cord'), (SELECT uid FROM users WHERE uemail = 'carlos@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2021-09-28', 11, (SELECT pid FROM parts WHERE pname = 'Plunger'), (SELECT uid FROM users WHERE uemail = 'carlos@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Las Montañas Aseguradoras')),
('2018-12-10', 9, (SELECT pid FROM parts WHERE pname = 'Pipe Fittings Assortment'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers')),
('2020-03-22', 4, (SELECT pid FROM parts WHERE pname = 'Extension Cord'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter')),
('2022-04-12', 2, (SELECT pid FROM parts WHERE pname = 'Modern Ceiling Light Fixture'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter')),
('2022-08-10', 1, (SELECT pid FROM parts WHERE pname = 'Electric Hedge Trimmer'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter')),
('2023-04-16', 3, (SELECT pid FROM parts WHERE pname = 'Toolbox Accessories Kit'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter')),
('2023-10-07', 5, (SELECT pid FROM parts WHERE pname = 'Extension Cord'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter')),
('2017-03-24', 5, (SELECT pid FROM parts WHERE pname = 'Paint Roller Set'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento')),
('2019-12-31', 8, (SELECT pid FROM parts WHERE pname = 'Jigsaw'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2023-07-14', 6, (SELECT pid FROM parts WHERE pname = 'Power Drill'), (SELECT uid FROM users WHERE uemail = 'sebastian@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2022-09-08', 3, (SELECT pid FROM parts WHERE pname = 'Power Drill'), (SELECT uid FROM users WHERE uemail = 'jean@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2021-04-25', 8, (SELECT pid FROM parts WHERE pname = 'Safety Glasses'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('2022-12-02', 5, (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2020-10-15', 12, (SELECT pid FROM parts WHERE pname = 'Hardware Organizer'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2023-03-18', 2, (SELECT pid FROM parts WHERE pname = 'Angle Grinder'), (SELECT uid FROM users WHERE uemail = 'isabella@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('2021-12-07', 7, (SELECT pid FROM parts WHERE pname = 'Painters Tape'), (SELECT uid FROM users WHERE uemail = 'sofia@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2020-06-30', 10, (SELECT pid FROM parts WHERE pname = 'Torch Kit'), (SELECT uid FROM users WHERE uemail = 'juan@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2019-08-12', 4, (SELECT pid FROM parts WHERE pname = 'Impact Wrench'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2023-01-22', 9, (SELECT pid FROM parts WHERE pname = 'Circular Saw'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('2021-11-05', 10, (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-11-04', 10, (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-11-03', 10, (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-10-09', 9, (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT uid FROM users WHERE uemail = 'badbunny@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2000-11-08', 9, (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT uid FROM users WHERE uemail = 'michael@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-10-10', 10, (SELECT pid FROM parts WHERE pname = 'Table Lamp Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-10-16', 5, (SELECT pid FROM parts WHERE pname = 'Table Lamp Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-10-20', 15, (SELECT pid FROM parts WHERE pname = 'Table Lamp Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-10-24', 20, (SELECT pid FROM parts WHERE pname = 'Table Lamp Set'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-11-10', 6, (SELECT pid FROM parts WHERE pname = 'Adjustable Floor Lamp'), (SELECT uid FROM users WHERE uemail = 'michael@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-11-12', 8, (SELECT pid FROM parts WHERE pname = 'Adjustable Floor Lamp'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-11-14', 10, (SELECT pid FROM parts WHERE pname = 'Adjustable Floor Lamp'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-04-12', 10, (SELECT pid FROM parts WHERE pname = 'Wall Sconce Pair'), (SELECT uid FROM users WHERE uemail = 'michael@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-04-14', 12, (SELECT pid FROM parts WHERE pname = 'Wall Sconce Pair'), (SELECT uid FROM users WHERE uemail = 'eddie@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-03-24', 20, (SELECT pid FROM parts WHERE pname = 'Modern Ceiling Light Fixture'), (SELECT uid FROM users WHERE uemail = 'badbunny@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2021-10-05', 6, (SELECT pid FROM parts WHERE pname = 'Tool Battery'), (SELECT uid FROM users WHERE uemail = 'sebastian@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'));


-- Outgoing Transactions
INSERT INTO outgoing_transaction (unit_sale_price, cid, tid) VALUES
(49.99, (SELECT cid FROM customer WHERE cphone = '787-213-1234'), (SELECT tid FROM transactions WHERE tdate = '2019-12-31')),
(299.99, (SELECT cid FROM customer WHERE cphone = '939-534-5678'), (SELECT tid FROM transactions WHERE tdate = '2023-11-15')),
(5.99, (SELECT cid FROM customer WHERE cphone = '787-632-2345'), (SELECT tid FROM transactions WHERE tdate = '2022-11-16')),
(7.99, (SELECT cid FROM customer WHERE cphone = '939-645-6789'), (SELECT tid FROM transactions WHERE tdate = '2021-11-20')),
(12.99, (SELECT cid FROM customer WHERE cphone = '787-133-3456'), (SELECT tid FROM transactions WHERE tdate = '2021-11-21')),
(7.99, (SELECT cid FROM customer WHERE cphone = '939-222-7890'), (SELECT tid FROM transactions WHERE tdate = '2022-09-18')),
(34.99, (SELECT cid FROM customer WHERE cphone = '787-432-4567'), (SELECT tid FROM transactions WHERE tdate = '2019-11-14')),
(19.99, (SELECT cid FROM customer WHERE cphone = '787-876-5678'), (SELECT tid FROM transactions WHERE tdate = '2021-11-19')),
(3.99, (SELECT cid FROM customer WHERE cphone = '939-987-8901'), (SELECT tid FROM transactions WHERE tdate = '2022-12-25')),
(14.99, (SELECT cid FROM customer WHERE cphone = '787-765-1234'), (SELECT tid FROM transactions WHERE tdate = '2017-03-24')),
(9.99, (SELECT cid FROM customer WHERE cphone = '939-654-2345'), (SELECT tid FROM transactions WHERE tdate = '2019-03-07')),
(29.99, (SELECT cid FROM customer WHERE cphone = '787-888-5678'), (SELECT tid FROM transactions WHERE tdate = '2021-08-22')),
(9.99, (SELECT cid FROM customer WHERE cphone = '939-654-2345'), (SELECT tid FROM transactions WHERE tdate = '2023-11-25')),
(9.99, (SELECT cid FROM customer WHERE cphone = '939-654-2345'), (SELECT tid FROM transactions WHERE tdate = '2023-11-23')),
(29.99, (SELECT cid FROM customer WHERE cphone = '787-888-5678'), (SELECT tid FROM transactions WHERE tdate = '2023-11-26'));

-- Incoming Transactions
INSERT INTO incoming_transaction (unit_buy_price, sid, rid, tid) VALUES
(39.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Paintbrush Rack'), (SELECT tid FROM transactions WHERE tdate = '2022-06-05')),
(2.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Heat Gun Rack'), (SELECT tid FROM transactions WHERE tdate = '2019-06-15')),
(7.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Measuring Tools Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-09-28')),
(12.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Flashlight Rack'), (SELECT tid FROM transactions WHERE tdate = '2022-11-17')),
(8.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Work Gloves Rack'), (SELECT tid FROM transactions WHERE tdate = '2020-03-22')),
(24.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Toolbox Accessories Rack'), (SELECT tid FROM transactions WHERE tdate = '2018-12-10')),
(5.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Leaf Blower Rack'), (SELECT tid FROM transactions WHERE tdate = '2022-04-12')),
(29.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Ceiling Light Fixtures Rack'), (SELECT tid FROM transactions WHERE tdate = '2022-02-27')),
(51.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Leaf Blower Rack'), (SELECT tid FROM transactions WHERE tdate = '2022-08-10')),
(35.99, (SELECT sid FROM supplier WHERE sphone = '939-425-1278'), (SELECT rid FROM racks WHERE rname = 'Table Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-10-10')),
(40.99, (SELECT sid FROM supplier WHERE sphone = '939-425-1278'), (SELECT rid FROM racks WHERE rname = 'Table Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-10-16')),
(25.99, (SELECT sid FROM supplier WHERE sphone = '939-425-1278'), (SELECT rid FROM racks WHERE rname = 'Table Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-10-20')),
(16.99, (SELECT sid FROM supplier WHERE sphone = '939-425-1278'), (SELECT rid FROM racks WHERE rname = 'Table Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-10-24')),
(10.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Floor Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-11-10')),
(12.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Floor Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-11-12')),
(14.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Floor Lamps Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-11-14')),
(12.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Wall Sconces Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-04-12')),
(14.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Wall Sconces Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-04-14')),
(18.99, (SELECT sid FROM supplier WHERE sphone = '787-402-9967'), (SELECT rid FROM racks WHERE rname = 'Ceiling Light Fixtures Rack'), (SELECT tid FROM transactions WHERE tdate = '2021-03-24')),
(1.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Ceiling Light Fixtures Rack'), (SELECT tid FROM transactions WHERE tdate = '2023-10-07'));

-- Transfers
INSERT INTO transfer (to_warehouse, user_requester, tid) VALUES
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT uid FROM users WHERE username = 'carlosh'), (SELECT tid FROM transactions WHERE tdate = '2023-07-14')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT uid FROM users WHERE username = 'alejandral'), (SELECT tid FROM transactions WHERE tdate = '2022-09-08')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'sofiam'), (SELECT tid FROM transactions WHERE tdate = '2021-04-25')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT uid FROM users WHERE username = 'carlosh'), (SELECT tid FROM transactions WHERE tdate = '2022-12-02')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT uid FROM users WHERE username = 'carlosh'), (SELECT tid FROM transactions WHERE tdate = '2020-10-15')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'sofiam'), (SELECT tid FROM transactions WHERE tdate = '2023-03-18')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'sofiam'), (SELECT tid FROM transactions WHERE tdate = '2021-12-07')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'dan'), (SELECT tid FROM transactions WHERE tdate = '2020-06-30')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'yaya'), (SELECT tid FROM transactions WHERE tdate = '2019-08-12')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'yaya'), (SELECT tid FROM transactions WHERE tdate = '2023-01-22')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'jean'), (SELECT tid FROM transactions WHERE tdate = '2021-10-05')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'mj'), (SELECT tid FROM transactions WHERE tdate = '2000-11-08')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'badbunny'), (SELECT tid FROM transactions WHERE tdate = '2021-10-09')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'eddie'), (SELECT tid FROM transactions WHERE tdate = '2021-11-05')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'eddie'), (SELECT tid FROM transactions WHERE tdate = '2021-11-04')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'eddie'), (SELECT tid FROM transactions WHERE tdate = '2021-11-03'));

-- Stored In
INSERT INTO stored_in (wid, pid, rid, parts_qty) VALUES
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Power Drill'), (SELECT rid FROM racks WHERE rname = 'Power Drill Rack'), 50),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Circular Saw'), (SELECT rid FROM racks WHERE rname = 'Circular Saw Rack'), 40),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Screwdriver Set'), (SELECT rid FROM racks WHERE rname = 'Screwdriver Set Rack'), 30),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Angle Grinder'), (SELECT rid FROM racks WHERE rname = 'Angle Grinder Rack'), 25),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Outdoor Solar Lights Set'), (SELECT rid FROM racks WHERE rname = 'Outdoor Lighting Rack'), 10),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Rotary Tool'), (SELECT rid FROM racks WHERE rname = 'Rotary Tool Rack'), 25),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Heat Gun'), (SELECT rid FROM racks WHERE rname = 'Heat Gun Rack'), 20),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Bench Grinder'), (SELECT rid FROM racks WHERE rname = 'Bench Grinder Rack'), 30),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Pipe Fittings Assortment'), (SELECT rid FROM racks WHERE rname = 'Pipe Fittings Rack'), 99),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Plunger'), (SELECT rid FROM racks WHERE rname = 'Plunger Rack'), 34),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Pipe Wrench'), (SELECT rid FROM racks WHERE rname = 'Pipe Wrench Rack'), 47),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Torch Kit'), (SELECT rid FROM racks WHERE rname = 'Torch Kit Rack'), 200),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Pipe Cutter'), (SELECT rid FROM racks WHERE rname = 'Pipe Cutter Rack'), 332),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Paintbrush Set'), (SELECT rid FROM racks WHERE rname = 'Paintbrush Rack'), 40),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Paint Roller Set'), (SELECT rid FROM racks WHERE rname = 'Paint Roller Rack'), 30),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas No-Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Painters Tape'), (SELECT rid FROM racks WHERE rname = 'Painter Tape Rack'), 25),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Spray Paint Assortment'), (SELECT rid FROM racks WHERE rname = 'Spray Paint Rack'), 20),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Paint Tray'), (SELECT rid FROM racks WHERE rname = 'Paint Tray Rack'), 35),
((SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution'), (SELECT pid FROM parts WHERE pname = 'Toolbox'), (SELECT rid FROM racks WHERE rname = 'Toolbox Rack'), 50),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Safety Glasses'), (SELECT rid FROM racks WHERE rname = 'Safety Equipment Rack'), 30),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Measuring Tape'), (SELECT rid FROM racks WHERE rname = 'Measuring Tools Rack'), 25),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Gas Lawn Mower'), (SELECT rid FROM racks WHERE rname = 'Lawn Mower Rack'), 44),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Cordless Leaf Blower'), (SELECT rid FROM racks WHERE rname = 'Leaf Blower Rack'), 90),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Electric Hedge Trimmer'), (SELECT rid FROM racks WHERE rname = 'Hedge Trimmer Rack'), 90),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Heavy-Duty Garden Hose'), (SELECT rid FROM racks WHERE rname = 'Garden Hose Rack'), 90),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Steel Wheelbarrow'), (SELECT rid FROM racks WHERE rname = 'Wheelbarrow Rack'), 34),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Modern Ceiling Light Fixture'), (SELECT rid FROM racks WHERE rname = 'Ceiling Light Fixtures Rack'), 100),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Table Lamp Set'), (SELECT rid FROM racks WHERE rname = 'Table Lamps Rack'), 101),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Adjustable Floor Lamp'), (SELECT rid FROM racks WHERE rname = 'Floor Lamps Rack'), 99),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Spaghetti'), (SELECT rid FROM racks WHERE rname = 'Spaghetti Rack'), 10),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Left For Dead 2'), (SELECT rid FROM racks WHERE rname = 'Left For Dead Rack'), 1),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Mood Lights'), (SELECT rid FROM racks WHERE rname = 'Mood Lights Rack'), 13),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Wall Sconce Pair'), (SELECT rid FROM racks WHERE rname = 'Wall Sconces Rack'), 50);

