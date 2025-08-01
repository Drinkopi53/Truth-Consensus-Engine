import re
import os
import sys
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

# Tambahkan src ke path untuk mengimpor data_aggregator untuk pengujian
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import data_aggregator

# Pastikan stopwords bahasa Indonesia tersedia
try:
    stop_words = set(stopwords.words('indonesian'))
except OSError:
    print("Kumpulan stopwords 'indonesian' tidak ditemukan. Menggunakan daftar fallback dasar.")
    stop_words = {'yang', 'di', 'dan', 'ke', 'dari', 'ini', 'itu', 'dengan', 'untuk', 'pada', 'adalah', 'atau', 'tapi', 'juga'}

def preprocess_text(text):
    """Membersihkan dan melakukan tokenisasi teks menjadi kalimat (klaim)."""
    text = re.sub(r'^\s*Topik:.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*Sumber:.*$', '', text, flags=re.MULTILINE)
    text = text.strip()
    sentences = sent_tokenize(text)
    return [s.strip() for s in sentences if s.strip()]

def normalize_claim(claim):
    """Menormalkan satu klaim untuk perbandingan."""
    claim = claim.lower()
    claim = re.sub(r'[^\w\s]', '', claim)
    words = [word for word in claim.split() if word not in stop_words and len(word) > 2]
    return set(words)

def jaccard_similarity(set1, set2):
    """Menghitung kesamaan Jaccard antara dua himpunan."""
    if not set1 and not set2:
        return 1.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union > 0 else 0.0

def analyze_sources(sources_data, similarity_threshold=0.3, consensus_threshold_ratio=0.6):
    """Menganalisis sumber yang dikumpulkan untuk menemukan konsensus dan klaim yang bertentangan."""
    all_claims = []
    for source in sources_data:
        source_name = source['source_name']
        sentences = preprocess_text(source['content'])
        for sentence in sentences:
            normalized = normalize_claim(sentence)
            if normalized:
                all_claims.append({
                    'original_claim': sentence,
                    'normalized_claim': normalized,
                    'source': source_name
                })

    claim_clusters = []
    processed_indices = set()
    for i in range(len(all_claims)):
        if i in processed_indices:
            continue

        current_cluster_claims = [all_claims[i]]
        processed_indices.add(i)

        for j in range(i + 1, len(all_claims)):
            if j in processed_indices:
                continue

            similarity = jaccard_similarity(
                all_claims[i]['normalized_claim'],
                all_claims[j]['normalized_claim']
            )
            if similarity >= similarity_threshold:
                if all_claims[j]['source'] not in {c['source'] for c in current_cluster_claims}:
                    current_cluster_claims.append(all_claims[j])
                    processed_indices.add(j)

        if current_cluster_claims:
            representative_claim = max(current_cluster_claims, key=lambda x: len(x['original_claim']))
            sources = {c['source'] for c in current_cluster_claims}
            claim_clusters.append({
                'representative_claim': representative_claim['original_claim'],
                'sources': sources
            })

    consensus_claims = []
    conflicting_claims = []
    num_sources = len(sources_data)
    consensus_threshold_count = int(consensus_threshold_ratio * num_sources)
    if consensus_threshold_count < 2: consensus_threshold_count = 2

    for cluster in claim_clusters:
        item = {
            'claim': cluster['representative_claim'],
            'sources': sorted(list(cluster['sources'])),
            'source_count': len(cluster['sources'])
        }
        if len(cluster['sources']) >= consensus_threshold_count:
            consensus_claims.append(item)
        else:
            conflicting_claims.append(item)

    return consensus_claims, conflicting_claims

if __name__ == '__main__':
    print("Menjalankan mesin analisis sebagai skrip mandiri...")
    mock_data = data_aggregator.aggregate_sources()
    if mock_data:
        print(f"Menganalisis {len(mock_data)} sumber data...")
        consensus, conflicting = analyze_sources(mock_data)

        print("\n--- FAKTA KONSENSUS ---")
        if consensus:
            consensus.sort(key=lambda x: x['source_count'], reverse=True)
            for item in consensus:
                print(f"({item['source_count']} sumber): {item['claim']}")
        else:
            print("Tidak ada fakta konsensus yang ditemukan.")

        print("\n--- KLAIM BERTENTANGAN / BELUM DIVERIFIKASI ---")
        if conflicting:
            conflicting.sort(key=lambda x: x['source_count'], reverse=True)
            for item in conflicting:
                print(f"({item['source_count']} sumber): {item['claim']}")
        else:
            print("Tidak ada klaim yang bertentangan ditemukan.")
    else:
        print("Tidak ada data yang ditemukan untuk dianalisis.")
