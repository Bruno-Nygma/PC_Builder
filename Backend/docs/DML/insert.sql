-- 20 Form Factors (Standard consumer shapes + industrial/legacy form factors for testing)
INSERT INTO Form_factor (id_form_factor, form_factor_type) VALUES
(1, 'ATX'),
(2, 'Micro-ATX'),
(3, 'Mini-ITX'),
(4, 'E-ATX'),
(5, 'XL-ATX'),
(6, 'SSI-EEB'),
(7, 'SSI-CEB'),
(8, 'Mini-DTX'),
(9, 'Flex-ATX'),
(10, 'Thin Mini-ITX'),
(11, 'HPTX'),
(12, 'WTX'),
(13, 'AT'),
(14, 'Baby AT'),
(15, 'BTX'),
(16, 'Micro-BTX'),
(17, 'Pico-ITX'),
(18, 'Nano-ITX'),
(19, 'UTX'),
(20, 'Proprietary');

-- 20 Accounts with authentic 60-character Bcrypt hashes
INSERT INTO Account (id_account, name, surname, email, password, role) VALUES


INSERT INTO Component (id_component, price, manufacturer, model, "type") VALUES
-- CPUs (1 to 20)
(1, 149.99, 'AMD', 'Ryzen 5 5600X', 'cpu'),
(2, 229.00, 'AMD', 'Ryzen 7 5800X3D', 'cpu'),
(3, 359.50, 'AMD', 'Ryzen 9 5900X', 'cpu'),
(4, 115.00, 'AMD', 'Ryzen 5 5600G', 'cpu'),
(5, 165.00, 'AMD', 'Ryzen 7 5700X', 'cpu'),
(6, 219.00, 'AMD', 'Ryzen 5 7600X', 'cpu'),
(7, 369.99, 'AMD', 'Ryzen 7 7800X3D', 'cpu'),
(8, 529.00, 'AMD', 'Ryzen 9 7950X', 'cpu'),
(9, 249.00, 'AMD', 'Ryzen 5 9600X', 'cpu'),
(10, 359.00, 'AMD', 'Ryzen 7 9700X', 'cpu'),
(11, 99.00, 'Intel', 'Core i3-12100', 'cpu'),
(12, 135.00, 'Intel', 'Core i5-12400F', 'cpu'),
(13, 275.00, 'Intel', 'Core i5-13600K', 'cpu'),
(14, 340.00, 'Intel', 'Core i7-13700K', 'cpu'),
(15, 530.00, 'Intel', 'Core i9-14900K', 'cpu'),
(16, 260.00, 'Intel', 'Core Ultra 5 245K', 'cpu'),
(17, 390.00, 'Intel', 'Core Ultra 7 265K', 'cpu'),
(18, 589.00, 'Intel', 'Core Ultra 9 285K', 'cpu'),
(19, 85.00, 'AMD', 'Ryzen 3 4100', 'cpu'),
(20, 65.00, 'Intel', 'Processor 300', 'cpu'),

-- Motherboards (21 to 40)
(21, 119.99, 'MSI', 'B550-A PRO', 'mobo'),
(22, 169.99, 'ASUS', 'ROG STRIX B550-F GAMING', 'mobo'),
(23, 89.00, 'Gigabyte', 'B550M DS3H AC', 'mobo'),
(24, 199.99, 'ASUS', 'ROG STRIX B550-I GAMING', 'mobo'),
(25, 299.00, 'ASRock', 'X570 Taichi', 'mobo'),
(26, 199.99, 'Gigabyte', 'B650 AORUS ELITE AX', 'mobo'),
(27, 219.50, 'ASUS', 'TUF GAMING B650-PLUS', 'mobo'),
(28, 179.99, 'MSI', 'MAG B650M MORTAR WIFI', 'mobo'),
(29, 269.00, 'ASUS', 'ROG STRIX B650E-I GAMING WIFI', 'mobo'),
(30, 449.99, 'ASRock', 'X670E Taichi Carrera', 'mobo'),
(31, 109.00, 'MSI', 'PRO B760-P WIFI DDR4', 'mobo'),
(32, 239.99, 'ASUS', 'PRIME Z790-A WIFI', 'mobo'),
(33, 259.99, 'Gigabyte', 'Z790 AORUS ELITE AX', 'mobo'),
(34, 189.99, 'MSI', 'MAG B760M MORTAR WIFI DDR5', 'mobo'),
(35, 329.99, 'ASUS', 'ROG STRIX Z790-I GAMING WIFI', 'mobo'),
(36, 639.99, 'ASUS', 'ROG MAXIMUS Z890 HERO', 'mobo'),
(37, 469.00, 'MSI', 'MPG Z890 CARBON WIFI', 'mobo'),
(38, 499.99, 'Gigabyte', 'Z890 AORUS MASTER', 'mobo'),
(39, 219.99, 'ASRock', 'Z890M Pro RS WiFi', 'mobo'),
(40, 359.99, 'ASUS', 'ROG STRIX Z890-I GAMING WIFI', 'mobo'),

