from pyspark import pipelines as dp
from pyspark.sql.functions import col

from pyspark.sql.types import *

schema = StructType(
                    [
                        StructField('_dBSequence_ref', StringType(), True), 
                        StructField('_end', LongType(), True), 
                        StructField('_id', StringType(), True), 
                        StructField('_isDecoy', BooleanType(), True), 
                        StructField('_peptide_ref', StringType(), True), 
                        StructField('_post', StringType(), True), 
                        StructField('_pre', StringType(), True), 
                        StructField('_start', LongType(), True),
                        StructField('source_file', StringType(), True), 
                        StructField('file_size', LongType(), True),
                     ]
                    )
xml_tag_to_extract="PeptideEvidence"

container="data" 
storage_account= "senjkdtbxloader"


storage_location = f"abfss://{container}@{storage_account}.dfs.core.windows.net/folder"


@dp.table
def peptide_evidence_bronze():

  return (
             spark.readStream.format("cloudFiles") \
            .option("cloudFiles.format", "xml") \
            .option("rowTag", xml_tag_to_extract) \
            .schema(schema)\
            .load(storage_location) \
            .withColumn("source_file", col("_metadata.file_path")) \
            .withColumn("file_size", col("_metadata.file_size"))
        )