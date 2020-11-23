BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text ,phone text, website text, regdata text);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-1234-5678','Kim.com','2020-11-21 19:26:16');
INSERT INTO "users" VALUES(2,'Lee','Lee@naver.com','010-1234-5678','Lee.com','2020-11-21 19:39:28');
INSERT INTO "users" VALUES(3,'Park','Park@naver.com','010-0000-0003','Park.com','2020-11-21 19:44:10');
INSERT INTO "users" VALUES(4,'Choi','Choi@naver.com','010-0000-0004','Choi.com','2020-11-21 19:44:10');
INSERT INTO "users" VALUES(5,'Jung','Jung@naver.com','010-0000-0005','Jung.com','2020-11-21 19:44:10');
COMMIT;
