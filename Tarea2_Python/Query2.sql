CREATE SCHEMA `people` ;

USE people;

CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
); 

INSERT INTO `people`.`employee` (`name`, `email`) 
VALUES ('Garcia', 'Garcia@gmail.com');
