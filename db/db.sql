create table user(
	id integer primary key,
	nom varchar(100),
	prenom varchar(100),
	email varchar(100),
	password varchar(100)
);


create table groupe(
	id integer primary key,
	nom varchar(100),
	admin integer,
	participant integer,
	foreign key (admin) references user(id),
	foreign key (participant) references user(id)
);



insert into user (nom,prenom,email,password) values("premier","user1","user1@email.com","password");
insert into user (nom,prenom,email,password) values("deuxieme","user2","user2@email.com","password");
insert into user (nom,prenom,email,password) values("troisieme","user3","user3@email.com","password");
insert into user (nom,prenom,email,password) values("quatrieme","user4","user4@email.com","password");
insert into user (nom,prenom,email,password) values("cinquieme","user5","user5@email.com","password");
insert into user (nom,prenom,email,password) values("sixieme","user6","user6@email.com","password");



insert into groupe (nom,admin,participant) values("groupe 11",1,1);
insert into groupe (nom,admin,participant) values("groupe 11",1,2);
insert into groupe (nom,admin,participant) values("groupe 11",1,3);
insert into groupe (nom,admin,participant) values("groupe 11",1,4);

insert into groupe (nom,admin,participant) values("groupe 22",4,4);
insert into groupe (nom,admin,participant) values("groupe 22",4,5);
insert into groupe (nom,admin,participant) values("groupe 22",4,6);
