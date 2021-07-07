-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jun 17, 2021 at 12:51 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `license_plate`
--

DROP TABLE IF EXISTS `license_plate`;
CREATE TABLE IF NOT EXISTS `license_plate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `license_plate` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `license_plate` (`license_plate`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `license_plate`
--

INSERT INTO `license_plate` (`id`, `license_plate`, `created_at`) VALUES
(1, 'ABC 1234', '2021-06-09 02:56:38'),
(2, 'CDF 1278', '2021-06-09 02:56:51'),
(3, '032 KKL', '2021-06-11 01:31:01'),
(4, 'BCN 8827', '2021-06-11 01:40:16'),
(5, 'ARTPL8', '2021-06-12 02:09:46'),
(6, 'GEZ 1164', '2021-06-12 02:10:11'),
(7, 'AZM9590', '2021-06-12 02:10:36'),
(8, 'CAJA 723', '2021-06-12 02:25:02'),
(9, 'LGM 3295', '2021-06-16 00:31:17');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
