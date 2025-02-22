# TPC2

**Author**: [**A102131** Oleksii Tantsura](https://www.github.com/Ol3ksii)

**Date**: 2025-02-22

## Summary
In this task for the 2nd week, the goal is to develop a Python program that analyzes a dataset of musical works while following specific constraints:

- The use of Python's CSV module is prohibited.
- The program must read the dataset, process it, and generate the following results:
    1. A sorted alphabetical list of musical composers.
    2. A distribution of works by period, displaying the number of cataloged works per period.
    3. A dictionary where each period is associated with an alphabetical list of work titles from that period.

## Results

The program is executed from the command line and requires the path to the CSV file as input. Example:

```bash
python3 TPC2.py < obras.csv
```

After execution, the user is presented with the output in the following order:

```bash
1) Sorted composers:
2) Distribution of works by period:
3) Period -> sorted list of titles:
```

- **1** (Sorted composers):
    ```
    1) Sorted composers:
    Alessandro Stradella
    Antonio Maria Abbatini
    Bach, Johann Christoph
    Bach, Johann Michael
    Bach, Wilhelm Friedemann
    Balbastre, Claude
    Baldassare Galuppi
    Barbara of Portugal
    Benda, Franz
    ...
    ```

- **2** (Distribution of works by period):
    ```
    2) Distribution of works by period:
    Barroco: 26 works
    Clássico: 15 works
    Medieval: 45 works
    Renascimento: 40 works
    Século XX: 18 works
    Romântico: 19 works
    Contemporâneo: 6 works
    ```


- **3** (Period -> sorted list of titles):

    ```
    3) Period -> sorted list of titles:

   Barroco:
        Ab Irato
        Die Ideale, S.106
        Fantasy No. 2
        Hungarian Rhapsody No. 16
        Hungarian Rhapsody No. 5
        Hungarian Rhapsody No. 8
        Impromptu Op.51
        In the Steppes of Central Asia
        Mazurkas, Op. 50
        Military Band No. 1
        Nocturne in C minor
        Paganini Variations, Book I
        Polonaise Op. 44
        Polonaise-Fantasie
        Polonaises Op.71
        Preludes Op. 11
        Preludes Op. 49 a
        Prince Rostislav
        Rage Over a Lost Penny
        Rondo Op. 5
        Shéhérazade, ouverture de féerie
        Symphonies de Beethoven
        The Rondo
        Transcendental Études
        Études Op. 25
        Études Op.10

   Clássico:
    ...
    ```

## Conclusion
The program successfully processes the dataset without utilizing Python's CSV module and generates the expected results in an organized format.
