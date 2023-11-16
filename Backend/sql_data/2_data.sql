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
('El Morro Ancient Storage', 'USA', 'Caribbean', 'San Juan', 'Calle de la Catedral Basícila', '00901', 9500000.00);


INSERT INTO racks (rname, rcapacity) VALUES
('Wood', 150),
('Nails', 150),
('Gardening', 75),
('Interior Furniture', 50),
('Plumbing', 5),
('Paint', 90),
('Power Tools', 60),
('Misc.', 200);

INSERT INTO parts (pname, pcolor, pmaterial, MSRP) VALUES
('Plywood Sheet', 'Natural', 'Wood', 29.99),
('Particle Board', 'Brown', 'Wood', 19.99),
('2x4 Lumber', 'Natural', 'Wood', 8.99),
('Oak Veneer', 'Golden', 'Wood', 49.99),
('Cedar Plank', 'Red', 'Wood', 12.99),  -- Wood
('Common Nails', 'Silver', 'Metal', 5.99),
('Finish Nails', 'Golden', 'Metal', 7.99),
('Brad Nails', 'Silver', 'Metal', 6.99),
('Roofing Nails', 'Galvanized', 'Metal', 8.99),
('Concrete Nails', 'Gray', 'Metal', 9.99), -- Nails
('Flower Seeds Mix', 'Multicolor', 'Organic', 4.99),
('Pruning Shears', 'Green', 'Metal', 12.99),
('Garden Gloves', 'Brown', 'Textile', 7.99),
('Fertilizer Granules', 'Blue', 'Chemical', 9.99),
('Hose Nozzle', 'Red', 'Plastic', 5.99),
('Plant Pots Set', 'Terracotta', 'Ceramic', 19.99), -- Gardening
('Modern Sofa', 'Gray', 'Fabric', 599.99),
('Wooden Coffee Table', 'Brown', 'Wood', 149.99),
('Leather Recliner', 'Black', 'Leather', 399.99),
('Dining Chair Set', 'White', 'Plastic', 199.99),
('Bookshelf', 'Natural', 'Wood', 299.99),
('Bedside Table', 'Espresso', 'Particle Board', 79.99),
('L-Shaped Desk', 'Walnut', 'Melamine', 249.99),  -- Interior Furniture
('Chrome Faucet', 'Chrome', 'Metal', 89.99),
('Stainless Steel Sink', 'Silver', 'Stainless Steel', 179.99),
('Toilet Bowl', 'White', 'Porcelain', 129.99),
('Plumbing Pipe Set', 'Gray', 'PVC', 49.99),
('Shower Head', 'Bronze', 'Brass', 59.99), -- Plumbing
('Interior Paint - White', 'White', 'Latex', 24.99),
('Exterior Paint - Beige', 'Beige', 'Acrylic', 29.99),
('Paint Roller Set', 'Assorted', 'Plastic', 9.99),
('Painter Tape', 'Blue', 'Paper', 4.99),  -- Paint
('Cordless Drill Kit', 'Blue', 'Plastic/Metal', 129.99),
('Circular Saw', 'Red', 'Metal/Plastic', 89.99),
('Power Screwdriver', 'Green', 'Plastic', 39.99),
('Electric Jigsaw', 'Orange', 'Metal/Plastic', 74.99),
('Angle Grinder', 'Black', 'Metal/Plastic', 99.99), -- Power tools
('Door Mat', 'Brown', 'Coir', 14.99),
('LED Light Bulb', 'White', 'Glass', 7.99),
('Smoke Detector', 'White', 'Plastic', 19.99),
('Fire Extinguisher', 'Red', 'Metal', 34.99),
('Cabinet Knob Set', 'Silver', 'Metal', 3.99),
('Picture Frame Set', 'Assorted', 'Wood', 29.99); -- Misc.


INSERT INTO supplier (sname, scountry, scity, sstreet, szipcode, sphone) VALUES
('Island Builders Supply', 'USA', 'San Juan', 'Calle del Mar Caribe', '00901', '787-523-1234'),
('Caribbean Tools Co.', 'USA', 'Aguadilla', 'Avenida del Sol Radiante', '00603', '939-423-5678'),
('Puerto Rico Hardware Emporium', 'USA', 'Ponce', 'Calle de la Luna Mágica', '00716', '787-173-9101'),
('Island Undestroyers Supply', 'USA', 'Arecibo', 'Calle de las Buenas', '00612', '787-402-9967'),
('Los Caimanes Construyentes', 'USA', 'Bayamon', 'Avenida del Sol Radiante', '00953', '939-425-1278');


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
('Isabel', 'Ramos', '00610', '787-888-5678');

