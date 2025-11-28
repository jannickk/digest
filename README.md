
# DIGEST

**D**ata Warehouse of **I**dentifications of Proteins and Peptides from **G**enomes by means of Mass **S**pectrometry **T**echnology

This project uses Databricks Autoloader and Spark Structured Streaming to parse mzIdentML files from Azure storage accounts to Delta Tables.
 

All project resources are deployed Databricks Asset Bundles.


## References
Jones AR, Eisenacher M, Mayer G, Kohlbacher O, Siepen J, Hubbard SJ, Selley JN, Searle BC, Shofstahl J, Seymour SL, Julian R, Binz PA, Deutsch EW, Hermjakob H, Reisinger F, Griss J, Vizcaíno JA, Chambers M, Pizarro A, Creasy D. The mzIdentML data standard for mass spectrometry-based proteomics results. Mol Cell Proteomics. 2012 Jul;11(7):M111.014381. doi: 10.1074/mcp.M111.014381. Epub 2012 Feb 27. PMID: 22375074; PMCID: PMC3394945.


### Metadata Curation.

The tables and columns are annotated with the following metadata



**bronze.peptide_evidence**

table description:

All peptide and protein matches which also contain decoy peptides which are included in the search in order to estimate the False Discovery rate.

column descriptin:

- _id: The id of the peptide-protein match which corresponds to the id of the XML document
- _dBSequence_ref: The reference to the protein in table dbsequence
- _end:  The end position of the peptide within the matched protein
- _isDecoy: Whether or not the peptide is a decoy peptide
- _peptide_ref: The reference to the peptide to the peptide of the peptide table
- _post: The amino acid immediately after the peptide sequence in the macthed protein
- _pre: The amino acid immediately preceeding the peptide sequence in the matched protein
- _start: The start position of the peptide in the protein of this peptide-protein match
- source_file: The absolute filesystem path of the library
- file_size: The size of the library

**silver.peptide_evidence**

table desciption:

This table contains all possible assignments of identified peptides to proteins of the search database. One entry corresponds to a peptide/protein pair. In comparison to the bronze table, all decoy peptides were removed the table. 

- _id: The id of the peptide-protein match which corresponds to the id of the XML document
- _dBSequence_ref: The reference to the protein in table dbsequence
- _end:  The end position of the peptide within the matched protein
- _isDecoy: Whether or not the peptide is a decoy peptide
- _peptide_ref: The reference to the peptide to the peptide of the peptide table
- _post: The amino acid immediately after the peptide sequence in the matched protein
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
- source_file: The library from which the data were extracted
- file_size: The file size of the library
- protein_description: A description of the protein from the annotation of the corresponding sequence


**bronze.spectrumidentifcationresult**

table description:

Each row contains a spectrum from the set of acquisitions which were used to build the library. The peptide-spectrum matches that could be established for a spectrum are contained in the array of column SpectrumIdentificationItem.

column description:

- _id : The id of the entry. This id corresponds to the the id attribute of the SpectrumIdentificationResult XML element from the library file
- _spectrumID: The locally unique id for the spectrum in the spectra data set specified by _spectraData_ref. This is the spectrum from which the identications are made. 
- _spectraData_ref: A data set containing spectra data (consisting of one or more spectra). 
- cvParam: An array of controlled vocabulatory terms that serve as metadata to the spectrum
- source_file: The library file from which the data were extracted. Each file corresponds to exactly one library. 
- file_size: The size of library in bytes
- SpectrumIdentificationItem: This column contains an array for each spectrum which contains all Peptide-Spectrum matches that could be established for the spectrum of that row 



**silver.spectrumidentifcationresult**

table description:

Each row of this table corresponds to an identified fragment ion from a Mass spectrum. The peptide precursor ion is indicated by the charge state and the experimental mass to charge ratio. The identied peptide is referenced by the peptide_reference column. The spectrum in which the identifcation is made is indicated by the _spectrumID. If there are two peptide_references for one spectrum, there are two peptide-spectrum matches (PSM) for that spectrum

column description:

- _id : The id of the entry. This id corresponds to the the id attribute of the SpectrumIdentificationResult XML element from the library file
- _spectrumID: The locally unique id for the spectrum in the spectra data set specified by _spectraData_ref. This is spectrum from which the identicationss are made. 
- _spectraData_ref: A data set containing spectra data (consisting of one or more spectra). 
- source_file: The library file from which the data were extracted. Each file corresponds to exactly one library. 
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

This table contains all discovered peptides with identified chemical modifications.

column description:

- Modification: An array of all discovered chemical modifications on the peptide
- PeptideSequence:  The sequence of the peptide using single letter amino acid code
- _id: The id of the peptide. This id corresponds to the id attribute of the corresponding xml attribute
- source_file: The absolute path of the protein library from which the data were extracted
- file_size: The size of the library


**silver.peptide**

table description:

This table contains one row for each combination of modification and peptide. If a peptide has two different modifications, two rows exist for that peptide.
This table is derived from the bronze.peptide library by exploding the modification array.

column descriptions:

- _id: The XML id of the peptide
- PeptideSequence: The Sequence of the identified Peptide
- source_file: The source file from which the data were extracted
- file_size: The size of the library file from which the peptides were read
- massDelta: The mass difference introduced by the modification in comparison to the unmodified peptide.
- location: The location of the modified amino acid within the peptide sequence
- residues: The modified residue
- cv_accession_number: The accession number of modification in the referenced controlled vocabulatory
- cvname: The name of the controlled vocabulatory entry, i.e. the actual name of the modification


 