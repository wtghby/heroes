/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : heroes

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 21/02/2019 16:11:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hibernate_sequence
-- ----------------------------
DROP TABLE IF EXISTS `hibernate_sequence`;
CREATE TABLE `hibernate_sequence`  (
  `next_val` bigint(20) DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for tb_department
-- ----------------------------
DROP TABLE IF EXISTS `tb_department`;
CREATE TABLE `tb_department`  (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `rise` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '买入额',
  `fall` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '卖出额',
  `total` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '净额',
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '外键_股票代码',
  `ddate` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '日期',
  `type` tinyint(4) NOT NULL COMMENT '0-买入，1-卖出',
  `stock_id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '股票外键',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_stock_department`(`code`, `ddate`) USING BTREE,
  INDEX `ffk_stock_department`(`stock_id`) USING BTREE,
  CONSTRAINT `ffk_stock_department` FOREIGN KEY (`stock_id`) REFERENCES `tb_stock` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 11111 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for tb_stock
-- ----------------------------
DROP TABLE IF EXISTS `tb_stock`;
CREATE TABLE `tb_stock`  (
  `id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主键',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '价格',
  `increase` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '涨幅',
  `deal` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '成交额',
  `buy` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '净买额',
  `rise` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '买入额',
  `fall` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '卖出额',
  `reason` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '上榜原因',
  `code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '股票代码',
  `ddate` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `code`(`code`) USING BTREE,
  INDEX `code_2`(`code`, `ddate`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
