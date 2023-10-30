-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2023 at 11:35 PM
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
-- Database: `film`
--

-- --------------------------------------------------------

--
-- Table structure for table `attori`
--

CREATE TABLE `attori` (
  `id_attore` bigint(20) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cognome` varchar(255) NOT NULL,
  `data_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attori`
--

INSERT INTO `attori` (`id_attore`, `nome`, `cognome`, `data_nascita`) VALUES
(1, 'Brad', 'Pitt', '1963-12-18'),
(2, 'Helena', 'Bonham Carter', '1966-05-26'),
(3, 'Leonardo', 'Di Caprio', '1974-11-11'),
(4, 'Kate', 'Winslet', '1975-10-05'),
(5, 'Colin', 'Firth', '1960-09-10'),
(6, 'Robert Sean', 'Leonard', '1969-02-28'),
(7, 'Robin', 'Williams', '1951-07-21'),
(8, 'Benedict', 'Cumberbatch', '1976-07-19'),
(9, 'Keira', 'Knightley', '1985-03-26'),
(10, 'Will', 'Smith', '1968-09-25'),
(11, 'Jaden', 'Smith', '1998-07-08'),
(12, 'Sandra', 'Bullock', '1964-07-26'),
(13, 'Ryan', 'Reynolds', '1976-10-23'),
(14, 'Linda', 'Blair', '1959-01-22'),
(15, 'Jason', 'Miller', '1939-04-22'),
(16, 'Bradley', 'Cooper', '1975-01-05'),
(17, 'Ed', 'Helms', '1974-01-24'),
(18, 'Elijah', 'Wood', '1981-01-28'),
(19, 'Cate', 'Blanchett', '1969-05-14'),
(20, 'Matthew', 'McConaughey', '1969-11-04'),
(21, 'Anne', 'Hathaway', '1982-11-12'),
(22, 'Terence', 'Hill', '1939-03-29'),
(23, 'Bud', 'Spencer', '1929-10-31'),
(24, 'Lady', 'Gaga', '1986-03-28'),
(25, 'Adam', 'Driver', '1983-11-19');

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `id_film` bigint(20) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `trama` text DEFAULT NULL,
  `durata` time NOT NULL,
  `data_uscita` date NOT NULL,
  `id_genere` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`id_film`, `nome`, `trama`, `durata`, `data_uscita`, `id_genere`) VALUES
(1, 'Fight Club', 'Tyler Durden ed un nuovo amico sfogano la loro aggressività creando un club di combattimento, che assume rapidamente connotati rivoluzionari, fino a esporre la vera identità di Tyler Durden.', '02:19:00', '1999-10-15', 1),
(2, 'Titanic', 'Il transatlantico Titanic, considerato un gioiello tecnologico ed il più lussuoso piroscafo da crociera mai realizzato, salpa dall\'Inghilterra il dieci aprile del 1912 con oltre 1500 passeggeri a bordo per il suo viaggio inaugurale. I viaggiatori sono collocati in tre classi, riflesso delle differenze sociali.', '03:47:00', '1998-01-16', 2),
(3, 'Il discorso del re', 'Dopo la morte del padre e l\'abdicazione del fratello Edoardo VIII, Bertie, che soffre da tutta la vita di balbuzie, viene incoronato re con il nome di Giorgio VI d\'Inghilterra. La sua fida, ora, è quella di affrontare un importante discorso pubblico.', '01:58:00', '2011-01-28', 3),
(4, 'L\'attimo fuggente', 'Un insegnante di un liceo per classi abbienti del New England utilizza metodi non convenzionali per esortare i suoi studenti, sotto pressione dai genitori e dalla scuola, alla libertà e creatività.', '02:08:00', '1989-09-29', 2),
(5, 'Inside out', 'Riley è costretta a lasciare la propria vita nel Midwest quando il padre si trasferisce per lavoro a San Francisco. La piccola è guidata dalle proprie emozioni: Gioia, Paura, Rabbia, Disgusto e Tristezza, che vivono nel Quartier Generale, il centro di controllo nella mente, da dove l\'aiutano a affrontare la vita di tutti i giorni.', '01:35:00', '2015-09-16', 4),
(6, 'Il re leone', 'In seguito alla morte del padre, il cucciolo di leone Simba deve combattere il malvagio zio Scar che cerca di rubargli il trono di re della giungla. In suo aiuto ci sono due simpatici compagni, Timon e Pumbaa.', '01:29:00', '1994-11-23', 4),
(7, 'The imitation game', 'La vita del matematico inglese Alan Turing, genio indiscusso del XX secolo, considerato uno dei padri dell\'informatica e dei moderni computer, fino alla sua precoce e tragica scomparsa.', '01:54:00', '2014-09-28', 2),
(8, 'La ricerca della felicità', 'Chris Gardner è un genitore single che lotta per crescere il figlio e cercare di realizzare il sogno di una vita migliore e dignitosa per entrambi.', '01:57:00', '2007-01-12', 2),
(9, 'Love actually', 'Nella città di Londra le storie di nove personaggi si intrecciano per raccontare la complessità dei rapporti umani e dell\'amore.', '02:09:00', '2003-11-14', 5),
(10, 'Ricatto d\'amore', 'Di fronte alla minaccia di deportazione dal Canada, un\'editrice di successo finge di essere fidanzata con il proprio assistente, lo stesso uomo che ha tormentato per anni.', '01:48:00', '2009-09-03', 5),
(11, 'L\'esorcista', 'Regan McNeil, una ragazzina di 12 anni, viene posseduta dal demonio. Un giovane prete in crisi di fede, aiutato dal proprio anziano mentore, affronta la presenza demoniaca in un mortale duello.', '02:12:00', '1974-10-04', 6),
(12, 'Una notte da leoni', 'Arrivato a Las Vegas per festeggiare l\'addio al celibato del loro amico Doug, durante la notte il gruppetto si dà alla pazza gioia prendendo una sbornia colossale. Al risveglio, però, qualcosa non va.', '01:40:00', '2009-06-19', 7),
(13, 'Il signore degli anelli', 'Un giovane hobbit e un variegato gruppo, composto da umani, un nano, un elfo e altri hobbit, partono per un delicata missione, guidati dal potente mago Gandalf. Devono distruggere un anello magico e sconfiggere così il malvagio Sauron.', '02:58:00', '2002-01-18', 8),
(14, 'Interstellar', 'In un futuro non precisato, un drastico cambiamento climatico colpisce duramente l\'agricoltura. Il granturco è l\'unica coltivazione ancora in grado di crescere ed un gruppo di scienziati è intenzionato ad attraversare lo spazio per trovare nuovi luoghi adatti a coltivarlo.', '02:49:00', '2014-10-26', 10),
(15, 'Lo chiamavano Trinità', 'Un pistolero buono e pigro, giunge in una cittadina dove ritrova suo fratello sotto le mentite spoglie di sceriffo, assunte per poter meglio perpetrare un furto di bestiame.', '01:55:00', '1970-12-22', 9),
(16, 'House of Gucci', 'Il difficile matrimonio e il tormentato divorzio di Patrizia e Maurizio Gucci, capo della casa di moda Gucci, porta ad un efferato omicidio.', '02:37:00', '2021-11-24', 11),
(17, 'Frozen', 'Il regno di ghiaccio', '01:32:00', '2013-12-12', 4),
(19, 'Il padrino', NULL, '02:55:00', '1972-09-21', NULL),
(20, 'Top Gun', NULL, '01:50:00', '1986-09-25', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `generi`
--

CREATE TABLE `generi` (
  `id_genere` bigint(20) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `descrizione` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `generi`
--

INSERT INTO `generi` (`id_genere`, `nome`, `descrizione`) VALUES
(1, 'Thriller', 'Il thriller (dall\'inglese to thrill, rabbrividire) è un genere di fiction che utilizza la suspense, la tensione e l\'eccitazione come elementi principali della trama.'),
(2, 'Drammatico', 'Un film drammatico è un genere di film che si basa sullo sviluppo dei personaggi, dell\'interazione tra essi e che tratta temi di impatto emotivo. Gone With The Wind è un dramma romantico. La definizione del genere è complessa e non ne esiste una universalmente condivisa, né dal punto di vista stilistico né tematico.'),
(3, 'Storico', 'Un film storico è un film in costume che tratta vicende reali, veramente o almeno verosimilmente avvenute nel passato e comunque ambientate in un preciso contesto storico, ricostruito nei dettagli in modo da apparire credibile allo spettatore.'),
(4, 'Animazione', 'Per cinema d\'animazione s\'intende pertanto quel particolare cinema che viene realizzato non attraverso la riproduzione fotografica della realtà, ma producendo una nuova realtà inventata, ottenuta dalla scomposizione e dalla ricomposizione del movimento delle figure.'),
(5, 'Romantico', 'Il film sentimentale mette la storia d\'amore o la ricerca dell\'amore al centro della trama principale. Occasionalmente, gli amanti devono affrontare ostacoli come problemi finanziari, malattie, varie forme di discriminazione, vincoli psicologici o familiari che minacciano di rompere la loro unione.'),
(6, 'Horror', 'Il cinema dell\'orrore o cinema horror è un genere cinematografico caratterizzato da personaggi immaginari e mostruosi, situazioni macabre, irrazionali o di origine soprannaturale e con atmosfere da brivido.'),
(7, 'Comico', 'Partiamo dalle basi: il film comico è un genere di pellicola incentrato sull\'innescare nello spettatore il meccanismo del riso e instillare un buonumore generalizzato. Per fare questo vengono adottate diverse tecniche, dal linguaggio umoristico alle gag divertenti, sino alle situazioni squisitamente paradossali.'),
(8, 'Fantasy', 'Genere di film che racconta una storia con elementi fantastici, surreali o fiabeschi: creature immaginarie, vicende al limite o oltre la realtà, incantesimi e magie, viaggi in dimensioni ultraterrene.'),
(9, 'Western', 'Genere cinematografico d\'avventura che, attraverso le vicende di pionieri, cowboy e fuorilegge, affronta il tema della \'frontiera\' all\'epoca della colonizzazione delle regioni occidentali (West) degli USA. Nato agli albori del cinema (il primo esempio può essere considerato L\'assalto al treno, 1903, di Edwin S.'),
(10, 'Fantascienza', 'Solitamente questo genere di film viene ambientato in un contesto legato a una visione più o meno lontana del futuro, come quello dei viaggi interstellari, quello del contatto con entità extraterrestri, quello dei conflitti nucleari o delle catastrofi climatiche globali.'),
(11, 'Biografico', 'Detto anche biopic (biographical picture), comprende quei film che rievocano la vita di personaggi realmente vissuti, rielaborandola in modo più o meno romanzesco.');

-- --------------------------------------------------------

--
-- Table structure for table `recitare`
--

CREATE TABLE `recitare` (
  `id_attore` bigint(20) NOT NULL,
  `id_film` bigint(20) NOT NULL,
  `ruolo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recitare`
--

INSERT INTO `recitare` (`id_attore`, `id_film`, `ruolo`) VALUES
(1, 1, 'Protagonista'),
(2, 1, 'Non protagonista'),
(2, 3, 'Non protagonista'),
(3, 2, 'Protagonista'),
(4, 2, 'Protagonista'),
(5, 3, 'Protagonista'),
(5, 9, 'Non protagonista'),
(6, 4, 'Non protagonista'),
(7, 4, 'Protagonista'),
(8, 7, 'Protagonista'),
(9, 7, 'Non protagonista'),
(9, 9, 'Non protagonista'),
(10, 8, 'Protagonista'),
(11, 8, 'Non protagonista'),
(12, 10, 'Protagonista'),
(13, 10, 'Protagonista'),
(14, 11, 'Protagonista'),
(15, 11, 'Non protagonista'),
(16, 12, 'Protagonista'),
(17, 12, 'Protagonista'),
(18, 13, 'Protagonista'),
(19, 13, 'Non protagonista'),
(20, 14, 'Protagonista'),
(21, 14, 'Non protagonista'),
(22, 15, 'Protagonista'),
(23, 15, 'Protagonista'),
(24, 16, 'Protagonista'),
(25, 16, 'Protagonista');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attori`
--
ALTER TABLE `attori`
  ADD PRIMARY KEY (`id_attore`);

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`id_film`),
  ADD KEY `id_genere` (`id_genere`);

--
-- Indexes for table `generi`
--
ALTER TABLE `generi`
  ADD PRIMARY KEY (`id_genere`);

--
-- Indexes for table `recitare`
--
ALTER TABLE `recitare`
  ADD PRIMARY KEY (`id_attore`,`id_film`),
  ADD KEY `id_film` (`id_film`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attori`
--
ALTER TABLE `attori`
  MODIFY `id_attore` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `film`
--
ALTER TABLE `film`
  MODIFY `id_film` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `generi`
--
ALTER TABLE `generi`
  MODIFY `id_genere` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `film`
--
ALTER TABLE `film`
  ADD CONSTRAINT `film_ibfk_1` FOREIGN KEY (`id_genere`) REFERENCES `generi` (`id_genere`);

--
-- Constraints for table `recitare`
--
ALTER TABLE `recitare`
  ADD CONSTRAINT `recitare_ibfk_1` FOREIGN KEY (`id_attore`) REFERENCES `attori` (`id_attore`),
  ADD CONSTRAINT `recitare_ibfk_2` FOREIGN KEY (`id_film`) REFERENCES `film` (`id_film`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
