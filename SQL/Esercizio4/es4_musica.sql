-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2023 at 11:17 PM
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
-- Database: `musica`
--

-- --------------------------------------------------------

--
-- Table structure for table `canzoni`
--

CREATE TABLE `canzoni` (
  `id_canzone` bigint(20) NOT NULL,
  `titolo` varchar(60) NOT NULL,
  `durata` time NOT NULL,
  `genere` varchar(40) NOT NULL,
  `data_uscita` date DEFAULT NULL,
  `num_ascolti` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `canzoni`
--

INSERT INTO `canzoni` (`id_canzone`, `titolo`, `durata`, `genere`, `data_uscita`, `num_ascolti`) VALUES
(1, 'Notti In Bianco', '00:02:57', 'Indie', '2020-07-22', 1300200),
(2, 'Blu Celeste', '00:03:46', 'Indie', '2021-09-09', 2100400),
(3, 'Vivere a colori', '00:04:19', 'Pop', '2016-06-17', 4000000),
(4, 'Comunque andare', '00:03:43', 'Pop', '2016-06-17', 3500000),
(5, 'Sorriso Grande', '00:03:26', 'Pop', '2021-04-07', 2500000),
(6, 'Mercy', '00:03:29', 'Pop', '2016-09-21', 5500000),
(7, 'Sabbie Mobili', '00:03:29', 'Pop', '2022-01-13', 1500000),
(8, 'T\'appartengo', '00:03:26', 'Pop', '1994-11-11', 6500000),
(9, 'Pianeti', '00:03:50', 'Pop', '2017-10-06', 2600000),
(10, 'Panico', '00:03:08', 'Rap', '2022-06-09', 2000000),
(11, 'Perle', '00:03:28', 'Pop', '2022-01-13', 2500000),
(12, 'Pastello Bianco', '00:03:58', 'Pop', '2020-12-04', 9500000),
(13, 'Giovani Wannabe', '00:03:33', 'Pop', '2022-06-15', 14500000),
(14, 'You Make Me So Happy', '00:02:23', 'Pop', '2022-06-09', 13500000),
(15, 'Ci Saro\'', '00:03:01', 'Pop', '2021-09-24', 3100000),
(16, 'Cinema', '00:03:22', 'Rap', '2022-04-08', 4500000),
(17, 'There\'s Nothing Holdin\' Me Back', '00:03:20', 'Pop', '2016-04-12', 7500000),
(18, 'When The Beat Drops Out', '00:03:31', 'Pop', '2014-06-16', 8500000);

-- --------------------------------------------------------

--
-- Table structure for table `canzoni_playlist`
--

CREATE TABLE `canzoni_playlist` (
  `id_canzone` bigint(20) NOT NULL,
  `cod_playlist` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `canzoni_playlist`
--

INSERT INTO `canzoni_playlist` (`id_canzone`, `cod_playlist`) VALUES
(1, 1),
(2, 1),
(2, 5),
(3, 2),
(4, 2),
(5, 4),
(5, 5),
(5, 7),
(7, 3),
(8, 10),
(9, 7),
(10, 7),
(11, 3),
(12, 6),
(13, 6),
(14, 9),
(15, 7),
(15, 9),
(17, 4),
(18, 10);

-- --------------------------------------------------------

--
-- Table structure for table `playlist`
--

CREATE TABLE `playlist` (
  `cod_playlist` bigint(20) NOT NULL,
  `nome` varchar(70) NOT NULL,
  `id_utente` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `playlist`
--

INSERT INTO `playlist` (`cod_playlist`, `nome`, `id_utente`) VALUES
(1, 'Blu celeste', 3),
(2, 'Vivere A Colori', 8),
(3, 'Universo', 3),
(4, 'Illuminate', 6),
(5, 'Tutto Accade', 8),
(6, 'Fake News', 9),
(7, 'Sirio', 2),
(8, 'pianeti', 5),
(9, 'Testa Tra Le Nuvole', 7),
(10, 'Mattia04', 1);

-- --------------------------------------------------------

--
-- Table structure for table `utenti`
--

CREATE TABLE `utenti` (
  `id_utente` bigint(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cognome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `utenti`
--

INSERT INTO `utenti` (`id_utente`, `nome`, `cognome`) VALUES
(1, 'Mattia', 'Rossi'),
(2, 'Jacopo', 'Lazzarini'),
(3, 'Mara', 'Sattei'),
(4, 'Riccardo', 'Fabbriconi'),
(5, 'Niccolò', 'Moriconi'),
(6, 'Shaw', 'Mendes'),
(7, 'Andrea', 'De Filippi'),
(8, 'Alessandra', 'Amoroso'),
(9, 'Pinguini', 'Tattici Nucleari');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `canzoni`
--
ALTER TABLE `canzoni`
  ADD PRIMARY KEY (`id_canzone`);

--
-- Indexes for table `canzoni_playlist`
--
ALTER TABLE `canzoni_playlist`
  ADD PRIMARY KEY (`id_canzone`,`cod_playlist`),
  ADD KEY `cod_playlist` (`cod_playlist`);

--
-- Indexes for table `playlist`
--
ALTER TABLE `playlist`
  ADD PRIMARY KEY (`cod_playlist`),
  ADD KEY `id_utente` (`id_utente`);

--
-- Indexes for table `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`id_utente`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `canzoni`
--
ALTER TABLE `canzoni`
  MODIFY `id_canzone` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `playlist`
--
ALTER TABLE `playlist`
  MODIFY `cod_playlist` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `utenti`
--
ALTER TABLE `utenti`
  MODIFY `id_utente` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `canzoni_playlist`
--
ALTER TABLE `canzoni_playlist`
  ADD CONSTRAINT `canzoni_playlist_ibfk_1` FOREIGN KEY (`cod_playlist`) REFERENCES `playlist` (`cod_playlist`),
  ADD CONSTRAINT `canzoni_playlist_ibfk_2` FOREIGN KEY (`id_canzone`) REFERENCES `canzoni` (`id_canzone`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
