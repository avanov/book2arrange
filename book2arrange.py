#!/usr/bin/env python
import os
import argparse



def main():
    cli_parser = argparse.ArgumentParser(
        description='Arrange audio files from http://www.50languages.com/ '\
        			'in one convenient collection for better language acquisition.'
    )
    cli_parser.add_argument('source', help="collections' parent dir")
    cli_parser.add_argument('target', help="path to the arranged collection")
    cli_parser.add_argument(
        'order',
        help="two-letter list of language collections to be put into the target collection"
    )
    args = cli_parser.parse_args()

    for i in range(1, 100):
        pass



if __name__ == '__main__':
    main()
