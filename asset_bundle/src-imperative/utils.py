
# Create table from dataframe
from pyspark.sql import DataFrame
from pyspark.sql.types import *


def create_table(spark, df: DataFrame, table_name:str):
    ddl = ", ".join([f"{field.name} {field.dataType.simpleString()}" for field in df.schema.fields])
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({ddl})"
    spark.sql(sql)


def create_table_from_schema(spark,schema: StructType, table_name:str):

    ddl = ", ".join([f"{field.name} {field.dataType.simpleString()}" for field in schema.fields])
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({ddl})"
    print(sql)
    spark.sql(sql)