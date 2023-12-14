--creates user user_0d_1 tith privileges
    --user_0d_1 should ahve all privileges on MySQL server
    --user_0d_1 password should be set to user_0d_1_pwd
    --if the user_0d_1 exists, the script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
