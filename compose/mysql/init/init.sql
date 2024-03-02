#Alter user 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
#ALTER USER 'admin'@'%' IDENTIFIED WITH caching_sha2_password BY 'password';
GRANT ALL PRIVILEGES ON myproject.* TO 'admin'@'%';
FLUSH PRIVILEGES;
