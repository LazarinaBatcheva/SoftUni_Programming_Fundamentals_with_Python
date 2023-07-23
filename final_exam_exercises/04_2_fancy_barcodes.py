import re


barcodes_count = int(input())
barcodes = [input() for _ in range(barcodes_count)]
pattern = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"
for barcode in barcodes:
    if re.fullmatch(pattern, barcode):
        product_group = re.findall(r"\d", barcode)
        product_group = "". join(product_group) if product_group else "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")