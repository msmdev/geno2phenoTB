============
Installation
============

There are several ways to install geno2phenoTB.
Directly from the bioconda channel, from PyPI using pip, or from the sources.

Bioconda / pip
--------------
To install geno2phenoTB 1.0.1 and above from the bioconda channel, a clean conda environment is
required:

.. code-block:: console

    # Required clean environment
    conda create -n g2p-tb
    conda activate g2p-tb

    # Installation
    conda install -c bioconda geno2phenoTB

If you want to install geno2phenoTB 1.0.0 from the bioconda channel, you need to create a conda
environment containing all dependencies beforehand. To do so, you need to checkout the source code
at the state of version 1.0.0 and create the required conda environment using the conda environment
file located in `tests/g2p-test.yaml`_:

.. code-block:: console

    # checkout the source code at 1.0.0
    git checkout 1.0.0

    # Required environment with all dependencies
    conda env create -f tests/g2p-test.yaml
    conda rename -n g2p-test g2p-tb
    conda activate g2p-tb

    # Installation
    conda install -c bioconda geno2phenoTB=1.0.0

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

The above will install the newest version. If you want to install an older version of geno2phenoTB,
you need to proceed as follows:

.. code-block:: console

    # checkout the source code at the desired version
    git checkout <version here>

    # Required environment with all dependencies
    conda env create -f tests/g2p-test.yaml
    conda rename -n g2p-test g2p-tb
    conda activate g2p-tb

    # Installation
    pip install geno2phenoTB==<version here>

Sources
-------
To install geno2phenoTB from the sources you need to:

* Download the repository.
* Install all dependencies into a new conda environment.
  They can be found in `tests/g2p-test.yaml`_.
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