-- Relational table values
-- Supplies
INSERT INTO supplies (sid, pid, stock) VALUES
-- Supplier: Island Builders Supply
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Plywood Sheet'), 100),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Particle Board'), 150),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = '2x4 Lumber'), 200),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Oak Veneer'), 50),
((SELECT sid FROM supplier WHERE sname = 'Island Builders Supply'), (SELECT pid FROM parts WHERE pname = 'Cedar Plank'), 75),

-- Supplier: Caribbean Tools Co.
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Flower Seeds Mix'), 300),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Pruning Shears'), 100),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), 150),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), 80),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Hose Nozzle'), 120),
((SELECT sid FROM supplier WHERE sname = 'Caribbean Tools Co.'), (SELECT pid FROM parts WHERE pname = 'Plant Pots Set'), 40),

-- Supplier: Puerto Rico Hardware Emporium
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Modern Sofa'), 30),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Wooden Coffee Table'), 50),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Bedside Table'), 5),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Picture Frame Set'), 75),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Cedar Plank'), 10),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), 3),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Plant Pots Set'), 5),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Electric Jigsaw'), 5),
((SELECT sid FROM supplier WHERE sname = 'Puerto Rico Hardware Emporium'), (SELECT pid FROM parts WHERE pname = 'Finish Nails'), 65),

-- Supplier: Los Caimanes Construyentes
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = '2x4 Lumber'), 200),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Oak Veneer'), 50),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Cedar Plank'), 75),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Pruning Shears'), 100),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), 150),
((SELECT sid FROM supplier WHERE sname = 'Los Caimanes Construyentes'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), 80),


