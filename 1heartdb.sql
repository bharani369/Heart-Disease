-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 24, 2025 at 07:25 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1heartdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `psw`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `diseasetb`
--

CREATE TABLE `diseasetb` (
  `id` int(10) NOT NULL auto_increment,
  `symptoms` varchar(100) NOT NULL,
  `disease` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `diseasetb`
--


-- --------------------------------------------------------

--
-- Table structure for table `querytb`
--

CREATE TABLE `querytb` (
  `id` bigint(250) NOT NULL auto_increment,
  `UserName` varchar(1000) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Height` varchar(250) NOT NULL,
  `Weight` varchar(250) NOT NULL,
  `ap_hi` varchar(250) NOT NULL,
  `ap_lo` varchar(250) NOT NULL,
  `cholesterol` varchar(250) NOT NULL,
  `glucose` varchar(250) NOT NULL,
  `Smoke` varchar(250) NOT NULL,
  `Alcohol` varchar(250) NOT NULL,
  `DResult` varchar(250) NOT NULL,
  `Prescription` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=67 ;

--
-- Dumping data for table `querytb`
--

INSERT INTO `querytb` (`id`, `UserName`, `Age`, `Gender`, `Height`, `Weight`, `ap_hi`, `ap_lo`, `cholesterol`, `glucose`, `Smoke`, `Alcohol`, `DResult`, `Prescription`) VALUES
(1, 'yaathash', '20', '1', '168', '75', '110', '90', '3', '80', '1', '1', 'Heart', ''),
(2, 'san', '20', '1', '168', '65', '110', '90', '3', '2', '1', '1', 'You DON T have  Heart Disease', 'Nill'),
(3, 'sangeeth', '20', '1', '168', '65', '110', '90', '3', '1', '1', '1', 'Arrhythmia', 'Procainamide (Procan, Procanbid) '),
(4, 'sangeeth', '60', '1', '168', '90', '140', '90', '3', '1', '1', '1', 'Arrhythmia', 'Procainamide (Procan, Procanbid) '),
(5, 'raveena', '60', '1', '168', '90', '140', '90', '3', '2', '1', '1', 'Arrhythmia', 'Procainamide (Procan, Procanbid) '),
(6, 'san', '20', '1', '168', '65', '150', '90', '3', '85', '2', '1', 'Arrhythmia', 'Procainamide (Procan, Procanbid) '),
(7, 'admin', '29', '2', '152', '50', '11', '11', '2', '2', '1', '1', 'You DON T have  Heart Disease', 'Nill'),
(8, 'admin', '55', '2', '152', '50', '156', '128', '1', '3', '1', '1', 'Arrhythmia', 'Procainamide (Procan, Procanbid) '),
(9, 'sam12', '24', '1', '56', '61', '82', '36', '1', '1', '0', '0', 'waiting', ''),
(10, 'vsp', '24', '1', '56', '61', '82', '36', '1', '2', '0', '0', 'waiting', ''),
(11, 'vsp', '24', '2', '56', '', '82', '36', '2', '1', '0', '0', 'waiting', ''),
(12, 'vsp', '24', '2', '56', '61', '82', '36', '2', '1', '0', '0', 'waiting', ''),
(13, 'vsp', '24', '2', '56', '61', '82', '36', '1', '1', '0', '0', 'Heart', ''),
(14, 'vsp', '23', '2', '56', '61', '82', '36', '1', '1', '0', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(15, 'vsp', '24', '2', '56', '61', '82', '36', '1', '1', '0', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(16, 'admin', '24', '2', '56', '61', '82', '36', '2', '2', '0', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(17, 'a123', '30', '1', '56', '61', '82', '36', '1', '1', '0', '1', 'waiting', ''),
(18, 'a123', '30.0', '2.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Heart'),
(19, 'a123', '30.0', '1.0', '56.0', '61.0', '82.0', '36.0', '3.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(20, 'a123', '24.0', '2.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '0.0', '0.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(21, 'admin12', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(22, 'admin12', '24.0', '2.0', '1.8', '5.0', '82.0', '36.0', '3.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(23, 'admin12', '24.0', '1.0', '6.0', '61.0', '82.0', '110.0', '1.0', '1.0', '0.0', '0.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(24, 'admin12', '52.0', '1.0', '165.0', '64.0', '130.0', '70.0', '3.0', '2.0', '0.0', '0.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(25, 'admin12', '20.0', '1.0', '168.0', '65.0', '110.0', '90.0', '3.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(26, 'admin', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(27, 'admin', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', ''),
(28, 'admin', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', ''),
(29, 'admin', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', ''),
(30, 'admin', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', ''),
(31, 'admin', '23.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(32, 'admin', '23.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(33, 'admin', '35.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Benazepril (Lotensin),Captopril (Capoten),Enalapril (Vasotec),Fosinopril (Monopril),Lisinopril (Prinivil, Zestril)'),
(34, 'admin', '35.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Benazepril (Lotensin),Captopril (Capoten),Enalapril (Vasotec),Fosinopril (Monopril),Lisinopril (Prinivil, Zestril)'),
(35, 'admin', '59.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Azilsartan (Edarbi),Candesartan (Atacand),Eprosartan (Teveten),Irbesartan (Avapro),Losartan (Cozaar)'),
(36, 'admin', '70.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', ''),
(37, 'admin', '70.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Azilsartan (Edarbi),Candesartan (Atacand),Eprosartan (Teveten),Irbesartan (Avapro),Losartan (Cozaar)'),
(38, 'admin', '70.0', '1.0', '56.0', '61.0', '11.0', '11.0', '2.0', '2.0', '1.0', '1.0', 'Heart', 'Medications Names:Azilsartan (Edarbi),Candesartan (Atacand),Eprosartan (Teveten),Irbesartan (Avapro),Losartan (Cozaar)'),
(39, 'admin', '70.0', '1.0', '56.0', '61.0', '11.0', '11.0', '2.0', '1.0', '1.0', '1.0', 'No HeartDisess', 'Medications Names:Azilsartan (Edarbi),Candesartan (Atacand),Eprosartan (Teveten),Irbesartan (Avapro),Losartan (Cozaar)'),
(40, 'admin', '70.0', '1.0', '56.0', '61.0', '11.0', '11.0', '2.0', '1.0', '1.0', '1.0', 'No HeartDisess', 'Medications Names:Azilsartan (Edarbi),Candesartan (Atacand),Eprosartan (Teveten),Irbesartan (Avapro),Losartan (Cozaar)'),
(41, 'sqwe', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '1.0', '1.0', '1.0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(42, 'admin12', '24.0', '1.0', '56.0', '61.0', '82.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You dont have any symptoms Heart Disease', ''),
(43, 'admin12', '24.0', '1.0', '56.0', '61.0', '120.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You have symptoms of getting heart disease', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(44, 'admin12', '24.0', '1.0', '56.0', '61.0', '120.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You have symptoms of getting heart disease', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(45, 'admin12', '24.0', '1.0', '56.0', '61.0', '120.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You have symptoms of getting heart disease', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(46, 'admin12', '24.0', '1.0', '56.0', '61.0', '120.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You have symptoms of getting heart disease', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(47, 'admin12', '24.0', '1.0', '56.0', '61.0', '120.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You have symptoms of getting heart disease', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(48, 'admin12', '24.0', '1.0', '56.0', '61.0', '100.0', '36.0', '2.0', '2.0', '1.0', '0.0', 'You dont have any symptoms Heart Disease', ''),
(49, 'SWER', '26.0', '1.0', '34.0', '44.0', '130.0', '89.0', '2.0', '2.0', '1.0', '1.0', 'You have symptoms of getting heart disease', 'Medications Names:Aspirin,Clopidogrel (Plavix),Dipyridamole (Persantine),Prasugrel (Effient),Ticagrelor (Brilinta)'),
(50, 'admin', '24', '2', '56', '61', '82', '36', '2', '2', '0', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(51, 'admin', '24', '2', '56', '61', '82', '36', '2', '2', '0', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(52, 's1234', '30', '1', '56', '61', '82', '36', '1', '1', '1', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(53, 'sam', '30', '1', '56', '61', '82', '36', '1', '1', '0', '0', 'waiting', ''),
(54, 'sample', '30', '1', '56', '61', '82', '36', '2', '2', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(55, 'admin', '24', '1', '56', '61', '82', '36', '3', '3', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(56, 'admin', '70', '1', '56', '61', '11', '11', '3', '2', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(57, 'admin', '70', '1', '56', '61', '11', '11', '2', '2', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(58, 'admin', '70', '1', '56', '61', '11', '11', '2', '2', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(59, 'admin', '70', '1', '56', '61', '11', '11', '2', '2', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(60, 'admin', '70', '1', '56', '61', '11', '11', '2', '2', '1', '1', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(61, 'admin', '30', '2', '56', '61', '82', '36', '1', '1', '0', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(62, 'admin', '30', '2', '56', '61', '82', '36', '1', '1', '0', '0', 'Congratulations!  You DON T have Heart Disease', 'Managing Glucose in T1D Once Had But One Treatment'),
(63, 'anbu86', '25', '1', '180', '90', '120', '50', '2', '2', '1', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(64, 'anbu86', '52', '1', '165', '64', '130', '70', '3', '1', '0', '0', 'Heart', 'Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)'),
(65, 'admin', '32', 'F', 'NAP', '12', '12', '1', 'ST', '12', 'Y', '12', 'Heart Disease', 'Managing Glucose in T1D Once Had But One Treatment'),
(66, 'admin', '32', 'M', 'NAP', '23', '23', '1', 'ST', '32', 'Y', '23', 'Heart Disease', 'Managing Glucose in T1D Once Had But One Treatment');

-- --------------------------------------------------------

--
-- Table structure for table `querytb1`
--

CREATE TABLE `querytb1` (
  `ID` int(11) NOT NULL auto_increment,
  `UserName` varchar(100) default NULL,
  `Age` int(11) default NULL,
  `Sex` varchar(1) default NULL,
  `ChestPainType` varchar(10) default NULL,
  `RestingBP` int(11) default NULL,
  `Cholesterol` int(11) default NULL,
  `FastingBS` tinyint(4) default NULL,
  `RestingECG` varchar(10) default NULL,
  `MaxHR` int(11) default NULL,
  `ExerciseAngina` varchar(1) default NULL,
  `Oldpeak` float default NULL,
  `ST_Slope` varchar(10) default NULL,
  `HeartMRI` tinyint(4) default NULL,
  `CTScan` tinyint(4) default NULL,
  `Echocardiogram` tinyint(4) default NULL,
  `ChestXray` tinyint(4) default NULL,
  `Smoking` varchar(20) default NULL,
  `Troponin` float default NULL,
  `Angio_Blockage_Percent` float default NULL,
  `Answer` varchar(50) default NULL,
  `Prescription` text,
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `querytb1`
--

INSERT INTO `querytb1` (`ID`, `UserName`, `Age`, `Sex`, `ChestPainType`, `RestingBP`, `Cholesterol`, `FastingBS`, `RestingECG`, `MaxHR`, `ExerciseAngina`, `Oldpeak`, `ST_Slope`, `HeartMRI`, `CTScan`, `Echocardiogram`, `ChestXray`, `Smoking`, `Troponin`, `Angio_Blockage_Percent`, `Answer`, `Prescription`) VALUES
(1, 'admin', 21, '1', 'NAP', 350, 392, 1, 'ST', 130, 'Y', 2, 'Flat', 1, 1, 1, 1, 'Smoker', 0.145, 31.6, 'Heart Disease', 'Managing Glucose in T1D Once Had But One Treatment'),
(2, 'admin', 26, '0', 'NAP', 356, 2, 1, 'ST', 145, 'Y', 2, 'Flat', 1, 1, 1, 1, 'Smoker', 123, 12, 'Heart Disease', 'Managing Glucose in T1D Once Had But One Treatment');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=32 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `age`, `email`, `phone`, `location`, `address`, `uname`, `psw`) VALUES
(14, 'sundar', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'a123', 'a123'),
(17, 'sundar', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'admin', 'a234'),
(18, 'sample', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'admin12', 'admin12'),
(19, 'sundar', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'admin', '1234'),
(20, 'sam', '24', 'sundarv06@gmail.com', '9840234119', '621319', 'trichy', 'admin', 'admin'),
(21, 'sundar', '24', 'test@gmail.com', '9840234119', '621319', 'ttt', 'sqwe', 'sqwe'),
(22, 'sundar', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'admin12', 'admin12'),
(23, 'sundar', '26', 'SUNADRV06@GMAIL.COM', '7904467677', '456456', 'TRICHY', 'SWER', 'SWER'),
(24, 'sundar', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'admin1', 'admin1'),
(25, 'sam', '30', 'test@gmail.com', '9840234119', '621319', 'trichy', 'sam1234', 'sam1234'),
(26, 'sam', '24', 'test@gmail.com', '7904461600', '621319', 'trichy', 'admin', 'admin'),
(27, 'sundar', '24', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 'san', 'san'),
(28, 'sundar', '30', 'sundarv06@gmail.com', '7904461600', '621319', 'trichy', 's1234', 's1234'),
(29, 'sam', '30', 'test@gmail.com', '9840234119', '621319', 'trichy', 'sam', 'sam'),
(30, 'sample', '30', 'test@gmail.com', '9840234119', '621319', 'trichy', 'sample', 'sample'),
(31, 'anbu', '30', 'anbu@gmail.com', '1234560789', '620002', 'asdf', 'anbu86', 'anbu86');
