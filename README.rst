

.. image:: https://img.shields.io/conda/vn/conda-forge/geno2phenoTB.svg
    :alt: Conda-Forge
    :target: https://anaconda.org/conda-forge/geno2phenoTB

.. image:: https://github.com/msmdev/geno2phenoTB/actions/workflows/ci.yml/badge.svg
    :alt: Test status
    :target: https://github.com/msmdev/geno2phenoTB/actions/workflows/ci.yml

.. image:: https://readthedocs.org/projects/geno2phenoTB/badge/?version=latest
    :alt: ReadTheDocs
    :target: https://geno2phenoTB.readthedocs.io/en/stable/

.. image:: https://api.juleskreuer.eu/citation-badge.php?doi=DOI
    :alt: Citation count
    :target: https://juleskreuer.eu/projekte/citation-badge/

============
geno2phenoTB
============

    geno2phenoTB is a machine learning based tool to predict resistance of *Mycobacterium
    tuberculosis* against antibiotics using whole-genome sequencing data.

Approximately 182.000 (range 113.000-250.000) patients die each year from tuberculosis (TB) caused
by a multidrug-resistant (MDR) or rifampicin-resistant (RR) strain of the *Mycobacterium
tuberculosis* complex (MTBC). The design of a MDR/RR-TB regimen requires detailed knowledge about
resistance against second-line anti-tuberculosis drugs. Performing phenotypic drug susceptibility
tests (DST) for multiple anti-tuberculosis drugs is time-consuming, laborious, and for some drugs
impossible. |br|
Next generation sequencing (NGS) techniques are on the verge to replace phenotypic methods by
predicting drug susceptibility and resistance based on mutation catalogs. NGS can be performed on
direct patient specimen and results are available within days. Advances in machine learning (ML)
techniques allow unbiased predictions from genotype to phenotype within minutes. We combined state-
of-the-art expertise in ML and genome-based resistance diagnostics to develop an engine that
predicts drug resistance profiles from whole genome sequencing (WGS) data.

We used genomic data, augmented with genotypic data (generated using a state-of-the-art resistance
mutation catalog (see [Grobbel21_] and [Finci22_]) of the Research Center Borstel - Leibniz
Lung Center (FZB)), from a database we curated of more than 18000 WGS samples with phenotypic DST
labels to train ML models capable of predicting drug resistance from WGS data. |br|
To find the best performing drug-specific models, different supervised learning methods such as
rule-based classifiers (RBC) utilizing Boolean compressed sensing, gradient-boosted trees (GBT),
logistic regression (LR), and random forests (RF) were compared. |br|
In greater detail, we employed a 10-fold repeated nested stratified 5-fold cross-validation (CV)
protocol to train the models and to assess their performance. This included tuning of the model
hyper-parameters on the inner CV folds. In case of GBT, LR, and RF models, they were tuned for
maximum average precision (AP_) on the inner CV folds, while the classifiers decision threshold
was tuned for optimal F1 score on the training partition of the outer CV fold. In case of RBC
models, they were tuned for maximum Matthews correlation coefficient (MCC), while no decision
threshold tuning was applied, since RBC deliver simple OR-rules. |br|
To make the models more understandable and increase confidence in the resulting predictions,
either inherently interpretable models like RBC were used or model-intrinsic feature importance
values are output. |br|
Results for 5 first-generation drugs (ethambutol, isoniazid, pyrazinamide, rifampicin,
streptomycin) and 7 second-generation drugs (amikacin, capreomycin, cycloserine, fluoroquinolones,
kanamycin, paraaminosalicylic acid, thioamides) show that the trained prediction models exhibit
comparable or better resistance prediction performance than a current resistance mutation catalog
of the FZB.

Finally, the best ML model for each of the 12 drugs was selected and implemented in a TB
resistance prediction engine. This constitutes the core of the geno2phenoTB package complemented
by state-of-the-art continuous integration and automatic deployment.
The geno2phenoTB package is mainly written in Python, hosted on GitHub, and can be easily and
directly installed via the common package manager conda. |br|
Further, geno2phenoTB integrates a complete NGS data processing pipeline, namely MTBSeq, starting
from raw reads given via FASTQ files. Since the processing step is computationally intensive,
a tool that can be installed locally (e.g., on a workstation or supercomputer), like geno2phenoTB,
offers the advantage, compared to web-based tools, of being able to scale the execution as needed
and process even thousands of samples in parallel and, thus, quickly.

.. _AP: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
.. _Grobbel21: https://pubmed.ncbi.nlm.nih.gov/33900387/
.. _Finci22: https://doi.org/10.1016/S2666-5247(22)00116-1

.. |br| raw:: html

  <br/>

Installation
============

To install geno2phenoTB from the bioconda channel a clean conda environment is required:

.. code-block:: console

    # Required clean environment
    conda create -n g2p-tb
    conda activate g2p-tb

    # Installation
    conda install -c bioconda geno2phenoTB

For the installation directly from the source, please refer to the documentation.

Basic Usage
===========
Two interfaces of geno2phenoTB are exposed. A CLI and a python interface.
Both require the path to a directory containing FASTQ files belonging to a single sample as input.
Under the hood we use MTBseq_ for the analysis of next generation sequencing data in the form of
FASTQ files from single end (one FASTQ file) or paired end (two FASTQ files) sequencing runs
(tested for Illumina and Ion Torrent files).

