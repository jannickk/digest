
from pyspark.sql.types import (
    StructType, StructField,
    StringType, DoubleType, LongType, BooleanType,
    ArrayType
)
from pyspark import pipelines as dp
from pyspark.sql.functions import col

schema = StructType([
    StructField(
        "SpectrumIdentificationItem",
        ArrayType(
            StructType([
                StructField(
                    "Fragmentation",
                    StructType([
                        StructField(
                            "IonType",
                            ArrayType(
                                StructType([
                                    StructField(
                                        "FragmentArray",
                                        ArrayType(
                                            StructType([
                                                StructField("_measure_ref", StringType(), True),
                                                StructField("_values", StringType(), True)
                                            ]),
                                            True
                                        ),
                                        True
                                    ),
                                    StructField("_charge", LongType(), True),
                                    StructField("_index", StringType(), True),
                                    StructField(
                                        "cvParam",
                                        ArrayType(
                                            StructType([
                                                StructField("_accession", StringType(), True),
                                                StructField("_cvRef", StringType(), True),
                                                StructField("_name", StringType(), True),
                                                StructField("_value", StringType(), True)
                                            ]),
                                            True
                                        ),
                                        True
                                    )
                                ]),
                                True
                            ),
                            True
                        )
                    ]),
                    True
                ),
                StructField(
                    "PeptideEvidenceRef",
                    ArrayType(
                        StructType([
                            StructField("_peptideEvidence_ref", StringType(), True)
                        ]),
                        True
                    ),
                    True
                ),
                StructField("_calculatedMassToCharge", DoubleType(), True),
                StructField("_chargeState", LongType(), True),
                StructField("_experimentalMassToCharge", DoubleType(), True),
                StructField("_id", StringType(), True),
                StructField("_passThreshold", BooleanType(), True),
                StructField("_peptide_ref", StringType(), True),
                StructField("_rank", LongType(), True),
                StructField(
                    "cvParam",
                    ArrayType(
                        StructType([
                            StructField("_accession", StringType(), True),
                            StructField("_cvRef", StringType(), True),
                            StructField("_name", StringType(), True),
                            StructField("_unitAccession", StringType(), True),
                            StructField("_unitCvRef", StringType(), True),
                            StructField("_unitName", StringType(), True),
                            StructField("_value", StringType(), True)
                        ]),
                        True
                    ),
                    True
                )
            ]),
            True
        ),
        True
    ),
    StructField("_id", StringType(), True),
    StructField("_spectraData_ref", StringType(), True),
    StructField("_spectrumID", StringType(), True),
    StructField(
        "cvParam",
        ArrayType(
            StructType([
                StructField("_accession", StringType(), True),
                StructField("_cvRef", StringType(), True),
                StructField("_name", StringType(), True),
                StructField("_unitAccession", StringType(), True),
                StructField("_unitCvRef", StringType(), True),
                StructField("_unitName", StringType(), True),
                StructField("_value", StringType(), True)
            ]),
            True
        ),
        True
    ),
    StructField("source_file", StringType(), False),
    StructField("file_size", LongType(), False)
])

xml_tag_to_extract="SpectrumIdentificationResult"
container="data" 
storage_account= "senjkdtbxloader"
storage_location = f"abfss://{container}@{storage_account}.dfs.core.windows.net/folder"

@dp.table
def spectrumidentificationresult_bronze():
    return (
        spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "xml") \
        .option("rowTag", xml_tag_to_extract) \
        .schema(schema)\
        .load(storage_location) \
        .withColumn("source_file", col("_metadata.file_path")) \
        .withColumn("file_size", col("_metadata.file_size"))
    )