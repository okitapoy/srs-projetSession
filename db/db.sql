create table user(
	id integer primary key,
	nom varchar(100),
	prenom varchar(100),
	email varchar(100),
	password varchar(100),
	unique(email)
);


create table groupe(
	id integer primary key,
	nom varchar(100),
	admin integer,
	montant integer,
	datePige text,
	foreign key (admin) references user(id)
);


create table participant(
	groupeId integer,
	id integer,
	foreign key (groupeId) references groupe(id),
	foreign key (id) references user(id)
);


create table cadeaux(
	cadeauId integer primary key,
	groupeId integer,
	userId integer,
	cadeau text,
	url text,
	foreign key (groupeId) references groupe(id),
	foreign key (userId) references user(id)
);



create table pige(
	groupeId integer,
	pigeur integer,
	aPige integer,
	foreign key (groupeId) references groupe(id),
	foreign key (pigeur) references user(id),
	foreign key (aPige) references user(id)
);



insert into user (nom,prenom,email,password) values("premier","user1","user1@email.com","password");
insert into user (nom,prenom,email,password) values("deuxieme","user2","user2@email.com","password");
insert into user (nom,prenom,email,password) values("troisieme","user3","user3@email.com","password");
insert into user (nom,prenom,email,password) values("quatrieme","user4","user4@email.com","password");
insert into user (nom,prenom,email,password) values("cinquieme","user5","user5@email.com","password");
insert into user (nom,prenom,email,password) values("sixieme","user6","user6@email.com","password");

insert into groupe (nom,admin,montant,datePige) values("groupe 11",1,100,"2020-12-10");
insert into groupe (nom,admin,montant,datePige) values("groupe 22",4,75,"2020-10-05");

insert into participant (groupeId,id) values(1,1);
insert into participant (groupeId,id) values(1,2);
insert into participant (groupeId,id) values(1,3);
insert into participant (groupeId,id) values(1,4);

insert into participant (groupeId,id) values(2,4);
insert into participant (groupeId,id) values(2,5);
insert into participant (groupeId,id) values(2,6);


insert into cadeaux (groupeId,userId,cadeau,url) values(1,1,"soulier addidas","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,1,"une montre","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,1,"ecouteur sans fil","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,2,"ballon de basket","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,2,"short de basket","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,2,"soulier de basket","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,3,"ecouteur sans fil","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,3,"ipod","https://www.amazon.ca/ref=ap_frn_logo");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,4,"chemise manches longues","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,4,"pantalon classique","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(1,4,"chausettes","https://www.amazon.ca");


insert into cadeaux (groupeId,userId,cadeau,url) values(2,4,"couteaux de cuisine","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,4,"set de casserole","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,4,"mixer pour smoothie","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,5,"pantalon de sport addidas","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,5,"soulier de sport addidas","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,5,"collant de sport addidas","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,6,"une montre","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,6,"ecouteur sans fil sony","https://www.amazon.ca");
insert into cadeaux (groupeId,userId,cadeau,url) values(2,6,"chausettes","https://www.amazon.ca");














