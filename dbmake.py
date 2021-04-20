import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1234',
    db='busan'
)

sql = '''
CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`desc` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
sql_3 = "INSERT INTO `busan`.`topic` (`author`, `desc`, `title`) VALUES (%s, %s, %s);"
author = input("제목을 적으세요")
title = input("내용을 적으세요")
desc = input("누구세요?")
input_data = [author, title, desc]

cursor = db.cursor()
# cursor.execute(sql)
cursor.execute(sql_3, input_data)
db.commit()
db.close()

#cursor.execute('SELECT * FROM users;')
#users = cursor.fetchall()
# print(users)