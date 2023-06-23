============
Installation
============

There are two ways of installing geno2phenoTB.
Directly from the bioconda channel or from the sources.

Bioconda
--------
To install geno2phenoTB from bioconda a clean conda environment is required:

.. code-block:: console

    # Required clean environment
    conda create -n g2p-tb
    conda activate g2p-tb

    # Installation
    conda install -c bioconda geno2phenoTB

While we recommend to install geno2phenoTB from bioconda, it can be installed using pip as well.
If you prefer to install using pip, you need to make sure that all requirements are fulfilled.
The simplest and recommended way in doing so is to create a conda environment containing all
dependencies (using the conda environment file located in `tests/g2p-test.yaml`_) before
installing geno2phenoTB via pip:

.. code-block:: console

    # Required environment with all dependencies
    conda env create -f tests/g2p-test.yaml
    conda rename -n g2p-test g2p-tb
    conda activate g2p-tb

    # Installation
    pip install geno2phenoTB

Sources
-------
To install geno2phenoTB from the sources you need to:

* Download the repository.
* Install all dependencies into a new conda environment. They can be found in `tests/g2p-test.yaml`.
* Install the module using pip:

.. code-block:: console

    # Download sources
    git clone https://github.com/msmdev/geno2phenoTB
    cd geno2phenoTB

    # Install dependencies and rename environment
    conda env create -f tests/g2p-test.yaml
    conda rename -n g2p-test g2p-tb
    conda activate g2p-tb

    # Install module using pip
    pip install .

.. _tests/g2p-test.yaml: https://github.com/msmdev/geno2phenoTB/blob/main/tests/g2p-test.yaml