-- Memory (41 to 60)
(41, 39.99, 'Corsair', 'Vengeance LPX 16GB DDR4-3200', 'memory'),
(42, 45.99, 'G.Skill', 'Ripjaws V 16GB DDR4-3600', 'memory'),
(43, 69.99, 'Corsair', 'Vengeance LPX 32GB DDR4-3200', 'memory'),
(44, 78.00, 'Teamgroup', 'T-Force Vulcan Z 32GB DDR4-3600', 'memory'),
(45, 120.00, 'G.Skill', 'Trident Z Neo 32GB DDR4-3600', 'memory'),
(46, 55.00, 'Kingston', 'Fury Beast 16GB DDR4-3200', 'memory'),
(47, 89.99, 'Crucial', 'Pro 32GB DDR4-3200', 'memory'),
(48, 140.00, 'Corsair', 'Vengeance RGB Pro 64GB DDR4-3200', 'memory'),
(49, 32.00, 'Silicon Power', 'Gaming 16GB DDR4-3200', 'memory'),
(50, 72.99, 'Patriot', 'Viper Steel 32GB DDR4-3600', 'memory'),
(51, 104.99, 'Corsair', 'Vengeance 32GB DDR5-6000', 'memory'),
(52, 119.99, 'G.Skill', 'Flare X5 32GB DDR5-6000', 'memory'),
(53, 124.99, 'G.Skill', 'Trident Z5 Neo RGB 32GB DDR5-6000', 'memory'),
(54, 139.99, 'Teamgroup', 'T-Force Delta RGB 32GB DDR5-6400', 'memory'),
(55, 98.00, 'Crucial', 'Classic 32GB DDR5-5600', 'memory'),
(56, 189.99, 'Corsair', 'Vengeance RGB 64GB DDR5-6000', 'memory'),
(57, 229.99, 'G.Skill', 'Trident Z5 RGB 64GB DDR5-6400', 'memory'),
(58, 255.00, 'Teamgroup', 'T-Create Expert 64GB DDR5-6000', 'memory'),
(59, 159.99, 'Kingston', 'Fury Renegade 32GB DDR5-7200', 'memory'),
(60, 399.99, 'Corsair', 'Dominator Titanium 96GB DDR5-6000', 'memory'),

-- GPUs (61 to 80)
(61, 299.99, 'MSI', 'GeForce RTX 4060 Ventus 2X', 'gpu'),
(62, 389.99, 'ASUS', 'Dual GeForce RTX 4060 Ti 8GB', 'gpu'),
(63, 599.99, 'Gigabyte', 'GeForce RTX 4070 Super EAGLE', 'gpu'),
(64, 799.00, 'ASUS', 'TUF Gaming GeForce RTX 4070 Ti Super', 'gpu'),
(65, 999.99, 'MSI', 'GeForce RTX 4080 Super Expert', 'gpu'),
(66, 1699.00, 'ASUS', 'ROG Strix GeForce RTX 4090 OC', 'gpu'),
(67, 269.99, 'Sapphire', 'Pulse Radeon RX 7600 XT', 'gpu'),
(68, 419.99, 'XFX', 'Speedster QICK 319 RX 7700 XT', 'gpu'),
(69, 499.99, 'PowerColor', 'Hellhound Radeon RX 7800 XT', 'gpu'),
(70, 699.99, 'Sapphire', 'NITRO+ Radeon RX 7900 XT', 'gpu'),
(71, 949.99, 'XFX', 'Speedster MERC 310 RX 7900 XTX', 'gpu'),
(72, 199.99, 'Intel', 'Arc A750 Limited Edition', 'gpu'),
(73, 289.00, 'Acer', 'Predator BiFrost Arc A770', 'gpu'),
(74, 210.00, 'Zotac', 'Gaming GeForce RTX 3060 12GB', 'gpu'),
(75, 340.00, 'MSI', 'GeForce RTX 3070 Ventus 3X', 'gpu'),
(76, 520.00, 'EVGA', 'GeForce RTX 3080 FTW3 Ultra', 'gpu'),
(77, 189.99, 'Gigabyte', 'Radeon RX 6600 Eagle', 'gpu'),
(78, 319.99, 'XFX', 'Speedster SWFT 309 RX 6700 XT', 'gpu'),
(79, 79.99, 'ASUS', 'GeForce GT 1030 2GB', 'gpu'),
(80, 1399.00, 'PNY', 'NVIDIA RTX A4000 Workstation', 'gpu'),

