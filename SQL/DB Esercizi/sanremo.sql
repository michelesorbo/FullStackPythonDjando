-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 08, 2023 at 12:16 AM
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
-- Database: `sanremo`
--

-- --------------------------------------------------------

--
-- Table structure for table `artisti`
--

CREATE TABLE `artisti` (
  `id_artista` bigint(20) NOT NULL,
  `nome` text NOT NULL,
  `numero_album` int(11) DEFAULT NULL,
  `citta` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `artisti`
--

INSERT INTO `artisti` (`id_artista`, `nome`, `numero_album`, `citta`) VALUES
(1, 'Anna Oxa', 23, 'Bari'),
(2, 'Gianmaria', 1, 'Vicenza'),
(3, 'Mr. Rain', 4, 'Desenzano del Garda'),
(4, 'Marco Mengoni', 11, 'Ronciglione'),
(5, 'Ariete', 2, 'Anzio'),
(6, 'Ultimo', 4, 'Roma'),
(7, 'Coma_Cose', 4, 'Milano'),
(8, 'Elodie', 3, 'Roma'),
(9, 'Leo Gassmann', 1, 'Roma'),
(10, 'I cugini di campagna', 19, 'Roma'),
(11, 'Gianluca Grignani', 16, 'Milano'),
(12, 'Olly', 2, 'Genova'),
(13, 'Colla zio', 0, 'Milano'),
(14, 'Mara Sattei', 1, 'Roma'),
(15, 'Will', 0, 'Vittorio Veneto'),
(16, 'Modà', 10, 'Milano'),
(17, 'SetHu', 0, 'Savona'),
(18, 'Articolo 31', 10, 'Milano'),
(19, 'Lazza', 3, 'Milano'),
(20, 'Giorgia', 19, 'Roma'),
(21, 'Colapesce e Di Martino', 1, 'Siracusa'),
(22, 'Shari', 0, 'Monfalcone'),
(23, 'Madame', 1, 'Creazzo'),
(24, 'Levante', 5, 'Caltagirone'),
(25, 'Tananai', 2, 'Milano'),
(26, 'Rosa Chemical', 2, 'Alpignano'),
(27, 'LDA', 1, 'Napoli'),
(28, 'Paola e Chiara', 10, 'Milano');

-- --------------------------------------------------------

--
-- Table structure for table `brani`
--

CREATE TABLE `brani` (
  `id_brano` bigint(20) NOT NULL,
  `nome` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brani`
--

INSERT INTO `brani` (`id_brano`, `nome`) VALUES
(1, 'Sali (Canto dell\'anima)'),
(2, 'Mostro'),
(3, 'Supereroi'),
(4, 'Due vite'),
(5, 'Mare di guai'),
(6, 'Alba'),
(7, 'L\'addio'),
(8, 'Due'),
(9, 'Terzo cuore'),
(10, 'Lettera 22'),
(11, 'Quando ti manca il fiato'),
(12, 'Polvere'),
(13, 'Non mi va'),
(14, 'Duemilaminuti'),
(15, 'Stupido'),
(16, 'Lasciami'),
(17, 'Cause perse'),
(18, 'Un bel viaggio'),
(19, 'Cenere'),
(20, 'Parole dette male'),
(21, 'Splash'),
(22, 'Egoista'),
(23, 'Il bene nel male'),
(24, 'Vivo'),
(25, 'Tango'),
(26, 'Made in Italy'),
(27, 'Se poi domani'),
(28, 'Furore');

-- --------------------------------------------------------

--
-- Table structure for table `esibizioni`
--

CREATE TABLE `esibizioni` (
  `id_artista` bigint(20) NOT NULL,
  `id_brano` bigint(11) NOT NULL,
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `esibizioni`
--

INSERT INTO `esibizioni` (`id_artista`, `id_brano`, `data`) VALUES
(1, 1, '2023-02-07'),
(2, 2, '2023-02-07'),
(3, 3, '2023-02-07'),
(4, 4, '2023-02-07'),
(5, 5, '2023-02-07'),
(6, 6, '2023-02-07'),
(7, 7, '2023-02-07'),
(8, 8, '2023-02-07'),
(9, 9, '2023-02-07'),
(10, 10, '2023-02-07'),
(11, 11, '2023-02-07'),
(12, 12, '2023-02-07'),
(13, 13, '2023-02-07'),
(14, 14, '2023-02-07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `artisti`
--
ALTER TABLE `artisti`
  ADD PRIMARY KEY (`id_artista`);

--
-- Indexes for table `brani`
--
ALTER TABLE `brani`
  ADD PRIMARY KEY (`id_brano`);

--
-- Indexes for table `esibizioni`
--
ALTER TABLE `esibizioni`
  ADD PRIMARY KEY (`id_artista`,`id_brano`,`data`),
  ADD KEY `id_brano` (`id_brano`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `artisti`
--
ALTER TABLE `artisti`
  MODIFY `id_artista` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `brani`
--
ALTER TABLE `brani`
  MODIFY `id_brano` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `esibizioni`
--
ALTER TABLE `esibizioni`
  ADD CONSTRAINT `esibizioni_ibfk_1` FOREIGN KEY (`id_artista`) REFERENCES `artisti` (`id_artista`),
  ADD CONSTRAINT `esibizioni_ibfk_2` FOREIGN KEY (`id_brano`) REFERENCES `brani` (`id_brano`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
