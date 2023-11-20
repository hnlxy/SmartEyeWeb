CREATE DATABASE smart_eye;
USE smart_eye;
CREATE TABLE `admins`(
    `username` varchar(32) primary key not null,
    `password` varchar(32) not null,
    `email` varchar(32) unique not null,
    `address` varchar(32),
    `gmt_create` datetime not null default now(),
    `gmt_update` datetime not null default now()
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
CREATE TABLE `monthly_info`(
    `date` DATETIME NOT NULL,
    `all_people` INT NOT NULL,
    `caregivers` INT NOT NULL,
    `available_beds` INT NOT NULL,
    `income` INT NOT NULL,
    `expenses` INT NOT NULL
);
ALTER TABLE
    monthly_info ADD PRIMARY KEY(`date`);
CREATE TABLE `users`(
    `user_id` VARCHAR(255) NOT NULL,
    `user_status` VARCHAR(255) NOT NULL,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `user_telephone` VARCHAR(255) NOT NULL,
    `user_address` VARCHAR(255) NOT NULL,
    `user_email` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `users` ADD PRIMARY KEY(`user_ID`);
CREATE TABLE `elder_expenses`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `elder_id` VARCHAR(255) NOT NULL,
    `elder_name` VARCHAR(255) NOT NULL,
    `payment` INT NOT NULL,
    `pay_date` DATETIME NOT NULL
);
CREATE TABLE `guardians`(
    `guardian_id` VARCHAR(255) NOT NULL,
    `guardian_name` VARCHAR(255) NOT NULL,
    `guardian_phone` VARCHAR(255) NOT NULL,
    `guardian_gender` ENUM('') NOT NULL,
    `guardian_address` VARCHAR(255) NOT NULL,
    `relation` VARCHAR(255) NOT NULL,
    `remark` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `guardians` ADD PRIMARY KEY(`guardian_id`);
CREATE TABLE `elders`(
    `elder_id` VARCHAR(255) NOT NULL,
    `elder_name` VARCHAR(255) NOT NULL,
    `elder_gender` ENUM('') NOT NULL,
    `elder_phone` VARCHAR(255) NOT NULL,
    `elder_address` VARCHAR(255) NOT NULL,
    `elder_birth` DATETIME NOT NULL,
    `assign_caregiver` VARCHAR(255) NOT NULL,
    `level_care` ENUM('') NOT NULL,
    `room_number` VARCHAR(255) NOT NULL
    );
ALTER TABLE
    `elders` ADD PRIMARY KEY(`elder_id`);
CREATE TABLE `announcements`(
    `announcement_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(255) NOT NULL,
    `content` VARCHAR(255) NOT NULL,
    `publication_date` DATETIME NOT NULL
);
CREATE TABLE `elder_guardian`(
    `elder_id` VARCHAR(255) NOT NULL,
    `guardian_id` VARCHAR(255) NOT NULL
);
ALTER TABLE
    elder_guardian ADD PRIMARY KEY(`elder_id`, `guardian_id`);
CREATE TABLE `caregivers`(
    `caregiver_id` VARCHAR(255) NOT NULL,
    `caregiver_name` VARCHAR(255) NOT NULL,
    `caregiver_phone` VARCHAR(255) NOT NULL,
    `caregiver_address` VARCHAR(255) NOT NULL,
    `hired_date` BIGINT NOT NULL,
    `caregiver_gender` ENUM('') NOT NULL,
    `caregiver_email` VARCHAR(255) NOT NULL,
    `caregiver_department` VARCHAR(255) NOT NULL,
    `experience` VARCHAR(255) NOT NULL,
    `photo` BINARY(16) NOT NULL,
    `qualification_photo` BINARY(16) NOT NULL
);
ALTER TABLE
    `caregivers` ADD PRIMARY KEY(`caregiver_id`);
CREATE TABLE `elder_health`(
    `elder_id` VARCHAR(255) NOT NULL PRIMARY KEY,
    `blood_pressure` DOUBLE NOT NULL,
    `blood_oxygen` DOUBLE NOT NULL,
    `blood_glucose` DOUBLE NOT NULL,
    `heart_rate` INT NOT NULL,
    `water_intake` DOUBLE NOT NULL
);
ALTER TABLE
    elder_guardian ADD CONSTRAINT `elder_guardian_elders_id_foreign` FOREIGN KEY(`elder_id`) REFERENCES `elders`(`elder_id`);
ALTER TABLE
    `elders`
    ADD CONSTRAINT `elders_elder_health_id_foreign` FOREIGN KEY(`elder_id`) REFERENCES elder_health(`elder_id`);
ALTER TABLE
    `elders` ADD CONSTRAINT `elders_caregivers_foreign` FOREIGN KEY(`assign_caregiver`) REFERENCES `caregivers`(`caregiver_id`);