import os
import shutil
import argparse
import tempfile
import zipfile



def main():
    cli_parser = argparse.ArgumentParser(
        description='Arrange audio files from http://www.50languages.com/ '\
        			'in one convenient collection for better language acquisition.'
    )
    cli_parser.add_argument('source', help="collections' parent dir")
    cli_parser.add_argument('target', help="path to the arranged collection")
    cli_parser.add_argument(
        'order', nargs='+',
        help="four-letter list of language collections to be put into the target collection"
    )
    args = cli_parser.parse_args()

    language_pairs = [pair.upper() for pair in args.order]

    tmpdir = tempfile.mkdtemp()
    try:
        # Extract
        for lang_pair in language_pairs:
            lang_archive = os.path.join(args.source, "{}-all.zip".format(lang_pair))
            with zipfile.ZipFile(lang_archive, 'r') as lang_zip:
                lang_zip.extractall(tmpdir)
        # Arrange
        ordinal = 1
        for idx in range(1, 101):
            for lang_pair in language_pairs:
                source_file = os.path.join(tmpdir, "{}{:03d}.mp3".format(lang_pair, idx))
                target_file = os.path.join(
                    args.target,
                    "{:05d}_{}_{}.mp3".format(ordinal, idx, lang_pair.lower())
                )
                shutil.move(source_file, target_file)
                ordinal +=1
    finally:
        # cleanup
        shutil.rmtree(tmpdir)
