======================
Command Line Interface
======================

The command-line interface (CLI) offers two modes: a self-test mode and a run mode.

.. contents:: Table of Contents


Run Mode
--------

This mode is used to predict atibiotic resistance of Mycobacterium tuberculosis.
The primary run command has several options:

.. code-block:: console

    geno2phenotb run [-h] [--skip-mtbseq] [-p] -i DIR -o DIR
                    --sample-id SampleID
                    [-d DrugCode]

Options:

    - -h, \--help
    - \--skip-mtbseq
    - -p, \--preprocess
    - -i, \--fastq-dir
    - -o, \--output
    - \--sample-id
    - -d, \--drug

Below is a description of each option:

-h, \--help
^^^^^^^^^^^
Show the help message and exit.

\--skip-mtbseq
^^^^^^^^^^^^^^
Skip the MTBseq step. Precomputed output must be present in the specified FASTQ directory.

-p, \--preprocess
^^^^^^^^^^^^^^^^^
Run only the preprocessing steps. The FASTQ reads will be assembled using MTBseq and features
extracted. This will skip the prediction.

-i DIR, \--fastq-dir DIR
^^^^^^^^^^^^^^^^^^^^^^^^
Path to the input directory where the FASTQ files are located.

As input, a directory with FASTQ files is required.
The FASTQ files must follow this naming scheme:

.. code-block:: text

    [SampleID]_[LibID]_[*]_[Direction].f(ast)q.gz
                        ^- Optional values.
    Direction must be one of R1, R2.

-o DIR, \--output DIR
^^^^^^^^^^^^^^^^^^^^^
Path to the directory where the final output files should be stored.

\--sample-id SampleID
^^^^^^^^^^^^^^^^^^^^^
SampleID (i.e., ERR/SRR run accession). The ID should match with the ID of the FASTQ files.

-d DrugCode, \--drug DrugCode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The drug for which resistance should be predicted. If you want predictions for several drugs,
use the argument several times, i.e., --d AMK --d DCS --d STR. If the flag is not set,
predictions for all drugs will be performed.

The DrugCode is a 2 / 3 letter code and can be one of:

.. code-block:: text

    AMK, CAP, DCS, EMB, ETH, FQ, INH, KAN, PAS, PZA, RIF, STR


Examples
--------

Predict the resistance of the sample (ERR551304) against all drugs:

.. code-block:: console

 $ geno2phenotb run -i dir_to_ERR551304/ -o output_dir/ --sample-id ERR551304

Predict only the resistance against AMK and RIF:

.. code-block:: console

 $ geno2phenotb run -i dir_to_ERR551304/ -o output_dir/ --sample-id ERR551304 -d AMK -d RIF

Skip the MTBseq steps and use the precomputed output:

.. code-block:: console

     $ geno2phenotb run -i dir_to_precomputed/ -o output_dir/ --sample-id ERR551304 --skip-mtbseq

Self-test mode
--------------

To check the integrity of the installation and dependencies, a self-test can be executed.
It does NOT guarantee that everything is okay, but is strong evidence:

.. code-block:: console

    geno2phenotb test [-h] (-f | -c)

The available options for the self-test mode are:

    - -h, \--help
    - -f, \--fast
    - -c, \--complete

Descriptions of the self-test mode options:

-h, \--help
^^^^^^^^^^^
Show the help message and exit.

-f, \--fast
^^^^^^^^^^^
Fast test of the installation. This will not test the preprocessing / MTBSeq steps.

-c, \--complete
^^^^^^^^^^^^^^^
Complete test of the installation. This will download ~170 MB from the ENA and start a complete
run. Depending on your bandwidth / hardware, this may take a few (5-30) minutes.

Examples
--------
To run the complete test (recommended) run:

.. code-block:: console

     $ geno2phenotb test -c
