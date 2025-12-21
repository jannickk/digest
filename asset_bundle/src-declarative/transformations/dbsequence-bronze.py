from pyspark import pipelines as dp
from pyspark.sql.functions import col

# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.

from pyspark.sql.types import *


schema = StructType(
                        [
                            StructField('_accession', StringType(), True), 
                            StructField('_id', StringType(), True), 
                            StructField('_searchDatabase_ref', StringType(), True), 
                            StructField('cvParam', ArrayType(
                                                            StructType(
                                                                        [
                                                                            StructField('_accession', StringType(), True),
                                                                            StructField('_cvRef', StringType(), True), 
                                                                            StructField('_name', StringType(), True), 
                                                                            StructField('_value', StringType(), True)]), 
                                                            True), 
                                        True),
                            StructField('source_file', StringType(), True),
                            StructField('file_size', StringType(), True)
                        ]
                    )

xml_tag_to_extract="DBSequence"
container="data" 
storage_account= "senjkdtbxloader"
storage_location = f"abfss://{container}@{storage_account}.dfs.core.windows.net/folder"


@dp.table
def dbsequence_bronze():
    return (
        spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "xml") \
        .option("rowTag", xml_tag_to_extract) \
        .schema(schema)\
        .load(storage_location) \
        .withColumn("source_file", col("_metadata.file_path")) \
        .withColumn("file_size", col("_metadata.file_size"))
    )