The FASTQ files must follow this naming scheme:

.. code-block:: text

    [SampleID]_[LibID]_[*]_[Direction].f(ast)q.gz
                        ^- Optional values.
    Direction must be one of R1, R2.
    Example: ERR551304_X_R1.fastq.gz

Here, [SampleID] represents the identifier for a specific bacterial sample and [LibID] is an
identifier (e.g., for the next generation sequencing library used). [Direction] is an essential
field and indicates if reads are in forward (R1) or reverse (R2) orientation in paired end data.
Files for single end data have to use the [Direction] R1. Other than these, file names can be
freely given, including further [*] fields.

Command-Line-Interface
----------------------
The CLI offers two modes. The run mode is used to predict the resistance:

.. code-block:: console

    geno2phenotb run [-h] -i DIR -o DIR [-p] --sample-id SampleID

      -h,     show the help message
      -i DIR, Path to the directory were the FASTQ files are located.
      -o DIR  Path to the directory were the final output files shall be stored.
      --sample-id SampleID,  SampleID (i.e. ERR/SRR run accession).

More advanced arguments / options are available and can be found in the
:todo link to readthedocs `CLI-documentation <cli-usage>`.

Example
*******

To predict the resistance of the sample (`ERR551304`) against all drugs use:

.. code-block:: console

    geno2phenotb run -i dir_to_ERR551304/ -o output_dir/ --sample-id ERR551304

Python Interface
----------------
Import geno2phenotb and use the :mod:`geno2phenotb.predict.predict` function of the
:mod:`geno2phenotb.predict` submodule:

.. code-block:: console

    Parameters:

    fastq_dir : str
        Path to directory containing the fastq files.
    output_dir : str
        Path to output directory.
    sample_id : str
        Sample ID.
    skip_mtbseq : bool, default=False
        Do not run MTBSeq  but use preprocessed data.
    drugs : Union[str, list], default=None
        If None, drug resistance predictions for all drugs known to geno2phenoTB are determined.
        If a list of drugs is supplied, predictions will be only determined for these. The drug
        must be one of 'AMK', 'CAP', 'DCS', 'EMB', 'ETH', 'FQ', 'INH', 'KAN', 'PAS', 'PZA', 'RIF',
        'STR'.

    Returns:

    result : pd.DataFrame
        A DataFrame with the probabilities (for resistance) and predictions (1.0 for resistance, 0.0 for susceptibility) for the requested drugs.
    feature_evaluation : pd.DataFrame
        A DataFrame listing the features (called variants, lineage classification, genotypes) plus
        an assessment of the relevance of each feature for the Machine-Learning-based and catalog
        based resistance prediction per drug. For each drug, two columns are given: '<drug>
        feature importance' and '<drug> catalog resistance variant'. The first contains the
        feature importance value derived from the Machine Learning model, the second informs if
        the variant is a known catalog resistance variant for the considered drug.
    rules : Dict[str, Optional[list[str]]]
        Dict of lists with features constituting a rule. If the used Machine Learning Model is a
        Rule-Based Classifier, rules[drug] is a list of features constituting a rule (the rule can
        be constructed by connecting the given features with boolean 'or' operators
        (disjunctions)). Otherwise, rules[drug]=None.

For the complete description refer to the
:todo link to readthedocs `Python Module Reference <api/modules>`.

Acknowledgments
===============

We would like to thank the EU for funding within the EU Horizon 2020 research and innovation
program project CARE_.
Further, Bernhard Reuter would like to thank the `Tübingen AI Center`_ for funding his work.
Special thanks go to `Nico Pfeifer`_ from the University of Tübingen and `Matthias Merker`_ and
`Jan Heyckendorf`_ from the Research Center Borstel – Leibniz Lung Center for their untiring
support.
They supplied data and expertise that was crucial for this project.
We would like to thank Nico Pfeifer, `Rolf Kaiser`_, and the whole geno2pheno_ team who laid
the mental foundation for this project by their creative and groundbreaking work on the original
geno2pheno tool.
Furthermore, we would like to thank `Francesca Incardona`_ and the people from the EuResist_
network for their efforts to initiate the CARE project.
Finally, we would like to thank all the talented people that were involved in the CARE project
for their great effort and work.

.. _MTBseq: https://github.com/ngs-fzb/MTBseq_source
.. _CARE: https://www.careresearch.eu/
.. _Tübingen AI Center: https://tuebingen.ai/
.. _Nico Pfeifer: https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/methods-in-medical-informatics/team/nico-pfeifer/
.. _Matthias Merker: https://www.dzif.de/de/matthias-merker
.. _Jan Heyckendorf: https://www.dzif.de/de/jan-heyckendorf
.. _Rolf Kaiser: https://virologie.uk-koeln.de/institut/direktor-team/bereichsleitungen/
.. _geno2pheno: https://www.geno2pheno.org/
.. _Francesca Incardona: https://phd.uniroma1.it/web/FRANCESCA-INCARDONA_nC2953_IT.aspx
.. _EuResist: https://www.euresist.org/
