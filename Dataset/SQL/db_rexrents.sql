-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2025 at 06:59 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_rexrents`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_akun`
--

CREATE TABLE `tb_akun` (
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('Admin','Employee') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_akun`
--

INSERT INTO `tb_akun` (`username`, `password`, `role`) VALUES
('admin', 'admin', 'Admin'),
('pegawai', 'pegawai', 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `tb_mobil`
--

CREATE TABLE `tb_mobil` (
  `id_mobil` char(3) NOT NULL,
  `model` varchar(255) NOT NULL,
  `merk` varchar(255) NOT NULL,
  `hargasewa` float DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `biaya_maintenance` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_mobil`
--

INSERT INTO `tb_mobil` (`id_mobil`, `model`, `merk`, `hargasewa`, `status`, `foto`, `biaya_maintenance`) VALUES
('M01', '520i G30', 'BMW', 2000000, 1, '1_520.png', 200000),
('M02', 'X3', 'BMW', 2000000, 1, '2_x3.png', 200000),
('M03', 'Xenia', 'Daihatsu', 300000, 1, '3_xenia.png', 30000),
('M04', 'Brio', 'Honda', 250000, 1, '4_brio.png', 25000),
('M05', 'Mobilio', 'Honda', 250000, 1, '5_mobilio.png', 25000),
('M06', 'Civic', 'Honda', 500000, 1, '6_civic.png', 50000),
('M07', 'Jazz', 'Honda', 300000, 1, '7_jazz.png', 30000),
('M08', 'HR-V', 'Honda', 500000, 0, '8_hrv.png', 50000),
('M09', 'City', 'Honda', 400000, 0, '9_city.png', 40000),
('M10', 'Xpander', 'Mitsubishi', 600000, 1, '10_xpander.png', 60000),
('M11', 'Stargazer', 'Hyundai', 450000, 1, '11_stargazer.png', 45000),
('M12', 'Ioniq 5', 'Hyundai', 1200000, 1, '12_ioniq.png', 120000),
('M13', 'Agya', 'Toyota', 250000, 1, '13_agya.png', 25000),
('M14', 'Calya', 'Toyota', 200000, 1, '14_calya.png', 20000),
('M15', 'Fortuner', 'Toyota', 1200000, 1, '15_fortuner.png', 120000),
('M16', 'Avanza', 'Toyota', 300000, 1, '16_avanza.png', 30000),
('M17', 'Rush', 'Toyota', 400000, 1, '17_rush.png', 40000),
('M18', 'Yaris', 'Toyota', 400000, 1, '18_yaris.png', 40000),
('M19', 'Zenix', 'Toyota', 600000, 1, '19_zenix.png', 60000),
('M20', 'Innova', 'Toyota', 800000, 1, '20_innova.png', 80000),
('M21', 'Camry', 'Toyota', 1000000, 1, '21_camry.png', 100000),
('M22', 'Hiace', 'Toyota', 1500000, 1, '22_hiace.png', 150000),
('M23', 'Alphard', 'Toyota', 2700000, 1, '23_alphard.png', 270000),
('M24', 'Swift', 'Suzuki', 280000, 1, '24_swift.png', 28000),
('M25', 'Ertiga', 'Suzuki', 300000, 1, '25_ertiga.png', 30000),
('M26', 'Aventador', 'Lamborghini', 9000000, 1, '26_aventador.png', 900000),
('M27', 'Chiron', 'Bugatti', 15000000, 1, '27_chiron.png', 1500000),
('M28', 'M4', 'BMW', 5000000, 1, '', 500000);

--
-- Triggers `tb_mobil`
--
DELIMITER $$
CREATE TRIGGER `hitung_biaya_maintenance` BEFORE INSERT ON `tb_mobil` FOR EACH ROW BEGIN
   SET NEW.biaya_maintenance = NEW.hargasewa * 0.10;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tb_pelanggan`
--

CREATE TABLE `tb_pelanggan` (
  `id_pelanggan` char(4) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `noHP` varchar(255) NOT NULL,
  `noKTP` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `gender` enum('L','P') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_pelanggan`
--

INSERT INTO `tb_pelanggan` (`id_pelanggan`, `nama`, `noHP`, `noKTP`, `alamat`, `gender`) VALUES
('P001', 'Andi Saputra', '081234567801', '3201123456780001', 'Jl. Melati No.12, Jakarta', 'L'),
('P002', 'Raka Pratama', '081234567802', '3201123456780002', 'Jl. Tegal Parang Selatan No.43, Jakarta', 'L'),
('P003', 'Halim Santoso', '081234567803', '3201123456780003', 'Jl. Anggrek No.5, Bandung', 'L'),
('P004', 'Laila Azzahra', '081234567804', '3201123456780004', 'Jl. Harapan No.21, Depok', 'P'),
('P005', 'Rafi Ahmad', '081234567805', '3201123456780005', 'Jl. Kebon Jeruk No.17, Jakarta', 'L'),
('P006', 'Satria Hidayat', '081234567806', '3201123456780006', 'Jl. Mawar No.3, Bekasi', 'L'),
('P007', 'Falah Putri', '081234567807', '3201123456780007', 'Jl. Kenanga No.8, Bogor', 'P'),
('P008', 'Agus Salim', '081234567808', '3201123456780008', 'Jl. Cemara No.10, Tangerang', 'L'),
('P009', 'Rafi Ahmad', '081234567805', '3201123456780005', 'Jl. Kebon Jeruk No.17, Jakarta', 'L'),
('P010', 'Niko Ramadhan', '081231020861', '3172021607000002', 'Jl. Puri Mas No.15, Bekasi', 'L'),
('P011', 'Dian Sastro', '08123456809', '3201123456780009', 'Jl. Dahlia No.25, Jakarta', 'P'),
('P012', 'Budi Santoso', '08123456810', '3201123456780010', 'Jl. Anggrek No.15, Tangerang', 'L'),
('P013', 'Maya Putri', '08123456811', '3201123456780011', 'Jl. Melati No.8, Bekasi', 'P'),
('P014', 'Rizky Pratama', '08123456812', '3201123456780012', 'Jl. Kencana No.32, Jakarta', 'L'),
('P015', 'Siti Nurhaliza', '08123456813', '3201123456780013', 'Jl. Mawar No.45, Depok', 'P'),
('P016', 'Ahmad Fadli', '08123456814', '3201123456780014', 'Jl. Teratai No.17, Bogor', 'L'),
('P017', 'Nina Wulandari', '08123456815', '3201123456780015', 'Jl. Kenanga No.21, Jakarta', 'P'),
('P018', 'Eko Prasetyo', '08123456816', '3201123456780016', 'Jl. Flamboyan No.9, Tangerang', 'L'),
('P019', 'Dewi Safitri', '08123456817', '3201123456780017', 'Jl. Tulip No.28, Bekasi', 'P'),
('P020', 'Hadi Wijaya', '08123456818', '3201123456780018', 'Jl. Bougenville No.12, Jakarta', 'L'),
('P021', 'Indra Kurniawan', '08123456819', '3201123456780019', 'Jl. Cendana No.11, Jakarta', 'L'),
('P022', 'Sari Melinda', '08123456820', '3201123456780020', 'Jl. Sawo No.7, Bandung', 'P'),
('P023', 'Yusuf Maulana', '08123456821', '3201123456780021', 'Jl. Rambutan No.19, Depok', 'L'),
('P024', 'Nadia Permata', '08123456822', '3201123456780022', 'Jl. Durian No.6, Bekasi', 'P'),
('P025', 'Bagus Prasetya', '08123456823', '3201123456780023', 'Jl. Belimbing No.10, Tangerang', 'L'),
('P026', 'Putri Ayu', '08123456824', '3201123456780024', 'Jl. Mangga No.14, Bogor', 'P'),
('P027', 'Dimas Saputra', '08123456825', '3201123456780025', 'Jl. Alpukat No.2, Jakarta', 'L'),
('P028', 'Mega Rahayu', '08123456826', '3201123456780026', 'Jl. Pisang No.18, Bekasi', 'P'),
('P029', 'Fikri Ramadhan', '08123456827', '3201123456780027', 'Jl. Nangka No.20, Tangerang', 'L'),
('P030', 'Ayu Lestari', '08123456828', '3201123456780028', 'Jl. Pepaya No.9, Depok', 'P'),
('P031', 'Aryajaya Alamsyah', '085156821462', '3272061807060002', 'Jl. Puri Depok Mas', 'L'),
('P032', 'Halim Hulian', '0814234567890', '32760610801912012', 'Jl. Tegal Parang 5', 'L');

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi`
--

CREATE TABLE `tb_transaksi` (
  `id_transaksi` char(7) NOT NULL,
  `tanggal` datetime NOT NULL,
  `id_pelanggan` char(4) NOT NULL,
  `id_mobil` char(3) NOT NULL,
  `denda` int(11) DEFAULT NULL,
  `durasi` int(11) NOT NULL,
  `total_harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_transaksi`
--

INSERT INTO `tb_transaksi` (`id_transaksi`, `tanggal`, `id_pelanggan`, `id_mobil`, `denda`, `durasi`, `total_harga`) VALUES
('TRX0001', '2025-04-28 00:00:00', 'P001', 'M09', 0, 3, 400000),
('TRX0002', '2025-04-29 00:00:00', 'P002', 'M10', 0, 2, 600000),
('TRX0003', '2025-04-30 00:00:00', 'P003', 'M11', 0, 4, 450000),
('TRX0004', '2025-05-01 00:00:00', 'P004', 'M12', 0, 2, 1200000),
('TRX0005', '2025-05-02 00:00:00', 'P005', 'M13', 0, 5, 250000),
('TRX0006', '2025-05-03 00:00:00', 'P006', 'M18', 0, 3, 400000),
('TRX0007', '2025-05-04 00:00:00', 'P007', 'M25', 0, 7, 300000),
('TRX0008', '2025-04-30 00:00:00', 'P005', 'M27', 0, 9, 180000000),
('TRX0009', '2025-05-11 00:00:00', 'P002', 'M22', 0, 12, 18000000),
('TRX0010', '2025-05-11 00:00:00', 'P002', 'M22', 0, 12, 18000000),
('TRX0011', '2025-05-11 00:00:00', 'P002', 'M22', 0, 12, 18000000),
('TRX0012', '2025-05-11 00:00:00', 'P002', 'M22', 0, 12, 18000000),
('TRX0013', '2025-05-11 00:00:00', 'P002', 'M22', 0, 12, 18000000),
('TRX0014', '2025-05-11 00:00:00', 'P002', 'M22', 0, 12, 18000000),
('TRX0015', '2025-05-11 00:00:00', 'P003', 'M24', 0, 3, 840000),
('TRX0016', '2025-05-11 00:00:00', 'P001', 'M01', 9000000, 2, 13000000),
('TRX0017', '2025-05-11 00:00:00', 'P004', 'M02', 0, 2, 4000000),
('TRX0018', '2025-05-11 00:00:00', 'P007', 'M14', 0, 10, 2000000),
('TRX0019', '2025-05-11 00:00:00', 'P006', 'M27', 0, 4, 60000000),
('TRX0020', '2025-05-11 00:00:00', 'P003', 'M26', 0, 5, 45000000),
('TRX0021', '2025-05-11 00:00:00', 'P004', 'M23', 0, 1, 2700000),
('TRX0022', '2025-05-11 00:00:00', 'P005', 'M21', 0, 3, 3000000),
('TRX0023', '2025-05-11 00:00:00', 'P006', 'M20', 0, 7, 5600000),
('TRX0024', '2025-05-11 00:00:00', 'P002', 'M19', 0, 17, 10200000),
('TRX0025', '2025-05-11 00:00:00', 'P010', 'M15', 0, 4, 4800000),
('TRX0026', '2025-05-11 00:00:00', 'P008', 'M17', 0, 5, 2000000),
('TRX0027', '2025-05-11 00:00:00', 'P001', 'M01', 0, 1, 2000000),
('TRX0028', '2025-05-11 00:00:00', 'P002', 'M27', 22500000, 2, 52500000),
('TRX0029', '2025-05-11 00:00:00', 'P010', 'M01', 3000000, 3, 9000000),
('TRX0030', '2025-05-11 00:00:00', 'P002', 'M01', 6000000, 4, 14000000),
('TRX0031', '2025-05-18 00:00:00', 'P006', 'M01', 0, 1, 2000000),
('TRX0032', '2025-05-19 00:00:00', 'P001', 'M07', 0, 3, 900000),
('TRX0033', '2025-05-20 00:00:00', 'P003', 'M01', 0, 1, 2000000),
('TRX0034', '2025-05-23 00:00:00', 'P002', 'M01', 0, 1, 2000000),
('TRX0035', '2025-05-23 00:00:00', 'P003', 'M02', 0, 30, 60000000),
('TRX0036', '2025-05-23 00:00:00', 'P003', 'M02', 0, 30, 60000000),
('TRX0037', '2025-05-23 00:00:00', 'P003', 'M27', 0, 30, 450000000),
('TRX0038', '2025-05-23 00:00:00', 'P004', 'M27', 0, 30, 450000000),
('TRX0039', '2025-05-23 00:00:00', 'P010', 'M27', 0, 30, 450000000),
('TRX0040', '2025-05-26 00:00:00', 'P005', 'M09', 0, 4, 1600000),
('TRX0041', '2025-05-26 00:00:00', 'P002', 'M02', 0, 1, 2000000),
('TRX0042', '2025-05-26 00:00:00', 'P031', 'M27', 6000000, 3, 501000000),
('TRX0043', '2025-05-27 00:00:00', 'P021', 'M08', 0, 11, 5500000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_akun`
--
ALTER TABLE `tb_akun`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `tb_mobil`
--
ALTER TABLE `tb_mobil`
  ADD PRIMARY KEY (`id_mobil`);

--
-- Indexes for table `tb_pelanggan`
--
ALTER TABLE `tb_pelanggan`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indexes for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_pelanggan` (`id_pelanggan`),
  ADD KEY `id_mobil` (`id_mobil`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD CONSTRAINT `tb_transaksi_ibfk_1` FOREIGN KEY (`id_pelanggan`) REFERENCES `tb_pelanggan` (`id_pelanggan`),
  ADD CONSTRAINT `tb_transaksi_ibfk_2` FOREIGN KEY (`id_mobil`) REFERENCES `tb_mobil` (`id_mobil`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
