#!/bin/bash

# Get the directory where the script resides
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Try to locate the test.env file
if [ -f "$DIR/test.env" ]; then
  source "$DIR/test.env"
elif [ -f "$DIR/../test.env" ]; then
  source "$DIR/../test.env"
else
  echo "Error: test.env file not found."
  exit 1
fi

# Try to locate the create_table.sql file
if [ -f "$DIR/create_table.sql" ]; then
  SQL_FILE="$DIR/create_table.sql"
elif [ -f "$DIR/../create_table.sql" ]; then
  SQL_FILE="$DIR/../create_table.sql"
else
  echo "Error: create_table.sql file not found."
  exit 1
fi

# Run the appropriate command based on the database type
case $1 in
  1)
    mysql -h $HOSTNAME -u $USERNAME -p$PASSWORD $DATABASE_NAME < $SQL_FILE # removed space between -p and $PASSWORD
    ;;
  2)
    export PGPASSWORD=$PASSWORD
    psql -h $HOSTNAME -U $USERNAME -d $DATABASE_NAME -f $SQL_FILE
    ;;
  3)
     sqlite3 "$DIR/$DATABASE_NAME.db" < $SQL_FILE
    ;;
  *)
    echo "Error: Invalid argument. Please provide 1 for MySQL, 2 for PostgreSQL, or 3 for SQLite."
    exit 1
    ;;
esac

echo "Table creation script executed successfully."
