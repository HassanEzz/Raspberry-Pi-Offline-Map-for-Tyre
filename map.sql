-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: map
-- ------------------------------------------------------
-- Server version	5.5.47-0+deb7u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tyr`
--

DROP TABLE IF EXISTS `tyr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tyr` (
  `name` text,
  `pic` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tyr`
--

LOCK TABLES `tyr` WRITE;
/*!40000 ALTER TABLE `tyr` DISABLE KEYS */;
INSERT INTO `tyr` VALUES ('Map 1','1.png'),('Map 2','2.png'),('Map 3','3.png'),('Map 4','4.png'),('Map 5','5.png'),('sliemart-jawad1','6.png'),('sliemart-jawad2','7.png'),('sliemart-bittar_station','8.png'),('tyr-blc_bank','9.png'),('tyr port-blc bank','10.png'),('tyr port-municipality tyr','11.png'),('rest house-red cross','12.png'),('route preview1','13.png'),('farhat pharmacy-south Tech1','14.png'),('farhat pharmacy-south Tech2','16.png'),('route preview2','16.png'),('route preview3','17.png'),('route preview4','18.png'),('route preview5','19.png'),('route preview6','20.png'),('route preview7','21.png'),('route preview8','22.png'),('rest house-DVD nasser','23.png'),('route preview9','24.png');
/*!40000 ALTER TABLE `tyr` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-25 19:35:11
