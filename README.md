
# DIGEST

**D**ata Warehouse of **I**dentifications of Proteins and Peptides from **G**enomes by means of Mass **S**pectrometry **T**echnology

This project uses Databricks Autoloader and Spark Structured Streaming to parse mzIdentML files from Azure storage accounts to Delta Tables.
 


All project resources are deployed Databricks Asset Bundles.


## References
Jones AR, Eisenacher M, Mayer G, Kohlbacher O, Siepen J, Hubbard SJ, Selley JN, Searle BC, Shofstahl J, Seymour SL, Julian R, Binz PA, Deutsch EW, Hermjakob H, Reisinger F, Griss J, Vizcaíno JA, Chambers M, Pizarro A, Creasy D. The mzIdentML data standard for mass spectrometry-based proteomics results. Mol Cell Proteomics. 2012 Jul;11(7):M111.014381. doi: 10.1074/mcp.M111.014381. Epub 2012 Feb 27. PMID: 22375074; PMCID: PMC3394945.


### Metadata Curation.

The tables and columns are annotated with the following metadata


**silver.peptide_evidence**

table desciption:

This table contains all possible assignments of identified peptides to proteins of the search database. One entry corresponds to a peptide/protein pair.

- _id: The id of the peptide-protein match which corresponds to the 
- _dBSequence_ref: The reference to the protein in table dbsequence
- _end:  The end position of the peptide within the matched protein
- _isDecoy: Whether or not the peptide is a decoy peptide
- _peptide_ref: The reference to the peptide to the peptide of the peptide table
- _post: The amino acid immediately after the peptide sequence in the macthed protein
- _pre: The amino acid immediately preceeding the peptide sequence in the matched protein
- _start: The start position of the peptide in the protein of this peptide-protein match
- source_file: The absolute filesystem path of the library
- file_size: The size of the library


**silver.dbsequence**

table description:

The table contains all identified proteins from the experimental mass spectra included in the search.

The columns are annotated in the following way:

- _accession : The accession numer under which the dbsequence can be found in the search database
- _id: The id of the entry. This ID corresponds to the id attribute of the corresponding XML element in the library file
- searchDatabase_ref: The search database against which identification are performed
- source_file: The library
- file_size: The file size of the library
- protein_description: A description of the protein from the annotation of the corresponding sequence


**silver.spectrumidentifcationresult**

table description:

Each row of this table corresponds to a fragment ion of the peptide that was identified from the spectrum. The peptide and the spectrum reference are given in separate columns. If there are two peptide_references for one spectrum, there are two peptide-spectrum matches (PSM).


column description:


- _id : The id of the entry. This id corresponds to the the id attribute of the SpectrumIdentificationResult XML element from the library file
- _spectrumID: The locally unique id for the spectrum in the spectra data set specified by _spectraData_ref. This is spectrum from which the identicationss are made. 
- _spectraData_ref: A data set containing spectra data (consisting of one or more spectra). 
- source_file: The library file from which the entity was extracted.
- file_size: The size of library in bytes
- peptide_reference: The reference to the peptide that was identified from the spectrum
- calculated_mass_to_charge: The calculated mass to charge ratio of the peptide ion precurosr adduct that was identified
- experimental_mass_to_charge: The experimenal mass to charge ratio of the peptide ion precursor
- charge_state: The charge of the peptide ion precursor
- pass_threshold: Whether or not the identified peptide meets identification confidence criteria
- fragment_mz: The mz value of the fragment ion
- fragment_name: The name of the fragment using established nomenclature
- charge: The charge of the fragment ion
- y_ion: Whether or not the fragment ion is an y-ion
- b_ion: Whether or not the fragment ion is an b-ion
- immonium_ion: whether or not the fragment ion is an immonium ion
- neutral_loss_chemical_formula: The neutral loss formula of the peptide ion precursor

**bronze.peptide**

table description:

This table contains all discovered peptides with identified posttranslational modifications


column description:

- Modification: An array of all discovered posttranslational modifications on the peptide
- PeptideSequence:  The sequence of the peptide using single letter amino acid code
- _id: The id of the peptide. This id corresponds to the id attribute of the corresponding xml attribute
- source_file: The absolute path of the protein library
- file_size: The size of the library in bytes





 