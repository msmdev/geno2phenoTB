"""Tests of the geno2phenotb prediction package."""

import os
from tempfile import TemporaryDirectory

import pytest

import geno2phenotb.utils as utils
from geno2phenotb.geno2phenotb import main
from geno2phenotb.predict import predict

__author__ = "Bernhard Reuter, Jules Kreuer"
__copyright__ = "Bernhard Reuter, Jules Kreuer"
__license__ = "LGPL-3.0-only"


drugs_to_test = utils.get_drugs()


@pytest.mark.parametrize(
    "sample_id, run_main, drugs",
    [
        ("ERR067579", True, drugs_to_test),
        ("ERR067579", False, drugs_to_test),
        ("ERR551304", True, drugs_to_test),
        ("ERR551304", False, drugs_to_test),
        ("ERR553187", True, drugs_to_test),
        ("ERR553187", False, drugs_to_test),
    ],
)
def test_prediction(sample_id, run_main, drugs):
    """
    Tests the prediction steps excluding the preprocessing.

    Parameters
    ----------
        sample_id: str. Sample-ID of the already preprocessed files.
        run_main: bool. Should the call happen through the main function of geno2phenotb.
        drugs: List[str]. Drugs that should be tested.
    Returns
    ----------
        None.
    """
    dirname = utils.get_static_dir()

    # Use precomputed MTBSeq output.
    fastq_dir = os.path.join(
        dirname,
        "test_files",
        f"{sample_id}_pre",
    )

    ground_truth_dir = os.path.join(
        dirname,
        "ground_truth",
        sample_id,
    )

    with TemporaryDirectory(prefix="geno2phenotb_test_") as output_dir:
        if run_main:
            args = [
                "run",
                "-i",
                fastq_dir,
                "-o",
                output_dir,
                "--sample-id",
                sample_id,
                "--skip-mtbseq",
            ]

            for d in drugs:
                args.append("--drug")
                args.append(d)

            main(args)

        else:
            predict(
                fastq_dir,
                output_dir,
                sample_id,
                skip_mtbseq=True,
                drugs=drugs,
            )
        # Check prediction.
        utils.check_output(output_dir, ground_truth_dir, sample_id, only_preprocess=False)
