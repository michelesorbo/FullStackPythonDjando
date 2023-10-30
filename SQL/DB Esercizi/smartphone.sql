-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2023 at 11:03 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jayasuriya`
--

-- --------------------------------------------------------

--
-- Table structure for table `numeri_telefonici`
--

CREATE TABLE `numeri_telefonici` (
  `id_numero` bigint(8) NOT NULL,
  `numero` varchar(12) NOT NULL,
  `compagnia_telefonica` varchar(252) NOT NULL,
  `id_persona` bigint(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `numeri_telefonici`
--

INSERT INTO `numeri_telefonici` (`id_numero`, `numero`, `compagnia_telefonica`, `id_persona`) VALUES
(1, '3372327469', 'VODAFONE', 1),
(2, '3902426382', 'TIM', 2),
(3, '3440543432', 'KENA MOBILE', 3),
(4, '3721213293', 'POSTE MOBILE', 4),
(5, '3814995915', 'IO', 5),
(6, '3709784288', 'TIM', 6),
(7, '3304702355', 'VODAFONE', 7),
(8, '3922038677', 'TIM', 8),
(9, '3121133132', 'TIM', 2),
(10, '3112213479', 'VODAFONE', 3),
(11, '3121138132', 'TIM', 6),
(12, '3913213479', 'TIM', 3),
(13, '3121136632', 'WIND', 6),
(14, '2113213479', 'VERY MOBILE', 5),
(15, '3944213479', 'TIM', 8),
(16, '2113299479', 'VERY MOBILE', 3);

-- --------------------------------------------------------

--
-- Table structure for table `persone`
--

CREATE TABLE `persone` (
  `id_persona` bigint(8) NOT NULL,
  `nome` varchar(252) NOT NULL,
  `cognome` varchar(252) NOT NULL,
  `data_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `persone`
--

INSERT INTO `persone` (`id_persona`, `nome`, `cognome`, `data_nascita`) VALUES
(1, 'GABRIELE', 'FORNARI', '1994-11-24'),
(2, 'FRANCESCA', 'SOPINO', '2002-07-15'),
(3, 'BEATRICE', 'PERTIS', '1990-05-27'),
(4, 'MASSIMO', 'VISCONTI', '1985-09-30'),
(5, 'SOFIA', 'DE PETRIS', '1977-01-04'),
(6, 'GIANLUCA', 'MARINO', '1980-02-05'),
(7, 'RICCARDO', 'LONZI', '2007-12-05'),
(8, 'SILVIA', 'BENEDETTI', '1999-06-13'),
(9, 'SILVIO', 'ROSSI', '1998-07-13');

-- --------------------------------------------------------

--
-- Table structure for table `smartphone`
--

CREATE TABLE `smartphone` (
  `id_smartphone` bigint(8) NOT NULL,
  `marca` varchar(252) NOT NULL,
  `modello` varchar(252) NOT NULL,
  `colore` varchar(252) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `smartphone`
--

INSERT INTO `smartphone` (`id_smartphone`, `marca`, `modello`, `colore`) VALUES
(1, 'APPLE', 'IPHONE 13', 'BIANCO'),
(2, 'OPPO', 'A9 2020', 'VERDE CROMATO\r\n'),
(3, 'SAMSUNG', 'A13', 'BIANCO\r\n'),
(4, 'OPPO', 'A54', 'BLU'),
(5, 'APPLE', 'IPHONE 12', 'BLU SCURO'),
(6, 'LG', 'VELVET 5G', 'GRIGIO'),
(7, 'MOTOROLA', 'EDGE 20', 'NERO\r\n'),
(8, 'NOKIA', 'C20', 'NERO CHIARO\r\n'),
(9, 'XIAOMI', 'REDMI NOTE 11', 'BIANCO'),
(10, 'XIAOMI', 'REDMI NOTE 12', 'BIANCO'),
(11, 'APPLE', 'IPHONE 13', 'NERO'),
(12, 'APPLE', 'IPHONE 13', 'BLU'),
(13, 'SAMSUNG', 'S20', 'BIANCO\r\n'),
(14, 'SAMSUNG', 'S20', 'BLU\r\n'),
(15, 'SAMSUNG', 'S20', 'ANTRACITE');

-- --------------------------------------------------------

--
-- Table structure for table `smartphone_posseduti`
--

CREATE TABLE `smartphone_posseduti` (
  `id_smartphone` bigint(8) NOT NULL,
  `id_persona` bigint(8) NOT NULL,
  `data_acquisto` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `smartphone_posseduti`
--

INSERT INTO `smartphone_posseduti` (`id_smartphone`, `id_persona`, `data_acquisto`) VALUES
(1, 1, '2020-07-21'),
(2, 2, '2017-03-21'),
(2, 3, '2018-03-21'),
(3, 3, '2022-05-09'),
(4, 4, '2021-11-06'),
(5, 5, '2023-01-02'),
(6, 6, '2022-12-24'),
(7, 7, '2022-12-23'),
(8, 8, '2022-08-15'),
(9, 1, '2022-08-15'),
(10, 7, '2022-04-10'),
(11, 7, '2022-03-10'),
(12, 6, '2021-03-10'),
(13, 4, '2021-02-10'),
(14, 2, '2020-12-10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `numeri_telefonici`
--
ALTER TABLE `numeri_telefonici`
  ADD PRIMARY KEY (`id_numero`),
  ADD KEY `id_persona_chiave_esterna` (`id_persona`);

--
-- Indexes for table `persone`
--
ALTER TABLE `persone`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indexes for table `smartphone`
--
ALTER TABLE `smartphone`
  ADD PRIMARY KEY (`id_smartphone`);

--
-- Indexes for table `smartphone_posseduti`
--
ALTER TABLE `smartphone_posseduti`
  ADD PRIMARY KEY (`id_smartphone`,`id_persona`),
  ADD KEY `id_persona` (`id_persona`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `numeri_telefonici`
--
ALTER TABLE `numeri_telefonici`
  MODIFY `id_numero` bigint(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `persone`
--
ALTER TABLE `persone`
  MODIFY `id_persona` bigint(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `smartphone`
--
ALTER TABLE `smartphone`
  MODIFY `id_smartphone` bigint(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `numeri_telefonici`
--
ALTER TABLE `numeri_telefonici`
  ADD CONSTRAINT `numeri_telefonici_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persone` (`id_persona`);

--
-- Constraints for table `smartphone_posseduti`
--
ALTER TABLE `smartphone_posseduti`
  ADD CONSTRAINT `smartphone_posseduti_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persone` (`id_persona`),
  ADD CONSTRAINT `smartphone_posseduti_ibfk_2` FOREIGN KEY (`id_smartphone`) REFERENCES `smartphone` (`id_smartphone`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
