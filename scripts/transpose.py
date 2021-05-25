#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pandas as pd


def parser_setting():
    """Setting parser."""
    parser = argparse.ArgumentParser(prog='transpose.py',
                                     description='pd.T')
    parser.add_argument('path_in_matrix',
                        action='store',
                        type=str,
                        help='File path of matrix')
    parser.add_argument('-o', '--path_out_txt',
                        action='store',
                        type=str,
                        default="output.tsv",
                        help='File path of output tsv')
    args = parser.parse_args()
    return vars(args)


def main(args):
    # preprocess - read configs
    path_in_matrix = args["path_in_matrix"]
    path_out_txt = args["path_out_txt"]

    # main - input
    df = pd.read_csv(path_in_matrix, sep="\t", index_col=0, comment="#")

    # main - output
    df.T.to_csv(path_out_txt, sep="\t")


if __name__ == '__main__':
    main(parser_setting())
