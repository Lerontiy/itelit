-- phpMyAdmin SQL Dump
-- version 4.7.5
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Час створення: Гру 29 2020 р., 20:30
-- Версія сервера: 5.7.20-log
-- Версія PHP: 5.6.32-1+0~20171027135529.7+stretch~1.gbpd60169

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База даних: `itelit_host1731`
--

-- --------------------------------------------------------

--
-- Структура таблиці `firma`
--

CREATE TABLE `firma` (
  `id` int(4) NOT NULL,
  `name` varchar(40) NOT NULL,
  `lastname` varchar(40) NOT NULL,
  `post` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп даних таблиці `firma`
--

INSERT INTO `firma` (`id`, `name`, `lastname`, `post`) VALUES
(1, 'Володимир', 'Постернак', 'директор'),
(2, 'Діма', 'Доронін', 'програміст'),
(3, 'Андрій', 'Семчук', 'методист'),
(4, 'Роман', 'Павлюс', 'менеджер'),
(5, 'Богдан', 'Зозуляк', 'учень'),
(6, 'Ігор', 'Німий', 'учень'),
(7, 'Стас', 'Сорба', 'учень'),
(8, 'Ігор', 'Кудінов', 'учень'),
(9, 'Соломія', 'Прокопів', 'учень'),
(10, 'Альона', 'Іващук', 'вчитель'),
(11, 'Богдан', 'Охрімчук', 'учень'),
(12, 'Тарас', 'Постернак', 'вчитель'),
(13, 'Вероніка', 'Романко', 'учень'),
(14, 'Володя', 'Костецький', 'учень'),
(15, 'Олег', 'Марчук', 'учень'),
(16, 'Олег', 'Козич', 'методист'),
(17, 'Галина', 'Шевченко', 'вчитель'),
(18, 'Андрій', 'Закопець', 'учень'),
(19, 'Андрій', 'Бинда', 'учень'),
(20, 'Микола', 'Мудрий', 'учень'),
(21, 'Андрій', 'Щегель', 'учень'),
(22, 'Володимир', 'Шевчук', 'вчитель'),
(23, 'Володимир', 'Постернак', 'директор');

--
-- Індекси збережених таблиць
--

--
-- Індекси таблиці `firma`
--
ALTER TABLE `firma`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для збережених таблиць
--

--
-- AUTO_INCREMENT для таблиці `firma`
--
ALTER TABLE `firma`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
