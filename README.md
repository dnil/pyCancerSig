# pyCancerSig
## A python package for deciphering cancer signatures.

Comprehensive cancer signatures with a main workflow in nextflow, and reusable modules written in python.
Integrate SNV, SV and MSI profiles in signatures decomposed using non-negative matrix factorisation, and produce production ready pdf reports. 

### Main workflow usage

    =========================================
              Cancer Signature Workflow
    =========================================
    Usage:
    The typical command for running the pipeline is as follows:
    nextflow run --bam_pair '/path/to/folder/with/bam/pairs/*-{normal,tumor}.bam' --somatic_snv_vcf /path/to/folder/with/somatic/snv/vcfs/*.vcf.gz --somatic_sv_vcf /path/to/folder/with/somatic/sv/vcfs/*.vcf --reference GRCh37.fa --project sens2010123
    Mandatory arguments:
      --bam_pair                    Path to input tumor-normal bam (must be surrounded with quotes)
      --somatic_snv_vcf             Path to input somatic single nucleotide variant in vcf format
      --somatic_sv_vcf              Path to input somatic structural variant in vcf format
      --reference                   Reference file used when the bams were aligned. Currently, the workflow assume that all bams were aligned using the same reference
      --project                     SLURM project code

    Optional arguments:
    MSI
      --microsates                  Homopolymer and microsates file required by msisensor
      --save_msi                    Save the MSI files - not done by default
    TiTv
      --save_titv                   Save the TiTv files - not done by default
    features
      --save_features               Save the joined features files - not done by default
    model
      --min_signatures              Minimum number of signatures in model construction
      --max_signatures              Maximum number of signatures in model construction
    Others:
      --freq_cutoff                 Cut-off criteria for variants to be included in the profile
      --out_dir                     The output directory where the results will be saved
      
### Installation 

    ./install.sh

or 

    python setup.py install
    
or 

    pip install .
    
### Setup

#### (Optional): Edit nexflow.config

#### (Optional): Prepare genome files

#### (Optional): FindSV installation

#### (Optional): MSIsensor installation

