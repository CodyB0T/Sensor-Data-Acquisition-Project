import lzo


def decompress_lzo(input_file, output_file):
    with open(input_file, "rb") as f_in:
        compressed_data = f_in.read()
        decompressed_data = lzo.decompress(compressed_data)
        with open(output_file, "wb") as f_out:
            f_out.write(decompressed_data)


help(lzo)


input_file = "test_rf.raw.lzo"
output_file = "decompressed_test.raw"

decompress_lzo(input_file, output_file)
print("Decompression completed.")
