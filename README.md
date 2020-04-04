# find_corpus
A corpus searcher powered by regular expression matching and can give contextual examples.

Just entering a few characters, all phrase usages in related, shown frequencies and context (optional) will be presented immediately.

## Features

![demo1](http://www.xyu.ink/wp-content/uploads/2020/04/feature2.png)

## Preparing your Corpus

Prepare your corpus files (in `.txt` format) and put **ALL of them** in **ONE** directory.

We also provide a demo corpus (CVPR 2018-2019) in case you don't have one [[Download](http://www.xyu.ink/wp-content/uploads/2019/12/CVPR_18-19.zip)].

## Getting Started

1. Set `root_dir` in `find_corpus.py` to your corpus directory.

2. Then run

   ```bash
   python find_corpus.py
   ```

3. Input the pattern, here are some examples:

   ```bash
   pattern:
   >>> as ? in fig           # ? matchs any one word
   >>> code * publicly       # * matchs [0-n] words
   >>> (show|demonstrate|achieve) ? results   # Multiple choice words
   >>> show[ns]? ? results   # RegEx matching
   >>> ### ? feature fusion  # use ### to show context
   ```

4.  Just a moment, results will be given.


