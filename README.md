# LibIndic ucasort
[![Build Status](https://travis-ci.org/libindic/ucasort.svg?branch=master)](https://travis-ci.org/libindic/ucasort)
[![Coverage Status](https://coveralls.io/repos/github/libindic/ucasort/badge.svg?branch=master)](https://coveralls.io/github/libindic/ucasort?branch=master)

LibIndic's ucasort module lets you sort words based on their linguistics.

## Installation
1. Clone the repository `git clone https://github.com/libindic/ucasort.git`
2. Change to the cloned directory `cd ucasort`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-ucasort*.tar.gz`

## Usage
```
>>> from libindic.ucasort import Sort
>>> instance = Sort()
>>> result = instance.sort(u"കർത്തവ്യം അംബരീക്ഷൻ കൃത്യനിഷ്ഠ ശാപം ക്ഷമ സോമൻ ഷീല")
>>> for word in result['UCA']:
...     print(word)
...
അംബരീക്ഷൻ
കർത്തവ്യം
കൃത്യനിഷ്ഠ
ക്ഷമ
ശാപം
ഷീല
സോമൻ
```
## Tests
Run tests with ``python setup.py test``
