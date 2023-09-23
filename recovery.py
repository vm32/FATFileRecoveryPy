import os
import struct

image_path = "path_to_your_fat_image.img"

# Open the FAT image in binary read mode
with open(image_path, "rb") as image:

    boot_sector = image.read(512)
    bytes_per_sector = struct.unpack("<H", boot_sector[11:13])[0]
    sectors_per_cluster = boot_sector[13]
    reserved_sectors = struct.unpack("<H", boot_sector[14:16])[0]
    number_of_fats = boot_sector[16]
    root_entries = struct.unpack("<H", boot_sector[17:19])[0]
    total_sectors = struct.unpack("<H", boot_sector[19:21])[0]
    sectors_per_fat = struct.unpack("<H", boot_sector[22:24])[0]
    root_dir_start = (reserved_sectors + number_of_fats * sectors_per_fat) * bytes_per_sector
    data_region_start = root_dir_start + (root_entries * 32)

    image.seek(root_dir_start)

    for i in range(root_entries):
        entry = image.read(32)
        if entry[0] == 0xE5:  # Check if the file is marked as deleted
            file_name = entry[:8].decode('ascii').strip()
            file_ext = entry[8:11].decode('ascii').strip()
            file_size = struct.unpack("<I", entry[28:32])[0]

            starting_cluster = struct.unpack("<H", entry[26:28])[0]
            file_data_address = data_region_start + (starting_cluster - 2) * sectors_per_cluster * bytes_per_sector
            image.seek(file_data_address)
            file_data = image.read(file_size)
            with open(f"recovered_{file_name}.{file_ext}", "wb") as recovered_file:
                recovered_file.write(file_data)
            print(f"Recovered {file_name}.{file_ext}")