-- Storage (81 to 100)
(81, 84.99, 'Samsung', '980 Pro 1TB M.2 NVMe', 'storage'),
(82, 149.99, 'Samsung', '990 Pro 2TB M.2 NVMe', 'storage'),
(83, 310.00, 'Samsung', '990 Pro 4TB M.2 NVMe', 'storage'),
(84, 69.99, 'Crucial', 'P3 Plus 1TB M.2 NVMe', 'storage'),
(85, 114.99, 'Crucial', 'T500 2TB M.2 NVMe', 'storage'),
(86, 269.99, 'Crucial', 'T700 Gen5 2TB M.2 NVMe', 'storage'),
(87, 79.99, 'WD', 'Black SN850X 1TB M.2 NVMe', 'storage'),
(88, 154.50, 'WD', 'Black SN850X 2TB M.2 NVMe', 'storage'),
(89, 59.99, 'Teamgroup', 'MP33 1TB M.2 NVMe', 'storage'),
(90, 109.99, 'Silicon Power', 'UD90 2TB M.2 NVMe', 'storage'),
(91, 64.99, 'Samsung', '870 EVO 500GB 2.5 SATA', 'storage'),
(92, 99.99, 'Samsung', '870 EVO 1TB 2.5 SATA', 'storage'),
(93, 179.99, 'Samsung', '870 EVO 2TB 2.5 SATA', 'storage'),
(94, 52.00, 'Crucial', 'BX500 1TB 2.5 SATA', 'storage'),
(95, 94.00, 'Crucial', 'MX500 2TB 2.5 SATA', 'storage'),
(96, 62.99, 'Seagate', 'Barracuda 2TB 3.5 HDD', 'storage'),
(97, 109.99, 'WD', 'Blue 4TB 3.5 HDD', 'storage'),
(98, 219.00, 'Seagate', 'IronWolf Pro 8TB NAS HDD', 'storage'),
(99, 349.99, 'WD', 'Red Pro 14TB Enterprise HDD', 'storage'),
(100, 39.99, 'Kingston', 'A400 480GB 2.5 SATA', 'storage'),

-- PSUs (101 to 120)
(101, 79.99, 'Corsair', 'CX650M 650W Bronze', 'psu'),
(102, 119.99, 'Corsair', 'RM750e 750W Gold ATX 3.0', 'psu'),
(103, 139.99, 'Corsair', 'RM850x 850W Gold Shift', 'psu'),
(104, 189.99, 'Corsair', 'RM1000x 1000W Gold', 'psu'),
(105, 289.99, 'Corsair', 'AX1600i 1600W Titanium', 'psu'),
(106, 99.99, 'Seasonic', 'Focus GX-650W Gold', 'psu'),
(107, 129.50, 'Seasonic', 'Focus GX-750W Gold ATX 3.0', 'psu'),
(108, 159.99, 'Seasonic', 'Focus GX-850W Gold ATX 3.0', 'psu'),
(109, 219.99, 'Seasonic', 'Vertex GX-1000W Gold ATX 3.0', 'psu'),
(110, 320.00, 'Seasonic', 'Prime TX-1300W Titanium', 'psu'),
(111, 89.99, 'EVGA', 'SuperNOVA 650 G6 Gold', 'psu'),
(112, 114.99, 'EVGA', 'SuperNOVA 750 GT Gold', 'psu'),
(113, 144.99, 'EVGA', 'SuperNOVA 850 G7 Gold', 'psu'),
(114, 105.00, 'Thermaltake', 'Toughpower GF1 750W Gold', 'psu'),
(115, 129.99, 'Thermaltake', 'Toughpower GF3 850W ATX 3.0', 'psu'),
(116, 169.99, 'Thermaltake', 'Toughpower GF3 1000W ATX 3.0', 'psu'),
(117, 119.99, 'be quiet!', 'Pure Power 12 M 750W ATX 3.0', 'psu'),
(118, 149.99, 'be quiet!', 'Pure Power 12 M 850W ATX 3.0', 'psu'),
(119, 199.99, 'be quiet!', 'Straight Power 12 1000W ATX 3.0', 'psu'),
(120, 95.00, 'MSI', 'MAG A750GL PCIE5 750W Gold', 'psu'),

