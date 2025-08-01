import os

def aggregate_sources(data_directory="data/"):
    """
    Mengumpulkan data dari semua file sumber di direktori yang ditentukan.

    Args:
        data_directory (str): Path ke direktori yang berisi file sumber.

    Returns:
        list[dict]: Daftar kamus, di mana setiap kamus berisi
                    nama sumber (nama file) dan kontennya.
    """
    sources = []
    if not os.path.isdir(data_directory):
        print(f"Error: Direktori '{data_directory}' tidak ditemukan.")
        return sources

    # Memastikan urutan file konsisten
    for filename in sorted(os.listdir(data_directory)):
        if filename.endswith(".txt"):
            filepath = os.path.join(data_directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    sources.append({"source_name": filename, "content": content})
            except Exception as e:
                print(f"Gagal membaca file {filepath}: {e}")

    return sources

# Contoh penggunaan untuk pengujian mandiri
if __name__ == '__main__':
    all_data = aggregate_sources()
    if all_data:
        print(f"Berhasil mengumpulkan {len(all_data)} sumber.")
        print("\n--- Contoh dari sumber pertama ---")
        print(all_data[0])
        print("---------------------------------")
    else:
        print("Tidak ada data yang dikumpulkan.")
