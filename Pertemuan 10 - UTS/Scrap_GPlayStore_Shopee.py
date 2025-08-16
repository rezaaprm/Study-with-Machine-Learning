import pandas as pd
from tqdm import tqdm
from google_play_scraper import Sort, reviews, app

# Aplikasi Shopee
app_id = 'com.shopee.id'

# Scraping informasi aplikasi
print("Mengambil informasi aplikasi Shopee...")
info = app(app_id, lang='id', country='id')
del info['comments']  # Hapus komentar yang tidak diperlukan
app_info_df = pd.DataFrame([info])

# Scraping ulasan aplikasi Shopee
print("Mengambil ulasan aplikasi Shopee...")
app_reviews = []
for score in range(1, 6):  # Skor ulasan 1-5
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
        rvs, _ = reviews(
            app_id,
            lang='id',
            country='id',
            sort=sort_order,
            count=200 if score == 3 else 100,
            filter_score_with=score
        )
        for r in rvs:
            r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
            r['appId'] = app_id
        app_reviews.extend(rvs)

# Konversi ke DataFrame
app_reviews_df = pd.DataFrame(app_reviews)

# Simpan hasil ke file CSV
app_info_df.to_csv('shopee_info.csv', index=False)
app_reviews_df.to_csv('shopee_reviews.csv', index=False)

print("Scraping selesai. Data telah disimpan:")
print("- Informasi aplikasi: shopee_info.csv")
print("- Ulasan aplikasi: shopee_reviews.csv")
