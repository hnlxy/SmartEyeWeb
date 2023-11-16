-- CREATE DATABASE smart_eye;
USE smart_eye;
CREATE TABLE `monthly_info`(
    `日期` DATETIME NOT NULL,
    `住院人数` INT NOT NULL,
    `护工人数` INT NOT NULL,
    `剩余床位` INT NOT NULL,
    `收入` INT NOT NULL,
    `支出` INT NOT NULL
);
ALTER TABLE
    monthly_info ADD PRIMARY KEY(`日期`);
CREATE TABLE `users`(
    `用户ID` VARCHAR(255) NOT NULL,
    `监护人ID` VARCHAR(255) NOT NULL,
    `账户状态` TINYINT(1) NOT NULL,
    `用户名` VARCHAR(255) NOT NULL,
    `密码` VARCHAR(255) NOT NULL,
    `电话号码` VARCHAR(255) NOT NULL,
    `地址` VARCHAR(255) NOT NULL,
    `出生日期` DATETIME NOT NULL,
    `邮箱` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `users` ADD PRIMARY KEY(`用户ID`);
CREATE TABLE `elder_expense`(
    `长者ID` VARCHAR(255) NOT NULL,
    `长者姓名` VARCHAR(255) NOT NULL,
    `押金（元）` INT NOT NULL,
    `缴费记录（元）` INT NOT NULL,
    `缴费时间` DATETIME NOT NULL
);
ALTER TABLE
    elder_expense ADD PRIMARY KEY(`长者ID`);
CREATE TABLE `guardians`(
    `监护人ID` VARCHAR(255) NOT NULL,
    `监护人姓名` VARCHAR(255) NOT NULL,
    `电话号码` VARCHAR(255) NOT NULL,
    `性别` ENUM('') NOT NULL,
    `地址` VARCHAR(255) NOT NULL,
    `关系` VARCHAR(255) NOT NULL,
    `备注` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `guardians` ADD PRIMARY KEY(`监护人ID`);
CREATE TABLE `elders`(
    `长者ID` VARCHAR(255) NOT NULL,
    `长者姓名` VARCHAR(255) NOT NULL,
    `性别` ENUM('') NOT NULL,
    `电话号码` VARCHAR(255) NOT NULL,
    `家庭住址` VARCHAR(255) NOT NULL,
    `入住日期` DATETIME NOT NULL,
    `分配护工` VARCHAR(255) NOT NULL,
    `护理级别` ENUM('') NOT NULL,
    `房间号` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `elders` ADD PRIMARY KEY(`长者ID`);
CREATE TABLE `announcements`(
    `公告id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `标题` VARCHAR(255) NOT NULL,
    `正文` VARCHAR(255) NOT NULL,
    `发布时间` DATETIME NOT NULL
);
CREATE TABLE `elder_guardian`(
    `监护人id` VARCHAR(255) NOT NULL,
    `长者id` VARCHAR(255) NOT NULL
);
ALTER TABLE
    elder_guardian ADD PRIMARY KEY(`监护人id`, `长者id`);
CREATE TABLE `caregivers`(
    `护工ID` VARCHAR(255) NOT NULL,
    `姓名` VARCHAR(255) NOT NULL,
    `联系电话` VARCHAR(255) NOT NULL,
    `地址` VARCHAR(255) NOT NULL,
    `出生年月` DATETIME NOT NULL,
    `录用日期` BIGINT NOT NULL,
    `性别` ENUM('') NOT NULL,
    `邮箱` VARCHAR(255) NOT NULL,
    `部门` VARCHAR(255) NOT NULL,
    `经历` VARCHAR(255) NOT NULL,
    `头像照` BINARY(16) NOT NULL,
    `资格照` BINARY(16) NOT NULL
);
ALTER TABLE
    `caregivers` ADD PRIMARY KEY(`护工ID`);
CREATE TABLE `elder_health`(
    `长者ID` VARCHAR(255) NOT NULL PRIMARY KEY,
    `血压(收缩压kpa/舒张压kpa)` DOUBLE NOT NULL,
    `血氧(%)` DOUBLE NOT NULL,
    `血糖(空腹mmol/L/餐后mmol/L)` DOUBLE NOT NULL,
    `心率(次/分)` INT NOT NULL,
    `饮水量(mL)` DOUBLE NOT NULL
);
ALTER TABLE
    `users` ADD CONSTRAINT `users_guardians_id_foreign` FOREIGN KEY(`监护人ID`) REFERENCES `guardians`(`监护人ID`);
ALTER TABLE
    elder_guardian ADD CONSTRAINT `elder_guardian_elders_id_foreign` FOREIGN KEY(`长者id`) REFERENCES `elders`(`长者ID`);
ALTER TABLE
    `elders` ADD CONSTRAINT `elders_elder_expense_id_foreign` FOREIGN KEY(`长者ID`) REFERENCES elder_expense(`长者ID`);
ALTER TABLE
    `elders`
    ADD CONSTRAINT `elders_elder_health_id_foreign` FOREIGN KEY(`长者ID`) REFERENCES elder_health(`长者ID`);
ALTER TABLE
    `elders` ADD CONSTRAINT `elders_caregivers_foreign` FOREIGN KEY(`分配护工`) REFERENCES `caregivers`(`护工ID`);