-- Cases (121 to 140)
(121, 89.99, 'Corsair', '4000D Airflow', 'tower_case'),
(122, 149.99, 'Corsair', '5000D Airflow', 'tower_case'),
(123, 79.99, 'NZXT', 'H5 Flow', 'tower_case'),
(124, 129.99, 'NZXT', 'H7 Flow', 'tower_case'),
(125, 139.99, 'Lian Li', 'PC-O11 Dynamic', 'tower_case'),
(126, 179.99, 'Lian Li', 'O11 Dynamic EVO', 'tower_case'),
(127, 99.99, 'Lian Li', 'Lancool 216', 'tower_case'),
(128, 115.00, 'Fractal Design', 'Pop Air', 'tower_case'),
(129, 144.99, 'Fractal Design', 'Meshify 2 Compact', 'tower_case'),
(130, 199.99, 'Fractal Design', 'North', 'tower_case'),
(131, 69.99, 'Phanteks', 'Eclipse G360A', 'tower_case'),
(132, 169.99, 'Phanteks', 'NV5', 'tower_case'),
(133, 84.99, 'be quiet!', 'Pure Base 500DX', 'tower_case'),
(134, 159.99, 'be quiet!', 'Shadow Base 800 DX', 'tower_case'),
(135, 59.99, 'Montech', 'AIR 903 MAX', 'tower_case'),
(136, 99.99, 'NZXT', 'H1 V2 (With PSU/Cooler)', 'tower_case'),
(137, 189.99, 'Fractal Design', 'Terra Mini-ITX', 'tower_case'),
(138, 119.99, 'Lian Li', 'A4-H2O Mini-ITX', 'tower_case'),
(139, 94.99, 'Cooler Master', 'MasterBox NR200P Mini-ITX', 'tower_case'),
(140, 49.99, 'Thermaltake', 'Versa H18 Micro-ATX', 'tower_case'),

-- Coolers (141 to 160)
(141, 35.90, 'Thermalright', 'Peerless Assassin 120 SE', 'cpu_cooler'),
(142, 37.90, 'Thermalright', 'Phantom Spirit 120 SE', 'cpu_cooler'),
(143, 19.99, 'Thermalright', 'Assassin X 120 Refined SE', 'cpu_cooler'),
(144, 44.99, 'Deepcool', 'AK400 Digital', 'cpu_cooler'),
(145, 74.99, 'Deepcool', 'AK620', 'cpu_cooler'),
(146, 119.95, 'Noctua', 'NH-D15 Chromax.Black', 'cpu_cooler'),
(147, 54.95, 'Noctua', 'NH-U12S Redux', 'cpu_cooler'),
(148, 69.95, 'Noctua', 'NH-L9i Chromax.Black SFF', 'cpu_cooler'),
(149, 49.99, 'be quiet!', 'Pure Rock 2 FX', 'cpu_cooler'),
(150, 99.90, 'be quiet!', 'Dark Rock Pro 5', 'cpu_cooler'),
(151, 89.99, 'Arctic', 'Liquid Freezer III 240 AIO', 'cpu_cooler'),
(152, 114.99, 'Arctic', 'Liquid Freezer III 360 AIO', 'cpu_cooler'),
(153, 124.99, 'Arctic', 'Liquid Freezer III 420 AIO', 'cpu_cooler'),
(154, 139.99, 'Corsair', 'iCUE H100i Elite Capellix XT', 'cpu_cooler'),
(155, 179.99, 'Corsair', 'iCUE H150i Elite Capellix XT', 'cpu_cooler'),
(156, 119.99, 'NZXT', 'Kraken 240 AIO', 'cpu_cooler'),
(157, 219.99, 'NZXT', 'Kraken Elite 360 RGB', 'cpu_cooler'),
(158, 84.99, 'Deepcool', 'LS720 SE 360mm AIO', 'cpu_cooler'),
(159, 134.99, 'Lian Li', 'Galahad II Trinity 360', 'cpu_cooler'),
(160, 9.99, 'Intel', 'Laminar RM1 Stock Cooler', 'cpu_cooler');

