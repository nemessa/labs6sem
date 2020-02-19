CREATE TABLE IF NOT EXISTS processors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    price INTEGER,
    clock INTEGER,
    cores INTEGER,
    threads INTEGER,
    l1_cache INTEGER,
    l2_cache INTEGER,
    l3_cache INTEGER,
    process_t INTEGER,
    balance INTEGER
);

CREATE TABLE IF NOT EXISTS clients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    date_order DATE
);

CREATE TABLE IF NOT EXISTS basket(
    id SERIAL PRIMARY KEY,
    id_processor INTEGER REFERENCES processors(id) ON DELETE CASCADE ON UPDATE CASCADE,
    quantity INTEGER,
    id_client INTEGER REFERENCES clients(id) ON DELETE CASCADE ON UPDATE CASCADE,
    id_order INTEGER REFERENCES orders(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO "public"."processors" 
("id", "name", "price", "clock", "cores", "threads", "l1_cache", "l2_cache", "l3_cache", "process_t", "balance")
VALUES (DEFAULT, 'AMD Ryzen 5 3600 Boxed', 185, 3600, 6, 12, null, null, 32, 12, 7);
INSERT INTO "public"."processors" 
("id", "name", "price", "clock", "cores", "threads", "l1_cache", "l2_cache", "l3_cache", "process_t", "balance")
VALUES (DEFAULT, 'AMD Ryzen 5 3600X Boxed', 219, 3800, 6, 12, null, null, 32, 12, 5);
INSERT INTO "public"."processors" 
("id", "name", "price", "clock", "cores", "threads", "l1_cache", "l2_cache", "l3_cache", "process_t", "balance")
VALUES (DEFAULT, 'AMD Ryzen 5 2600', 119, 3400, 6, 12, null, null, 16, 14, 20);
INSERT INTO "public"."processors" 
("id", "name", "price", "clock", "cores", "threads", "l1_cache", "l2_cache", "l3_cache", "process_t", "balance")
VALUES (DEFAULT, 'Intel Core i5-9600KF', 214, 3700, 6, 6, null, null, 9, 14, 11);
INSERT INTO "public"."processors" 
("id", "name", "price", "clock", "cores", "threads", "l1_cache", "l2_cache", "l3_cache", "process_t", "balance")
VALUES (DEFAULT, 'Intel Core i5-9600K', 255, 3700, 6, 6, null, null, 9, 14, 8);
INSERT INTO "public"."processors" 
("id", "name", "price", "clock", "cores", "threads", "l1_cache", "l2_cache", "l3_cache", "process_t", "balance")
VALUES (DEFAULT, 'Intel Core i5-9400F', 162, 2900, 6, 6, null, null, 9, 14, 15);

INSERT INTO "public"."clients" ("id", "name") VALUES (DEFAULT, 'Mark')
INSERT INTO "public"."clients" ("id", "name") VALUES (DEFAULT, 'Adam')
INSERT INTO "public"."clients" ("id", "name") VALUES (DEFAULT, 'Kurt')
INSERT INTO "public"."clients" ("id", "name") VALUES (DEFAULT, 'Lindemann')

INSERT INTO "public"."orders" ("id", "date_order") VALUES (DEFAULT, null)
INSERT INTO "public"."orders" ("id", "date_order") VALUES (DEFAULT, null)
INSERT INTO "public"."orders" ("id", "date_order") VALUES (DEFAULT, null)

INSERT INTO "public"."basket" ("id", "id_processor", "quantity", "id_client", "id_order")
VALUES (DEFAULT, 1, 3, 1, 1)
INSERT INTO "public"."basket" ("id", "id_processor", "quantity", "id_client", "id_order")
VALUES (DEFAULT, 3, 1, 1, 1)
INSERT INTO "public"."basket" ("id", "id_processor", "quantity", "id_client", "id_order")
VALUES (DEFAULT, 2, 2, 2, 2)
INSERT INTO "public"."basket" ("id", "id_processor", "quantity", "id_client", "id_order")
VALUES (DEFAULT, 4, 1, 3, 3)