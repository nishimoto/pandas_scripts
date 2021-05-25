#!/usr/bin/env python
# -*- coding: utf-8 -*-
import warnings
import argparse
import pandas as pd
warnings.filterwarnings('ignore')


def parser_setting():
    """Setting parser."""
    parser = argparse.ArgumentParser(prog='concat.py',
                                     description='description')
    parser.add_argument('path_in_matrixs',
                        action='store',
                        nargs="*",
                        type=str,
                        help='File path of matrix')
    parser.add_argument('-o', '--path_out_txt',
                        action='store',
                        type=str,
                        default="output.pdf",
                        help='pdf-output directory path')
    parser.add_argument('-axis', '--axis',
                        action='store',
                        type=int,
                        default=0,
                        help='0: たて, 1: よこ')
    parser.add_argument('-fillna', '--fillna',
                        action='store',
                        type=str,
                        default=None,
                        help='Value to fill nan')
    args = parser.parse_args()
    return vars(args)


def main(args):
    # preprocess - read configs
    path_in_matrixs = args["path_in_matrixs"]
    path_out_txt = args["path_out_txt"]
    axis = args["axis"]
    fillna = args["fillna"]

    opts = {"sep": "\t", "index_col": 0}
    df_in_matrixs = [pd.read_csv(path_in_matrix, **opts) for path_in_matrix in path_in_matrixs]

    # main - input
    out_df = pd.concat(df_in_matrixs, axis=axis)
    if fillna is not None:
        out_df.fillna(fillna, inplace=True)
    out_df.to_csv(path_out_txt, sep="\t")


if __name__ == '__main__':
    main(parser_setting())
