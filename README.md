# Burns Depression Checklist Package

This package provides two scripts, `run_checklist.py` and `print_db.py`, for running the Burns Depression Checklist and managing the results.

## Description

The Burns Depression Checklist is a self-report assessment used to measure the severity of depressive symptoms. The package includes two scripts: one for running the checklist and storing the results in a SQLite database, and another for reading the database and exporting the data as a CSV file.

## Dependencies

This package requires the following dependencies:

`pysqlite3`
`click`

You can install them using the following command:

```bash
pip install pysqlite3`
pip install click
```

## Usage

### Running the checklist

To run the Burns Depression Checklist and store the results in a database:

```bash
python run_checklist.py
```

This will prompt you with questions and store the results in a `depression_survey.db` SQLite database.

### Exporting the Results to CSV

To read the database and export the results to a CSV file:

```bash
python print_db.py
```
This will read the depression_survey.db database and save the results as a CSV file.

# License

This project is licensed under the MIT License.

# Author
`Tariq Mohamed <tariqmohamed59@gmail.com>`
