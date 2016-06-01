--
-- Table structure for table `stock`
--

CREATE TABLE IF NOT EXISTS `stock` (
  `id` int(4) unsigned NOT NULL,
  `code` char(6) NOT NULL COMMENT '股票代码',
  `name` varchar(255) DEFAULT '' COMMENT '股票名称',
  `date` date NOT NULL COMMENT '发行日期',
  `open` float unsigned NOT NULL DEFAULT '0' COMMENT '开盘价',
  `close` float unsigned NOT NULL DEFAULT '0' COMMENT '收盘价',
  `high` float unsigned NOT NULL DEFAULT '0' COMMENT '最高',
  `low` float unsigned NOT NULL DEFAULT '0' COMMENT '最低',
  `change` float NOT NULL DEFAULT '0',
  `change_rate` float NOT NULL DEFAULT '0',
  `volume` bigint(8) unsigned NOT NULL DEFAULT '0' COMMENT '成交量',
  `turnover` bigint(8) unsigned NOT NULL DEFAULT '0' COMMENT '成交额',
  `market_cap` int(4) unsigned NOT NULL DEFAULT '0' COMMENT '总市值',
  `cons_num` int(4) unsigned NOT NULL DEFAULT '0' COMMENT '?',
  `p_e1` float unsigned NOT NULL DEFAULT '0',
  `p_e2` float unsigned NOT NULL DEFAULT '0',
  `d_p1` float unsigned NOT NULL DEFAULT '0',
  `d_p2` float unsigned NOT NULL DEFAULT '0',
  `open_interest` int(4) DEFAULT NULL COMMENT '未平仓合约,期货交易空盘量',
  `settlement_turnover` int(4) DEFAULT NULL,
  `modified_duration` int(4) DEFAULT NULL,
  `convexity` int(4) DEFAULT NULL,
  `yield_to_maturity` int(4) DEFAULT NULL,
  `duration` int(4) DEFAULT NULL,
  `average_price` float unsigned DEFAULT '0',
  `net_price` float unsigned DEFAULT '0',
  `interest_reinvestment_price` int(4) DEFAULT NULL,
  `reserve` int(4) DEFAULT NULL,
  `created_at` datetime NOT NULL COMMENT '入库时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uk_code_date` (`code`,`date`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