-- 20 CPUs
INSERT INTO Cpu (id_component, clock, integrated_graphics, tdp, socket) VALUES
(1, '3.7 GHz', false, 65, 'AM4'),
(2, '3.4 GHz', false, 105, 'AM4'),
(3, '3.7 GHz', false, 105, 'AM4'),
(4, '3.9 GHz', true, 65, 'AM4'),
(5, '3.4 GHz', false, 65, 'AM4'),
(6, '4.7 GHz', true, 105, 'AM5'),
(7, '4.2 GHz', true, 120, 'AM5'),
(8, '4.5 GHz', true, 170, 'AM5'),
(9, '3.9 GHz', true, 65, 'AM5'),
(10, '3.8 GHz', true, 65, 'AM5'),
(11, '3.3 GHz', true, 60, 'LGA1700'),
(12, '2.5 GHz', false, 65, 'LGA1700'),
(13, '3.5 GHz', true, 125, 'LGA1700'),
(14, '3.4 GHz', true, 125, 'LGA1700'),
(15, '3.2 GHz', true, 125, 'LGA1700'),
(16, '3.9 GHz', true, 125, 'LGA1851'),
(17, '3.9 GHz', true, 125, 'LGA1851'),
(18, '4.2 GHz', true, 125, 'LGA1851'),
(19, '3.8 GHz', false, 65, 'AM4'),
(20, '3.9 GHz', true, 46, 'LGA1700');

-- 20 Motherboards
INSERT INTO Mobo (id_component, form_factor, socket, chipset, memory_type, memory_slots, pcie_slots) VALUES
(21, 'ATX', 'AM4', 'B550', 'DDR4', 4, 4),
(22, 'ATX', 'AM4', 'B550', 'DDR4', 4, 3),
(23, 'Micro-ATX', 'AM4', 'B550', 'DDR4', 4, 2),
(24, 'Mini-ITX', 'AM4', 'B550', 'DDR4', 2, 1),
(25, 'ATX', 'AM4', 'X570', 'DDR4', 4, 4),
(26, 'ATX', 'AM5', 'B650', 'DDR5', 4, 3),
(27, 'ATX', 'AM5', 'B650', 'DDR5', 4, 4),
(28, 'Micro-ATX', 'AM5', 'B650', 'DDR5', 4, 2),
(29, 'Mini-ITX', 'AM5', 'B650E', 'DDR5', 2, 1),
(30, 'E-ATX', 'AM5', 'X670E', 'DDR5', 4, 3),
(31, 'ATX', 'LGA1700', 'B760', 'DDR4', 4, 3),
(32, 'ATX', 'LGA1700', 'Z790', 'DDR5', 4, 4),
(33, 'ATX', 'LGA1700', 'Z790', 'DDR5', 4, 3),
(34, 'Micro-ATX', 'LGA1700', 'B760', 'DDR5', 4, 2),
(35, 'Mini-ITX', 'LGA1700', 'Z790', 'DDR5', 2, 1),
(36, 'ATX', 'LGA1851', 'Z890', 'DDR5', 4, 3),
(37, 'ATX', 'LGA1851', 'Z890', 'DDR5', 4, 3),
(38, 'ATX', 'LGA1851', 'Z890', 'DDR5', 4, 3),
(39, 'Micro-ATX', 'LGA1851', 'Z890', 'DDR5', 4, 2),
(40, 'Mini-ITX', 'LGA1851', 'Z890', 'DDR5', 2, 1);

-- 20 Memory Kits (Updated with DDR generation mapped to form_factor)
INSERT INTO Memory (id_component, form_factor, speed) VALUES
(41, 'DDR4', 3200),
(42, 'DDR4', 3600),
(43, 'DDR4', 3200),
(44, 'DDR4', 3600),
(45, 'DDR4', 3600),
(46, 'DDR4', 3200),
(47, 'DDR4', 3200),
(48, 'DDR4', 3200),
(49, 'DDR4', 3200),
(50, 'DDR4', 3600),
(51, 'DDR5', 6000),
(52, 'DDR5', 6000),
(53, 'DDR5', 6000),
(54, 'DDR5', 6400),
(55, 'DDR5', 5600),
(56, 'DDR5', 6000),
(57, 'DDR5', 6400),
(58, 'DDR5', 6000),
(59, 'DDR5', 7200),
(60, 'DDR5', 6000);

