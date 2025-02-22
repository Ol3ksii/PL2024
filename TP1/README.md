# TPC1

**Author**: [**102131** Oleksii Tantsura](https://www.github.com/Ol3ksii)

**Date**: 21/02/2025

## Summary
This Python program reads text from standard input and sums every digit sequence it finds, under these rules:
1. The string "Off" (in any case combination) disables summation.
2. The string "On" (in any case combination) enables summation.
3. Each "=" sign outputs the current total and continues the process.

At the end of the text, the final total is also printed.

## Example Input 1 (input.txt)
```txt
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens 
deu-nos
este trabalho para fazer.=OfF
E deu-nos 7= dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!
```

## Example Output 1
```txt
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens 
deu-nos
este trabalho para fazer.=
>> 2032
OfF
E deu-nos 7=
>> 2032
 dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!
>> 2057
```

## Example Input 2
```txt
123=On
Now 456 is added,
OFF
Ignore 789
Reset? on
Add 1 2 3 again...= 
Finish
```

## Example Output 2
```txt
123=
>> 123
On
Now 456 is added,
OFF
Ignore 789
Reset? on
Add 1 2 3 again...=
>> 585
 
Finish

>> 585
```

## Usage
The code is contained in the file **TPC1.py** and must be run with Python 3, taking its input from stdin:
```bash
$ python3 TPC1.py < input.txt
