# Komachi 2022

## How to run

```
python solve.py
```

## Get unique result

```
cat result.txt | awk -F'] ' '{print $2}' | sort | uniq
```