## Travel Bucket List

Build an app to track someone's travel adventures.

### MVP:

 * The app should allow the user to track countries and cities they want to visit and those they have visited.
 * The user should be able to create and edit countries
 * Each country should have one or more cities to visit
 * The user should be able to create and delete entries for cities
 * The app should allow the user to mark destinations as visited or still to see

### Possible Extensions:

 * Have separate pages for destinations visited and those still to visit
 * Add sights to the destination cities
 * Search for destination by continent, city or country
 * Any other ideas you might come up with

(1)Create  database   db/travel_bucket directory and make two files in it 
(i)run_sql.py (ii)db/travel_bucket.sql file to create tables
(2)In this travel_bucket project classes have single name, DB has plural names and controllers also have plural names.
(3)Use postico to check data is being saved
(4)Run python3 console.py command to check written data  values are being saved in db
(5)Use psql -d travel_bucket -f  db/travel_adventure.sql command to run queries
(6)Use flask run to run display data on browser