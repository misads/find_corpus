# find_corpus
A corpus searcher with RegEx matching and contextual examples.

Phrase usage, occurence (times) and context (if needed) of every matching results will be presented explicitly.

## Demonstration

![demo1](http://www.xyu.ink/wp-content/uploads/2019/12/demo2.png)

## Prepare your Corpus

Put your corpus files (all in txt format) in a directory.

We also prepare a demo corpus (CVPR 2018-2019) in case you don't have one [[download](http://www.xyu.ink/wp-content/uploads/2019/12/CVPR_18-19.zip)].

## Code Usage

1. Set `root_dir` to your corpus directory.

2. Run

   ```bash
   python find_corpus.py
   ```

3. Input the pattern

   ```bash
   pattern:
   >>> as ? in fig           # ? matchs any one word
   >>> code * publicly       # * matchs [0-n] words
   >>> (show|demonstrate|achieve) ? results   # Multiple choice words
   >>> show[ns]? ? results   # RegEx matching
   >>> ### ? feature fusion  # use ### to show context
   ```

4.  Results will be given like that of *Demonstration* part.


