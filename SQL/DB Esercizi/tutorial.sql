-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 02, 2023 at 01:14 AM
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
-- Database: `tutorial`
--

-- --------------------------------------------------------

--
-- Table structure for table `categorie`
--

CREATE TABLE `categorie` (
  `id_categoria` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `descrizione` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categorie`
--

INSERT INTO `categorie` (`id_categoria`, `nome`, `descrizione`) VALUES
(1, 'Programmazione', 'Categoria per i tutorial di programmazione'),
(2, 'Design', 'Categoria per i tutorial di design'),
(3, 'Business', 'Categoria per i tutorial di business'),
(4, 'Musica', 'Categoria per i tutorial di musica'),
(5, 'Sport', 'Categoria per i tutorial di sport'),
(6, 'Cucina', 'Categoria per i tutorial di cucina'),
(7, 'Lingue', 'Categoria per i tutorial di lingue');

-- --------------------------------------------------------

--
-- Table structure for table `social_network`
--

CREATE TABLE `social_network` (
  `id_social_network` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `social_network`
--

INSERT INTO `social_network` (`id_social_network`, `nome`) VALUES
(1, 'Facebook'),
(2, 'Twitter'),
(3, 'Instagram'),
(4, 'LinkedIn'),
(5, 'TikTok'),
(6, 'YouTube'),
(7, 'Pinterest');

-- --------------------------------------------------------

--
-- Table structure for table `tutorial`
--

CREATE TABLE `tutorial` (
  `id_tutorial` int(11) NOT NULL,
  `titolo` varchar(255) NOT NULL,
  `descrizione` text DEFAULT NULL,
  `livello` varchar(50) DEFAULT NULL,
  `durata` time DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tutorial`
--

INSERT INTO `tutorial` (`id_tutorial`, `titolo`, `descrizione`, `livello`, `durata`, `link`, `id_categoria`) VALUES
(1, 'Introduzione a Python', 'Un tutorial introduttivo su Python', 'Principiante', '00:10:20', 'https://www.example.com/python', 1),
(2, 'Progettare un sito web', 'Un tutorial su come progettare un sito web', 'Intermedio', '00:09:30', 'https://www.example.com/web-design', 2),
(3, 'Marketing sui social media', 'Un tutorial su come fare marketing sui social media', 'Avanzato', '00:02:40', 'https://www.example.com/social-media-marketing', 3),
(4, 'Imparare a suonare la chitarra', 'Un tutorial su come suonare la chitarra', 'Principiante', '00:15:20', 'https://www.example.com/guitar', 4),
(5, 'Allenamento a casa', 'Un tutorial su come fare allenamento a casa', 'Intermedio', '00:11:20', 'https://www.example.com/home-workout', 5),
(6, 'Imparare a cucinare la pasta', 'Un tutorial su come cucinare la pasta', 'Principiante', '01:01:08', 'https://www.example.com/cooking-pasta', 6),
(7, 'Imparare il francese', 'Un tutorial su come imparare il francese', 'Intermedio', '00:11:00', 'https://www.example.com/learn-french', 7),
(8, 'Progettare un logo', 'Un tutorial su come progettare un logo', 'Intermedio', '00:16:00', 'https://www.example.com/logo-design', 2),
(9, 'Programmazione avanzata in Java', 'Un tutorial avanzato su Java', 'Avanzato', '00:15:40', 'https://www.example.com/advanced-java', 1),
(10, 'Marketing su Facebook', 'Un tutorial su come fare marketing su Facebook', 'Intermedio', '00:10:20', 'https://www.example.com/facebook-marketing', 3),
(11, 'Imparare a dipingere', 'Un tutorial su come dipingere', 'Principiante', '00:04:00', 'https://www.example.com/painting', 4),
(12, 'Imparare a fare yoga', 'Un tutorial su come fare yoga', 'Principiante', '00:12:00', 'https://www.example.com/yoga', 5),
(13, 'Imparare il tedesco', 'Un tutorial su come imparare il tedesco', 'Intermedio', '00:16:00', 'https://www.example.com/learn-german', 7),
(14, 'Creare un sito web responsive', 'Un tutorial su come creare un sito web responsive', 'Intermedio', '00:09:20', 'https://www.example.com/responsive-web-design', 2),
(15, 'Programmazione in C', 'Un tutorial introduttivo su C', 'Principiante', '00:07:16', 'https://www.example.com/c-programming', 1),
(16, 'Imparare a suonare il pianoforte', 'Un tutorial su come suonare il pianoforte', 'Principiante', '00:12:30', 'https://www.example.com/piano', 4),
(17, 'Imparare il giapponese', 'Un tutorial su come imparare il giapponese', 'Intermedio', '00:24:08', 'https://www.example.com/learn-japanese', 7);

-- --------------------------------------------------------

--
-- Table structure for table `tutorial_social_network`
--

CREATE TABLE `tutorial_social_network` (
  `id_tutorial` int(11) NOT NULL,
  `id_social_network` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tutorial_social_network`
--

INSERT INTO `tutorial_social_network` (`id_tutorial`, `id_social_network`) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3),
(4, 4),
(4, 5),
(5, 3),
(5, 5),
(6, 6),
(7, 3),
(7, 6),
(8, 1),
(8, 3),
(9, 1),
(9, 2),
(9, 3),
(10, 1),
(10, 2),
(11, 1),
(11, 3),
(12, 2),
(13, 1),
(13, 3),
(14, 1),
(14, 2),
(15, 2),
(15, 3),
(16, 1),
(17, 1),
(17, 2),
(17, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categorie`
--
ALTER TABLE `categorie`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indexes for table `social_network`
--
ALTER TABLE `social_network`
  ADD PRIMARY KEY (`id_social_network`);

--
-- Indexes for table `tutorial`
--
ALTER TABLE `tutorial`
  ADD PRIMARY KEY (`id_tutorial`),
  ADD KEY `categoria_id` (`id_categoria`);

--
-- Indexes for table `tutorial_social_network`
--
ALTER TABLE `tutorial_social_network`
  ADD PRIMARY KEY (`id_tutorial`,`id_social_network`),
  ADD KEY `social_network_id` (`id_social_network`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tutorial`
--
ALTER TABLE `tutorial`
  ADD CONSTRAINT `tutorial_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categorie` (`id_categoria`);

--
-- Constraints for table `tutorial_social_network`
--
ALTER TABLE `tutorial_social_network`
  ADD CONSTRAINT `tutorial_social_network_ibfk_1` FOREIGN KEY (`id_tutorial`) REFERENCES `tutorial` (`id_tutorial`),
  ADD CONSTRAINT `tutorial_social_network_ibfk_2` FOREIGN KEY (`id_social_network`) REFERENCES `social_network` (`id_social_network`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
