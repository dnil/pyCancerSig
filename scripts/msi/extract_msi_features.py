#!/usr/bin/env python

import argparse
from cancersig.features.msi import MSIFeaturesExtractByBaseComposition

parser = argparse.ArgumentParser()

parser.add_argument('--raw_msisensor_report',
                    metavar="FILE",
                    dest='raw_msisensor_report',
                    help='an output from "msisensor msi" that have only msi score (percentage of MSI loci)',
                    required=True,
                    )
parser.add_argument('--raw_msisensor_somatic',
                    metavar="FILE",
                    dest='raw_msisensor_somatic',
                    help='an output from "msisensor msi" that have suffix "_somatic"',
                    required=True,
                    )
parser.add_argument('--sample_id',
                    dest='sample_id',
                    required=True,
                    )
parser.add_argument('--output_file',
                    metavar="FILE",
                    dest='output_file',
                    required=True,
                    )

args = parser.parse_args()
fe = MSIFeaturesExtractByBaseComposition()
fe.extract_features(args.raw_msisensor_report,
                    args.raw_msisensor_somatic,
                    args.sample_id,
                    args.output_file,
                    )