-- Supplier: Island Undestroyers Supply
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), 150),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), 80),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Hose Nozzle'), 120),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Electric Jigsaw'), 5),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Finish Nails'), 65),
((SELECT sid FROM supplier WHERE sname = 'Island Undestroyers Supply'), (SELECT pid FROM parts WHERE pname = 'Plant Pots Set'), 40);


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
('Jean', 'Castro', 'jean', 'jean@email.com', 'jeanpass654', (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'));


-- Transactions
INSERT INTO transactions (tdate, part_amount, pid, uid, wid) VALUES
('2023-11-14', 5, (SELECT pid FROM parts WHERE pname = 'Plywood Sheet'), (SELECT uid FROM users WHERE uemail = 'sofia@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2023-11-15', 3, (SELECT pid FROM parts WHERE pname = 'Modern Sofa'), (SELECT uid FROM users WHERE uemail = 'alejandra@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('2023-11-16', 10, (SELECT pid FROM parts WHERE pname = 'Common Nails'), (SELECT uid FROM users WHERE uemail = 'carlos@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2023-11-17', 8, (SELECT pid FROM parts WHERE pname = 'LED Light Bulb'), (SELECT uid FROM users WHERE uemail = 'isabella@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center')),
('2023-11-18', 2, (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), (SELECT uid FROM users WHERE uemail = 'juan@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus')),
('2023-11-19', 15, (SELECT pid FROM parts WHERE pname = 'Angle Grinder'), (SELECT uid FROM users WHERE uemail = 'mariana@email.com'), (SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions')),
('2023-11-20', 4, (SELECT pid FROM parts WHERE pname = 'Smoke Detector'), (SELECT uid FROM users WHERE uemail = 'sebastian@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2023-11-21', 7, (SELECT pid FROM parts WHERE pname = 'Fire Extinguisher'), (SELECT uid FROM users WHERE uemail = 'daniel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2023-11-22', 1, (SELECT pid FROM parts WHERE pname = 'Smoke Detector'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2023-11-23', 11, (SELECT pid FROM parts WHERE pname = 'Common Nails'), (SELECT uid FROM users WHERE uemail = 'jean@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2023-11-24', 11, (SELECT pid FROM parts WHERE pname = 'Roofing Nails'), (SELECT uid FROM users WHERE uemail = 'jean@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage')),
('2023-11-25', 1, (SELECT pid FROM parts WHERE pname = 'Smoke Detector'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution')),
('2023-11-26', 1, (SELECT pid FROM parts WHERE pname = 'Smoke Detector'), (SELECT uid FROM users WHERE uemail = 'yadiel@email.com'), (SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution'));
-- Outgoing Transactions
INSERT INTO outgoing_transaction (unit_sale_price, cid, tid) VALUES
(49.99, (SELECT cid FROM customer WHERE cphone = '787-213-1234'), (SELECT tid FROM transactions WHERE tdate = '2023-11-14')),
(299.99, (SELECT cid FROM customer WHERE cphone = '939-534-5678'), (SELECT tid FROM transactions WHERE tdate = '2023-11-15')),
(5.99, (SELECT cid FROM customer WHERE cphone = '787-632-2345'), (SELECT tid FROM transactions WHERE tdate = '2023-11-16')),
(7.99, (SELECT cid FROM customer WHERE cphone = '939-645-6789'), (SELECT tid FROM transactions WHERE tdate = '2023-11-17')),
(12.99, (SELECT cid FROM customer WHERE cphone = '787-133-3456'), (SELECT tid FROM transactions WHERE tdate = '2023-11-18')),
(7.99, (SELECT cid FROM customer WHERE cphone = '939-222-7890'), (SELECT tid FROM transactions WHERE tdate = '2023-11-19')),
(34.99, (SELECT cid FROM customer WHERE cphone = '787-432-4567'), (SELECT tid FROM transactions WHERE tdate = '2023-11-14')),
(19.99, (SELECT cid FROM customer WHERE cphone = '787-876-5678'), (SELECT tid FROM transactions WHERE tdate = '2023-11-15')),
(3.99, (SELECT cid FROM customer WHERE cphone = '939-987-8901'), (SELECT tid FROM transactions WHERE tdate = '2023-11-16')),
(14.99, (SELECT cid FROM customer WHERE cphone = '787-765-1234'), (SELECT tid FROM transactions WHERE tdate = '2023-11-17')),
(9.99, (SELECT cid FROM customer WHERE cphone = '939-654-2345'), (SELECT tid FROM transactions WHERE tdate = '2023-11-18')),
(29.99, (SELECT cid FROM customer WHERE cphone = '787-888-5678'), (SELECT tid FROM transactions WHERE tdate = '2023-11-19')),
(9.99, (SELECT cid FROM customer WHERE cphone = '939-654-2345'), (SELECT tid FROM transactions WHERE tdate = '2023-11-25')),
(29.99, (SELECT cid FROM customer WHERE cphone = '787-888-5678'), (SELECT tid FROM transactions WHERE tdate = '2023-11-26'));
-- Incoming Transactions
INSERT INTO incoming_transaction (unit_buy_price, sid, rid, tid) VALUES
(39.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Wood'), (SELECT tid FROM transactions WHERE tdate = '2023-11-14')),
(2.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Nails'), (SELECT tid FROM transactions WHERE tdate = '2023-11-15')),
(7.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Gardening'), (SELECT tid FROM transactions WHERE tdate = '2023-11-16')),
(12.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Paint'), (SELECT tid FROM transactions WHERE tdate = '2023-11-19')),
(8.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Power Tools'), (SELECT tid FROM transactions WHERE tdate = '2023-11-14')),
(24.99, (SELECT sid FROM supplier WHERE sphone = '787-173-9101'), (SELECT rid FROM racks WHERE rname = 'Misc.'), (SELECT tid FROM transactions WHERE tdate = '2023-11-15')),
(5.99, (SELECT sid FROM supplier WHERE sphone = '787-523-1234'), (SELECT rid FROM racks WHERE rname = 'Gardening'), (SELECT tid FROM transactions WHERE tdate = '2023-11-18')),
(29.99, (SELECT sid FROM supplier WHERE sphone = '939-423-5678'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture'), (SELECT tid FROM transactions WHERE tdate = '2023-11-19'));

-- Transfers
INSERT INTO transfer (to_warehouse, user_requester, tid) VALUES
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT uid FROM users WHERE username = 'carlosh'), (SELECT tid FROM transactions WHERE tdate = '2023-11-14')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT uid FROM users WHERE username = 'alejandral'), (SELECT tid FROM transactions WHERE tdate = '2023-11-15')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'sofiam'), (SELECT tid FROM transactions WHERE tdate = '2023-11-16')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT uid FROM users WHERE username = 'carlosh'), (SELECT tid FROM transactions WHERE tdate = '2023-11-17')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT uid FROM users WHERE username = 'alejandral'), (SELECT tid FROM transactions WHERE tdate = '2023-11-18')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT uid FROM users WHERE username = 'sofiam'), (SELECT tid FROM transactions WHERE tdate = '2023-11-19')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'sebas'), (SELECT tid FROM transactions WHERE tdate = '2023-11-20')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'dan'), (SELECT tid FROM transactions WHERE tdate = '2023-11-21')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'yaya'), (SELECT tid FROM transactions WHERE tdate = '2023-11-22')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'jean'), (SELECT tid FROM transactions WHERE tdate = '2023-11-24')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT uid FROM users WHERE username = 'jean'), (SELECT tid FROM transactions WHERE tdate = '2023-11-23'));
-- Stored In
INSERT INTO stored_in (wid, pid, rid) VALUES
-- Wood
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Plywood Sheet'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Particle Board'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = '2x4 Lumber'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Oak Veneer'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Cedar Plank'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Plywood Sheet'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Particle Board'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = '2x4 Lumber'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Oak Veneer'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Cedar Plank'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Plywood Sheet'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Particle Board'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = '2x4 Lumber'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Oak Veneer'), (SELECT rid FROM racks WHERE rname = 'Wood')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Cedar Plank'), (SELECT rid FROM racks WHERE rname = 'Wood')),
-- Nails
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Common Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Finish Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Brad Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Roofing Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Concrete Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Common Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Finish Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Brad Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Roofing Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'El Morro Ancient Storage'), (SELECT pid FROM parts WHERE pname = 'Concrete Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Common Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Finish Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Brad Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Roofing Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Concrete Nails'), (SELECT rid FROM racks WHERE rname = 'Nails')),
-- Gardening
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Flower Seeds Mix'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Pruning Shears'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Hose Nozzle'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Flower Seeds Mix'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Pruning Shears'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Storage NonSolutions'), (SELECT pid FROM parts WHERE pname = 'Hose Nozzle'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Los Altísimos de Almacenamiento'), (SELECT pid FROM parts WHERE pname = 'Hose Nozzle'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Garden Gloves'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Fertilizer Granules'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Hose Nozzle'), (SELECT rid FROM racks WHERE rname = 'Gardening')),
-- Interior Furniture
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Modern Sofa'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Wooden Coffee Table'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Leather Recliner'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Dining Chair Set'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Bookshelf'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Bayamon Database Centers'), (SELECT pid FROM parts WHERE pname = 'Bedside Table'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Modern Sofa'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Wooden Coffee Table'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Leather Recliner'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Dining Chair Set'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Bookshelf'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Bedside Table'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'L-Shaped Desk'), (SELECT rid FROM racks WHERE rname = 'Interior Furniture')),
-- Plumbing
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Chrome Faucet'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Stainless Steel Sink'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Toilet Bowl'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Plumbing Pipe Set'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Shower Head'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Toilet Bowl'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Plumbing Pipe Set'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Shower Head'), (SELECT rid FROM racks WHERE rname = 'Plumbing')),
-- Paint
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Interior Paint - White'), (SELECT rid FROM racks WHERE rname = 'Paint')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Exterior Paint - Beige'), (SELECT rid FROM racks WHERE rname = 'Paint')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Paint Roller Set'), (SELECT rid FROM racks WHERE rname = 'Paint')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Painter Tape'), (SELECT rid FROM racks WHERE rname = 'Paint')),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Exterior Paint - Beige'), (SELECT rid FROM racks WHERE rname = 'Paint')),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Paint Roller Set'), (SELECT rid FROM racks WHERE rname = 'Paint')),
((SELECT wid FROM warehouse WHERE wname = 'Arecibo Aviation DataCenter'), (SELECT pid FROM parts WHERE pname = 'Painter Tape'), (SELECT rid FROM racks WHERE rname = 'Paint')),
-- Power Tools
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Cordless Drill Kit'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Circular Saw'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Power Screwdriver'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Electric Jigsaw'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Angle Grinder'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Cordless Drill Kit'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Circular Saw'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Power Screwdriver'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Electric Jigsaw'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Angle Grinder'), (SELECT rid FROM racks WHERE rname = 'Power Tools')),
-- Misc.
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'Door Mat'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'Aguadilla Logistics Center'), (SELECT pid FROM parts WHERE pname = 'LED Light Bulb'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Smoke Detector'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'Mayagüez Distribution Nexus'), (SELECT pid FROM parts WHERE pname = 'Fire Extinguisher'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Cabinet Knob Set'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'Fajardo Storage Solutions'), (SELECT pid FROM parts WHERE pname = 'Picture Frame Set'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution'), (SELECT pid FROM parts WHERE pname = 'Smoke Detector'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution'), (SELECT pid FROM parts WHERE pname = 'Fire Extinguisher'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution'), (SELECT pid FROM parts WHERE pname = 'Cabinet Knob Set'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'El Campo Storage Solution'), (SELECT pid FROM parts WHERE pname = 'Picture Frame Set'), (SELECT rid FROM racks WHERE rname = 'Misc.')),
((SELECT wid FROM warehouse WHERE wname = 'Las Montañas No-Aseguradoras'), (SELECT pid FROM parts WHERE pname = 'Picture Frame Set'), (SELECT rid FROM racks WHERE rname = 'Misc.'));



