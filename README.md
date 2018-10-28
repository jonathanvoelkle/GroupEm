# GroupEm

🙋 Grouping people so everyone is happy.

If you've ever had to group people together (esp. kids) and everyone wanted something different, you know it's a pain. This small programm tries to remove the hassle doing that.

<!-- TODO -->

## Installation and Usage

This project is build in python 3.6, so make sure you have python 3 installed (at least nobody has tried running this in python 2.x)

Then just clone this repo and run the programm

```shell
git clone https://github.com/jonathanvoelkle/GroupEm.git
cd groupem
python3 groupem
```

You might have to change the input file (optional, see the following).

If you want to output the assigned groups to a file, you can also run.

```shell
python3 groupem > f.txt
```

to save them to a file called `f.txt`.

The programm tries to locate a file `data/data.csv` (with has to have the said structure).

A sample dataset is provided under [`sample/data.csv`](/sample/data.csv).

Note that a set of data with a large number people or large group-variability can take a (very, very) long time to process, you might have to modify this algorithm.

The code assumes you use a integer based rating system (e.g. stars, higher value means higher preferences) (and transforms them into a cost function to be used in `linear_sum_assignment()`).

## FAQ

<dl>
  <dt>I found a bug/have a idea for improvement/etc</dt>
  <dd>Feel free to submit a PR</dd>

  <dt>How does the file have to look like?</dt>
  <dd><ul>
    <li>The first row can include the names of the different groups</li>
    <li>The second row has to be the minimum size of each group</li>
    <li>The thrid row has to be the maximum size of each group</li>
    <li>The fourth row has to be the optimal size of each group (not implemented yet)</li>
    <li>The first column can include something like an index</li>
    <li>The second column can include e.g. the name of each person</li>
    <li>Everything else has to be the rating of each person (of the current row) regarding the group (in the current column)</li>
  </ul></dd>
</dl>

## Copyright and License

GroupEm is open source software [licensed as MIT](LICENSE)
