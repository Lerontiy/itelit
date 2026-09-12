-- phpMyAdmin SQL Dump
-- version 4.0.10.2
-- http://www.phpmyadmin.net
--
-- Хост: itelit.mysql.ukraine.com.ua
-- Час створення: Бер 17 2015 р., 07:44
-- Версія сервера: 5.1.72-cll-lve
-- Версія PHP: 5.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База даних: `itelit_car`
--

-- --------------------------------------------------------

--
-- Структура таблиці `foto`
--

CREATE TABLE IF NOT EXISTS `foto` (
  `id_car` int(4) NOT NULL,
  `foto` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп даних таблиці `foto`
--

INSERT INTO `foto` (`id_car`, `foto`) VALUES
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/1.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/2.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/3.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/4.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/5.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/6.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/7.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/8.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/9.jpg'),
(1, 'http://zavd.it-elit.org/fotoavto/mersedes/10.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/1.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/2.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/3.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/4.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/5.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/6.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/7.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/8.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/9.jpg'),
(2, 'http://zavd.it-elit.org/fotoavto/bmw/10.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/1.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/2.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/3.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/4.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/5.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/6.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/7.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/8.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/9.jpg'),
(3, 'http://zavd.it-elit.org/fotoavto/audi/10.jpg'),
(0, '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
