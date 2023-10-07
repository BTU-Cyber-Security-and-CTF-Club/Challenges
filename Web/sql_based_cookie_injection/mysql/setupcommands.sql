-- create "flag" table
CREATE TABLE flag (flag VARCHAR(32) NOT NULL);
INSERT INTO flag VALUE("BTU{yayy_y0u_g0t_appl3_ic3}");

-- create all other tables
CREATE TABLE ice_flavors (flavors VARCHAR(32),quantity INT, price INT);
CREATE TABLE products (productId INT,productname VARCHAR(32),discount_percent INT, price INT,imagefile TEXT);
CREATE TABLE cakes_and_desserts (products VARCHAR(32),quantity INT, price INT);
CREATE TABLE soda (soda_flavor VARCHAR(32),quantity INT, price INT);

INSERT INTO ice_flavors VALUE("chocolate",90,60);
INSERT INTO ice_flavors VALUE("butterscotch",100,55);
INSERT INTO ice_flavors VALUE("strawberry",110,40);
INSERT INTO ice_flavors VALUE("vanilla",150,40);
INSERT INTO ice_flavors VALUE("mango",65,60);
INSERT INTO ice_flavors VALUE("strawberry",110,40);
INSERT INTO ice_flavors VALUE("pista",100,55);
INSERT INTO ice_flavors VALUE("banana",80,60);
INSERT INTO ice_flavors VALUE("mint chocolate chip",100,75);
INSERT INTO ice_flavors VALUE("cookie dough",100,70);
INSERT INTO ice_flavors VALUE("oreo",50,63);
INSERT INTO ice_flavors VALUE("coffee",75,80);
INSERT INTO ice_flavors VALUE("cotton candy",80,60);
INSERT INTO ice_flavors VALUE("peanut butter",50,75);
INSERT INTO ice_flavors VALUE("blueberry",100,88);
INSERT INTO ice_flavors VALUE("salted caramel",50,69);

INSERT INTO products VALUE(1,"milkshake",20,100,"milkshake.jpg");
INSERT INTO products VALUE(2,"ice cream cone",10,60,"icecream_cone.jpg");
INSERT INTO products VALUE(3,"popsicle",13,45,"popsicle.jpg");
INSERT INTO products VALUE(4,"shaved ice",15,50,"shaved_ice.jpg");
INSERT INTO products VALUE(5,"cookies",15,100,"cookies.jpg");
INSERT INTO products VALUE(6,"sundae",11,110,"sundae.jpg");
INSERT INTO products VALUE(7,"ice cream sandwich",19,35,"ice_cream_sandwich.jpg");
INSERT INTO products VALUE(8,"frozen yoghurt",13,60,"yoghurt.jpg");

INSERT INTO cakes_and_desserts VALUE("apple cake",500,300);
INSERT INTO cakes_and_desserts VALUE("black forest cake",500,450);
INSERT INTO cakes_and_desserts VALUE("white forest cake",500,400);
INSERT INTO cakes_and_desserts VALUE("red velvet cake",500,600);
INSERT INTO cakes_and_desserts VALUE("chocolate cake",500,400);
INSERT INTO cakes_and_desserts VALUE("cheesecake",500,450);
INSERT INTO cakes_and_desserts VALUE("strawberry pie",500,470);
INSERT INTO cakes_and_desserts VALUE("tiramisu",500,480);
INSERT INTO cakes_and_desserts VALUE("chocolate brownie",500,300);

INSERT INTO soda VALUE("coca cola",100,40);
INSERT INTO soda VALUE("cherry",100,50);
INSERT INTO soda VALUE("mango",100,65);
INSERT INTO soda VALUE("mixed fruit",100,50);
INSERT INTO soda VALUE("lemon",100,60);
INSERT INTO soda VALUE("guava",100,50);
INSERT INTO soda VALUE("grape",100,55);
INSERT INTO soda VALUE("passion fruit",100,60);
INSERT INTO soda VALUE("raspberry",100,65);
INSERT INTO soda VALUE("watermelon",100,60);

create user 'flask'@'%'identified by 'v5UmnxifRv';
-- reload privileges
FLUSH PRIVILEGES;
GRANT SELECT ON flask.* TO 'flask'@'%'; 
