import diffios
baseline = "R1.txt"
comparing = "R2.txt"
ignore = "ignore.txt"
diff = diffios.Compare(baseline=baseline,comparison=comparing,ignore_lines=ignore)
print(diff.delta())