-- 20 GPUs
INSERT INTO Gpu (id_component, tdp, VRAM) VALUES
(61, 115, 8), (62, 160, 8), (63, 220, 12), (64, 285, 16), (65, 320, 16),
(66, 450, 24), (67, 165, 8), (68, 245, 12), (69, 263, 16), (70, 315, 20),
(71, 355, 24), (72, 225, 8), (73, 225, 16), (74, 170, 12), (75, 220, 8),
(76, 320, 10), (77, 132, 8), (78, 230, 12), (79, 30, 2), (80, 140, 16);

-- 20 Storage Units
INSERT INTO Storage (id_component, capacity, storage_type) VALUES
(81, '1TB', 'NVMe'), (82, '2TB', 'NVMe'), (83, '4TB', 'NVMe'), (84, '1TB', 'NVMe'), (85, '2TB', 'NVMe'),
(86, '2TB', 'NVMe'), (87, '1TB', 'NVMe'), (88, '2TB', 'NVMe'), (89, '1TB', 'NVMe'), (90, '2TB', 'NVMe'),
(91, '500GB', 'SATA SSD'), (92, '1TB', 'SATA SSD'), (93, '2TB', 'SATA SSD'), (94, '1TB', 'SATA SSD'), (95, '2TB', 'SATA SSD'),
(96, '2TB', 'HDD'), (97, '4TB', 'HDD'), (98, '8TB', 'HDD'), (99, '14TB', 'HDD'), (100, '480GB', 'SATA SSD');

-- 20 Power Supplies
INSERT INTO Psu (id_component, wattage) VALUES
(101, 650), (102, 750), (103, 850), (104, 1000), (105, 1600),
(106, 650), (107, 750), (108, 850), (109, 1000), (110, 1300),
(111, 650), (112, 750), (113, 850), (114, 750), (115, 850),
(116, 1000), (117, 750), (118, 850), (119, 1000), (120, 750);

-- 20 Tower Cases
INSERT INTO Tower_case (id_component, case_type) VALUES
(121, 'Mid Tower'), (122, 'Full Tower'), (123, 'Mid Tower'), (124, 'Mid Tower'), (125, 'Mid Tower'),
(126, 'Mid Tower'), (127, 'Mid Tower'), (128, 'Mid Tower'), (129, 'Mid Tower'), (130, 'Mid Tower'),
(131, 'Mid Tower'), (132, 'Mid Tower'), (133, 'Mid Tower'), (134, 'Full Tower'), (135, 'Mid Tower'),
(136, 'Mini ITX Tower'), (137, 'Mini ITX Desktop'), (138, 'Mini ITX Desktop'), (139, 'Small Form Factor'), (140, 'Micro-ATX Mini');

-- 20 Coolers
INSERT INTO Cpu_cooler (id_component, fan_rpm, water_cooled) VALUES
(141, 1500, false), (142, 1500, false), (143, 1500, false), (144, 2000, false), (145, 1850, false),
(146, 1500, false), (147, 1700, false), (148, 2500, false), (149, 2000, false), (150, 1700, false),
(151, 1800, true),  (152, 1800, true),  (153, 1700, true),  (154, 2400, true),  (155, 2400, true),
(156, 2000, true),  (157, 2500, true),  (158, 2250, true),  (159, 2450, true),  (160, 2000, false);

