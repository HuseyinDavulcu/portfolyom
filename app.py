import streamlit as st
from PIL import Image

# Sayfa Ayarları
st.set_page_config(page_title="Benim Portfolyom", page_icon="🚀", layout="wide")

# Sol Taraftaki Yan Menü
with st.sidebar:
    st.header("İletişim")
    st.write("📍 Lokasyon: Türkiye")
    st.write("📧 E-posta: h_1936@hotmail.com")
    st.write("🔗 [LinkedIn Profilim](https://tr.linkedin.com/in/h%C3%BCseyin-d-999a831b1?trk=people-guest_people_search-card)")
    
    st.divider()
    st.write("Bu site Python ve Streamlit ile yapılmıştır.")

# Ana Başlık Bölümü
st.title("Merhaba, Ben Hüseyin! 👋")
st.subheader("Python Geliştiricisi & Üretim Tutkunu")
st.write("""
Burada geliştirdiğim projeleri, yazdığım otomasyon kodlarını ve 
teknik yeteneklerimi sergiliyorum.
""")

st.divider()

# Projeler Bölümü
st.header("📂 Projelerim")

# Sütunlara bölelim (Görsel ve Yazı yan yana olsun)
col1, col2 = st.columns([1, 2])

with col1:
    # Buraya bir resim ekleyebilirsiniz, şimdilik yazı koyalım
    st.info("PROJE 1") 

with col2:
    st.subheader("Excel VBA Palet Optimizasyonu")
    st.write("""
    **Kullanılanlar:** Excel, VBA, Matematiksel Modelleme
    
    Ürünlerin paletlere en verimli şekilde dizilmesini sağlayan bir algoritma geliştirdim.
    Bu proje sayesinde paketleme hacminde %20 tasarruf sağlandı.
    """)

st.divider()

col3, col4 = st.columns([1, 2])

with col3:
    st.info("PROJE 2")

with col4:
    st.subheader("Python Veri Analizi")
    st.write("""
    **Kullanılanlar:** Python, Pandas, Matplotlib
    
    Satış verilerini analiz ederek otomatik raporlayan bir bot yazdım.
    """)

# Kapanış
st.divider()
st.caption("© 2024 - Tüm hakları saklıdır.")
