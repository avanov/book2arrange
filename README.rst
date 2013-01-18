book2arrange
============

Arrange audio files from http://www.50languages.com/ in one convenient collection for better language acquisition.

Installation
--------------

.. code-block:: bash

    $ pip install book2arrange


Usage
----------

.. code-block:: bash

    $ book2arrange $HOME/book2source $HOME/Desktop/polyglot enfr ende


The command will extract and arrange audio files from book2 archives. The target
files will have the following naming schema:

.. code-block:: none

    $HOME/Desktop/polyglot/00001_1_enfr.mp3
    $HOME/Desktop/polyglot/00002_1_ende.mp3
    $HOME/Desktop/polyglot/00003_2_enfr.mp3
    $HOME/Desktop/polyglot/00004_2_ende.mp3
    ...
    $HOME/Desktop/polyglot/00199_100_enfr.mp3
    $HOME/Desktop/polyglot/00200_100_ende.mp3


Note: all listed directories must exist.


.. code-block:: guess

    $ book2arrange -h
    usage: book2arrange [-h] source target order [order ...]

    Arrange audio files from http://www.50languages.com/ in one convenient
    collection for better language acquisition.

    positional arguments:
      source      collections' parent dir
      target      path to the arranged collection
      order       four-letter list of language collections to be put into the
                  target collection

    optional arguments:
      -h, --help  show this help message and exit
