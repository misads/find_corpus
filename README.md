# find_corpus
An intelligent corpus searcher, you can search any expressions you needed with regular expression.

Just entering the pattern, all matching expressions, shown frequencies and context will be listed.

## Features

![demo1](http://www.xyu.ink/wp-content/uploads/2020/04/feature2.png)

## Preparing your Corpus

Prepare your corpus materials (articles, wikis... all in `txt` format) and put them in the same directory, namely `root_dir` in the program.

We also provide a demo corpus (CVPR 2018-2019) in case you don't know how to make your own one [[Download](http://www.xyu.ink/wp-content/uploads/2019/12/CVPR_18-19.zip)].

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

4.  Waiting for the results.


