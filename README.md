

---

# File Upload Utility

## Overview

The File Upload Utility is a Python script designed to read CSV files from a specified directory and upload them to a MySQL database table. It retrieves MySQL connection details from a JSON configuration file.

## Prerequisites

- Python 3.x
- pandas
- sqlalchemy

Install the required dependencies using:

```bash
pip install pandas sqlalchemy
```

## Usage

1. Clone the repository or download the script `file_upload.py`.

2. Navigate to the directory containing the script.

3. Run the script with the following command:

   ```bash
   python file_upload.py --source_dir <source_directory_path> --destination_table <destination_table_name>
   ```

   Replace `<source_directory_path>` with the path to the directory containing CSV files and `<destination_table_name>` with the name of the MySQL table.

4. The script will prompt for MySQL connection details through a JSON file named `mysql_config.json` in the source directory. Make sure to create this file with the following structure:

   ```json
   {
       "host": "localhost",
       "port": "3306",
       "user": "your_username",
       "password": "your_password",
       "database": "your_database_name"
   }
   ```

5. The script will read all CSV files in the specified directory and upload them to the specified MySQL table.

## Example

```bash
python file_upload.py --source_dir /path/to/csv/files --destination_table my_table
```

## Notes

- Ensure that the MySQL server is running and accessible from the machine where the script is executed.
- The script uses the `pandas` library to read CSV files and the `sqlalchemy` library to establish a connection with the MySQL database.

---

