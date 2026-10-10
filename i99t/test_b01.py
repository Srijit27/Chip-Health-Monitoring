from dataset_builder import build_dataset

bench_file = r"D:\Srijit\Development\Chip-Health-Monitoring\i99t\b01\b01_C.bench" #dataset path in Srijit's machine

df = build_dataset(bench_file)

print("\n===== b01 DATASET =====")
print(df.to_string(index=False))

print("\n===== DEPTH SUMMARY =====")
print(df["depth"].describe())

print("\n===== MAX DEPTH =====")
print(df["depth"].max())