INSERT INTO Compatible_with (id_component, id_form_factor) VALUES
-- ATX Mid/Full Towers typically handle ATX (1), Micro-ATX (2), Mini-ITX (3)
(121, 1), (121, 2), (121, 3), -- Corsair 4000D
(122, 1), (122, 2), (122, 3), (122, 4), -- Corsair 5000D (+ E-ATX)
(123, 1), (123, 2), (123, 3), -- NZXT H5
(124, 1), (124, 2), (124, 3), -- NZXT H7
(125, 1), (125, 2), (125, 3), -- O11 Dynamic
(126, 1), (126, 2), (126, 3), (126, 4), -- O11D Evo
(127, 1), (127, 2), (127, 3), -- Lancool 216
(128, 1), (128, 2), (128, 3), -- Pop Air
(129, 1), (129, 2), (129, 3), -- Meshify 2
(130, 1), (130, 2), (130, 3), -- Fractal North
(131, 1), (131, 2), (131, 3), -- Phanteks G360A
(132, 1), (132, 2), (132, 3), -- Phanteks NV5
(133, 1), (133, 2), (133, 3), -- Pure Base 500DX
(134, 1), (134, 2), (134, 3), (134, 4), (134, 5), -- Shadow Base 800 (+XL-ATX)
(135, 1), (135, 2), (135, 3), (135, 4), -- Air 903
-- SFF Cases that ONLY fit Mini-ITX (3) and Mini-DTX (8)
(136, 3), (137, 3), (138, 3), (139, 3), (139, 8),
-- Micro-ATX Case fitting Micro-ATX (2) and Mini-ITX (3)
(140, 2), (140, 3);

-- 20 Builds
INSERT INTO Build (id_build, id_account, price) VALUES
(1, 1, 2500.00), (2, 2, 1850.00), (3, 3, 3200.00), (4, 4, 850.00), (5, 5, 1200.00),
(6, 6, 1450.00), (7, 7, 999.00), (8, 8, 650.00), (9, 9, 2100.00), (10, 10, 1600.00),
(11, 11, 4100.00), (12, 12, 1350.00), (13, 13, 2800.00), (14, 14, 1100.00), (15, 15, 3400.00),
(16, 16, 2300.00), (17, 17, 1750.00), (18, 18, 1900.00), (19, 19, 1250.00), (20, 20, 500.00);

-- Junction Mappings mapping hardware components to builds (45 structural test connections)
INSERT INTO Includes (id_build, id_component) VALUES
-- Build 1: High End AM5 Setup (Fully Compatible)
(1, 7),   -- Ryzen 7 7800X3D
(1, 26),  -- B650 AORUS ELITE AX (ATX)
(1, 53),  -- DDR5 RAM
(1, 65),  -- RTX 4080 Super
(1, 104), -- 1000W PSU
(1, 121), -- 4000D Case

-- Build 2: Intel Core i5 Configuration (Fully Compatible)
(2, 13),  -- Core i5-13600K
(2, 32),  -- Z790 Motherboard
(2, 51),  -- DDR5 RAM
(2, 63),  -- RTX 4070 Super

-- Build 3: Core Ultra 9 Flagship (Fully Compatible)
(3, 18),  -- Core Ultra 9 285K
(3, 36),  -- Z890 Hero
(3, 57),  -- 64GB DDR5
(3, 66),  -- RTX 4090

-- Build 4: Budget AM4 System (Fully Compatible)
(4, 1),   -- Ryzen 5 5600X
(4, 21),  -- B550-A Pro
(4, 41),  -- 16GB DDR4 RAM
(4, 61),  -- RTX 4060

-- Build 5: Error Test Build (INTENTIONAL MISMATCHES)
-- Errors: AM4 CPU placed inside AM5 Motherboard, combining DDR5 Memory onto DDR4 board constraints.
(5, 2),   -- Ryzen 7 5800X3D (AM4 Socket)
(5, 26),  -- B650 AORUS Motherboard (AM5 Socket / DDR5)
(5, 42),  -- Ripjaws V DDR4 RAM

-- Build 6 to 20 straight-link components mapping targets for baseline data volume assertions
(6, 6), (6, 27), (6, 52), (6, 64),
(7, 3), (7, 25), (7, 45), (7, 68),
(8, 12), (8, 31), (8, 46), (8, 77),
(9, 14), (9, 33), (9, 54), (9, 70),
(10, 8), (10, 30), (10, 56), (10, 71),
(11, 15), (11, 35), (11, 60), (11, 66),
(12, 9), (12, 28), (12, 55), (12, 67),
(13, 17), (13, 37), (13, 59), (13, 65),
(14, 4), (14, 23), (14, 43), (14, 72),
(15, 10), (15, 29), (15, 58), (15, 66),
(16, 16), (16, 38), (16, 51), (16, 64),
(17, 5), (17, 22), (17, 44), (17, 69),
(18, 13), (18, 34), (18, 52), (18, 63),
(19, 11), (19, 31), (19, 47), (19, 62),
(20, 19), (20, 23), (20, 49), (20, 79);