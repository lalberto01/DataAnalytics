/*
a) Actor_id, first_name, last_name, last_update
b) Film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update
c) film_actor
d) Rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. No because the information uses mostly ID numbers.
e) inventory_id, film_id, store_id, last-update
f) In order to understand the names of all films on a specific date you would need to use the rental, inventory, and film tables. The rental table identifies the rental date and  inventory id. The inventory table contains inventory_id and film_id. The film table will use film_id to understand the names of the film.
SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
*/
