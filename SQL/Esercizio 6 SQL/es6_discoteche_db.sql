-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 15, 2023 at 10:25 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `discoteche_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `discoteche`
--

CREATE TABLE `discoteche` (
  `id_discoteca` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `indirizzo` varchar(100) NOT NULL,
  `citta` varchar(50) NOT NULL,
  `telefono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `discoteche`
--

INSERT INTO `discoteche` (`id_discoteca`, `nome`, `indirizzo`, `citta`, `telefono`) VALUES
(1, 'Discoteca ABC', 'Via Roma 1', 'Milano', '02-1234567'),
(2, 'Discoteca XYZ', 'Via Garibaldi 2', 'Roma', '06-2345678'),
(3, 'Discoteca 123', 'Piazza del Popolo 3', 'Firenze', '055-3456789'),
(4, 'Discoteca QWE', 'Via Garibaldi 4', 'Napoli', '081-4567890'),
(5, 'Discoteca ASD', 'Piazza del Popolo 5', 'Roma', '06-3456789'),
(6, 'Discoteca ZXC', 'Via Roma 6', 'Torino', '011-5678901'),
(7, 'Discoteca ERT', 'Piazza Duomo 7', 'Milano', '02-3456789'),
(8, 'Discoteca FGH', 'Via Garibaldi 8', 'Napoli', '081-5678901'),
(9, 'Discoteca JKL', 'Corso Vittorio Emanuele 9', 'Roma', '06-4567890');

-- --------------------------------------------------------

--
-- Table structure for table `dj`
--

CREATE TABLE `dj` (
  `id_dj` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `genere_musicale` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dj`
--

INSERT INTO `dj` (`id_dj`, `nome`, `genere_musicale`) VALUES
(1, 'DJ Marco', 'House'),
(2, 'DJ Luca', 'Techno'),
(3, 'DJ Alessia', 'Hip Hop'),
(4, 'DJ Giuseppe', 'EDM'),
(5, 'DJ Federico', 'Tech House'),
(6, 'DJ Valentina', 'Deep House'),
(7, 'DJ Andrea', 'Trance'),
(8, 'DJ Laura', 'House'),
(9, 'DJ Simone', 'Electro');

-- --------------------------------------------------------

--
-- Table structure for table `dj_eventi`
--

CREATE TABLE `dj_eventi` (
  `id_dj` int(11) NOT NULL,
  `id_evento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dj_eventi`
--

INSERT INTO `dj_eventi` (`id_dj`, `id_evento`) VALUES
(1, 1),
(1, 10),
(1, 13),
(2, 2),
(2, 11),
(2, 14),
(3, 3),
(3, 12),
(3, 15),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

-- --------------------------------------------------------

--
-- Table structure for table `eventi`
--

CREATE TABLE `eventi` (
  `id_evento` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `data` date NOT NULL,
  `orario` time NOT NULL,
  `descrizione` varchar(500) NOT NULL,
  `prezzo` decimal(10,2) NOT NULL DEFAULT 0.00,
  `id_discoteca` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `eventi`
--

INSERT INTO `eventi` (`id_evento`, `nome`, `data`, `orario`, `descrizione`, `prezzo`, `id_discoteca`) VALUES
(1, 'Serata House', '2023-03-25', '22:00:00', 'Una serata all’insegna della house music', '20.00', 1),
(2, 'Festa Techno', '2023-04-01', '23:00:00', 'Una festa di techno per tutti gli appassionati', '15.00', 2),
(3, 'Serata Hip Hop', '2023-04-08', '22:30:00', 'Una serata dedicata al meglio dell’hip hop', '18.00', 3),
(4, 'Serata EDM', '2023-04-15', '23:00:00', 'Una serata di musica EDM', '25.00', 4),
(5, 'Festa Tech House', '2023-04-22', '22:30:00', 'Una festa di tech house con ospiti internazionali', '30.00', 5),
(6, 'Serata Deep House', '2023-04-29', '22:00:00', 'Una serata dedicata alla deep house', '20.00', 6),
(7, 'Serata Trance', '2023-05-06', '23:30:00', 'Una serata di musica trance', '20.00', 7),
(8, 'Festa House', '2023-05-13', '22:00:00', 'Una festa di house con ospiti internazionali', '25.00', 8),
(9, 'Serata Electro', '2023-05-20', '22:30:00', 'Una serata dedicata alla musica electro', '18.00', 9),
(10, 'Serata EDM con DJ Giuseppe', '2023-06-03', '22:30:00', 'Una serata di musica EDM con il DJ Giuseppe', '15.00', 1),
(11, 'Festa Tech House con DJ Federico', '2023-06-10', '23:00:00', 'Una festa di tech house con il DJ Federico', '20.00', 2),
(12, 'Serata Deep House con DJ Valentina', '2023-06-17', '22:00:00', 'Una serata dedicata alla deep house con la DJ Valentina', '18.00', 3),
(13, 'Serata Techno con DJ Matteo', '2023-06-23', '23:00:00', 'Una serata di musica techno con il DJ Matteo', '12.00', 1),
(14, 'Festa House con DJ Federica', '2023-07-01', '23:30:00', 'Una festa di house con la DJ Federica', '18.00', 2),
(15, 'Serata Disco con DJ Andrea', '2023-07-15', '22:00:00', 'Una serata dedicata alla disco music con il DJ Andrea', '20.00', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `discoteche`
--
ALTER TABLE `discoteche`
  ADD PRIMARY KEY (`id_discoteca`);

--
-- Indexes for table `dj`
--
ALTER TABLE `dj`
  ADD PRIMARY KEY (`id_dj`);

--
-- Indexes for table `dj_eventi`
--
ALTER TABLE `dj_eventi`
  ADD PRIMARY KEY (`id_dj`,`id_evento`),
  ADD KEY `id_evento` (`id_evento`);

--
-- Indexes for table `eventi`
--
ALTER TABLE `eventi`
  ADD PRIMARY KEY (`id_evento`),
  ADD KEY `discoteca_id` (`id_discoteca`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `discoteche`
--
ALTER TABLE `discoteche`
  MODIFY `id_discoteca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `dj`
--
ALTER TABLE `dj`
  MODIFY `id_dj` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `dj_eventi`
--
ALTER TABLE `dj_eventi`
  MODIFY `id_dj` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `eventi`
--
ALTER TABLE `eventi`
  MODIFY `id_evento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dj_eventi`
--
ALTER TABLE `dj_eventi`
  ADD CONSTRAINT `dj_eventi_ibfk_1` FOREIGN KEY (`id_dj`) REFERENCES `dj` (`id_dj`),
  ADD CONSTRAINT `dj_eventi_ibfk_2` FOREIGN KEY (`id_evento`) REFERENCES `eventi` (`id_evento`);

--
-- Constraints for table `eventi`
--
ALTER TABLE `eventi`
  ADD CONSTRAINT `eventi_ibfk_1` FOREIGN KEY (`id_discoteca`) REFERENCES `discoteche` (`id_discoteca`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
