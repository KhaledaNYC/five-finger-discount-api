django:

./manage.py makemigrations
./manage.py migrate
./manage.py showmigrations
./manage.py shell_plus



Postgres stuff:

dropdb {dbname}
createdb {dbname}
pg_dump -U {username} {dbname} > {dbname}.psql
