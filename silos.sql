-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19-Nov-2021 às 14:58
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `phpmyadmin`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `silos`
--

CREATE TABLE `silos` (
  `Codigo` varchar(255) COLLATE utf8_bin NOT NULL,
  `Produto` varchar(255) COLLATE utf8_bin NOT NULL,
  `Peso` varchar(255) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Extraindo dados da tabela `silos`
--

INSERT INTO `silos` (`Codigo`, `Produto`, `Peso`) VALUES
('4782911109837', '', ''),
('4782201942124', '', ''),
('4782334190212', '', ''),
('4782132000987', '', ''),
('4788392029111', '', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
