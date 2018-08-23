-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'order'
-- 订单（用户点了哪些菜）
-- ---
DROP TABLE IF EXISTS `order`;
		
CREATE TABLE `order` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `foodName` VARCHAR(100) NOT NULL DEFAULT '自助餐',
  PRIMARY KEY (`id`)
) COMMENT '订单（用户点了哪些菜）';

-- ---
-- Foreign Keys 
-- ---


-- ---
-- Table Properties
-- ---

-- ALTER TABLE `order` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `order` (`id`,`foodName`) VALUES
-- ('','');
