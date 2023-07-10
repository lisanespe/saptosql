import csv
import click

@click.command()
@click.option('--Table', type=str, prompt='Wich table?', help='Table name')
@click.option('--Path', type=str, prompt='Wich path?')
def generate_create_statement(Path, Table):
    '''Takes a file with Integration Services Metada and transform in a SQL Create Statemet '''
    with open(file_path, 'r', encoding="utf8") as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header row

        create_statement = "CREATE TABLE {Table} (\n"

        for row in reader:
            column_name = row[0].strip('"')
            data_type = row[1].strip('"')
            precision = int(row[2].strip('"'))
            scale = int(row[3].strip('"'))
            length = int(row[4].strip('"'))

            sql_data_type = ''
            if data_type == 'DT_WSTR':
                sql_data_type = f'NVARCHAR({length})'
            elif data_type == 'DT_I2':
                sql_data_type = 'SMALLINT'
            elif data_type == 'DT_NUMERIC':
                sql_data_type = f'DECIMAL({precision}, {scale})'
            elif data_type == 'DT_DBTIMESTAMP':
                sql_data_type = 'DATETIME'
            elif data_type == 'DT_I4':
                sql_data_type = 'INT'

            create_statement += f'    {column_name:<25} {sql_data_type:<25} NULL,\n'

        create_statement = create_statement.rstrip(
            ',\n')  # Remove the last comma
        create_statement += "\n);"

        return create_statement

if __name__ == "__main__":
    generate_create_statement()

# Example usage
# FilePath = 'sap.txt'
# create_statement = generate_create_statement(FilePath,TableName)
# with open("create.txt", "wt",encoding="utf8") as f:
#   print(create_statement, file = f)
