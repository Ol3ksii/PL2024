# TPC4

**Author**: [**A102131** Oleksii Tantsura](https://www.github.com/Ol3ksii)

**Date**: 2025-03-09

## Summary

In this task (TPC4), the goal is to develop a lexical analyzer in Python that processes query language statements.

The program must:

- **Tokenize the input** to identify keywords, variables, literals, and punctuation.
- **Recognize key components** such as:
  - **Keywords**: `SELECT`, `WHERE`, `LIMIT`, `PREFIX`, `A`
  - **Identifiers**: Prefix names, terms, and variables
  - **Literals**: Strings, numbers, and IRIs
  - **Special symbols**: `{`, `}`, `:`, `.`
- **Ignore comments** (`# ...`) and handle language tags (`@en`).

## Results

The program is executed from the command line and expects a query input via standard input. Example usage:

```bash
python3 TPC4.py < example.txt
```

## example.txt:
```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

After execution, the user is presented with the lexical analysis output:

```bash
LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',1,0)
LexToken(SELECT,'select',2,32)
LexToken(VAR,'?nome',2,39)
LexToken(VAR,'?desc',2,45)
LexToken(WHERE,'where',2,51)
LexToken(LBRACE,'{',2,57)
LexToken(VAR,'?s',3,59)
LexToken(A,'a',3,62)
LexToken(PREFIXNAME,'dbo',3,64)
LexToken(COLON,':',3,67)
LexToken(TERM,'MusicalArtist',3,68)
LexToken(DOT,'.',3,81)
LexToken(VAR,'?s',4,83)
LexToken(PREFIXNAME,'foaf',4,86)
LexToken(COLON,':',4,90)
LexToken(TERM,'name',4,91)
LexToken(STRING,'"Chuck Berry"',4,96)
LexToken(LANGTAG,'@en',4,109)
LexToken(DOT,'.',4,113)
LexToken(VAR,'?w',5,115)
LexToken(PREFIXNAME,'dbo',5,118)
LexToken(COLON,':',5,121)
LexToken(TERM,'artist',5,122)
LexToken(VAR,'?s',5,129)
LexToken(DOT,'.',5,131)
LexToken(VAR,'?w',6,133)
LexToken(PREFIXNAME,'foaf',6,136)
LexToken(COLON,':',6,140)
LexToken(TERM,'name',6,141)
LexToken(VAR,'?nome',6,146)
LexToken(DOT,'.',6,151)
LexToken(VAR,'?w',7,153)
LexToken(PREFIXNAME,'dbo',7,156)
LexToken(COLON,':',7,159)
LexToken(TERM,'abstract',7,160)
LexToken(VAR,'?desc',7,169)
LexToken(RBRACE,'}',8,175)
LexToken(LIMIT,'LIMIT',8,177)
LexToken(NUMBER,1000,8,183)
```

- **1** (Keyword recognition):
    ```
    SELECT, WHERE, LIMIT, PREFIX, A
    ```
    Detected and tokenized as keywords.

- **2** (Variable recognition):
    ```
    ?nome, ?desc, ?s, ?w
    ```
    Identified as variables.

- **3** (Prefix and Term recognition):
    ```
    dbo:MusicalArtist, foaf:name, dbo:artist
    ```
    Identified correctly.

- **4** (String and Language Tag handling):
    ```
    "Chuck Berry"@en
    ```
    Recognized as a STRING token with a LANGTAG.

- **5** (Punctuation handling):
    ```
    { }, :, .
    ```
    Identified and tokenized correctly.

## Conclusion

The lexical analyzer successfully processes query statements, identifying keywords, variables, literals, and special symbols while handling language tags and comments.
