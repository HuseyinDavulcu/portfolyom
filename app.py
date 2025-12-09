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
Uluslararası Ticaret ve Finans alanındaki sağlam temelimle, otomotiv ve tekstil sektörlerini kapsayan çeşitli bir profesyonel geçmişe sahibim.
Operasyonel verimlilik, satış becerisi ve teknik inovasyonu benzersiz bir şekilde bir araya getiriyorum.İkiler Otomotiv Filtre İthalat İhracat San. ve Tic. A.Ş.'de en son İhracat Operasyonları Uzmanı olarak lojistiği optimize etmeye ve operasyonel maliyetleri azaltmaya odaklandım.
Otomotiv sektöründen önce, tekstil ve promosyon ürünleri endüstrisinde uluslararası satış ve yaratıcı becerilerimi geliştirdiğim kapsamlı bir deneyim kazandım.
Adobe Illustrator, Photoshop ve SketchUp kullanarak fuar standları tasarlama geçmişine sahibim.
İngilizce'yi akıcı (C1) konuşuyorum ve temel düzeyde Almanca ve İspanyolca bilgisine sahibim. Satışın operasyonel zeka ile buluştuğu bu çok disiplinli zihniyeti organizasyonunuza taşımaya hazırım.   
""")

st.divider()

# Projeler Bölümü
st.header("📂 Projelerim")

# Sütunlara bölelim (Görsel ve Yazı yan yana olsun)
col1, col2 = st.columns([1, 2])

with col1:
    # Buraya bir resim ekleyebilirsiniz, şimdilik yazı koyalım
    st.info("PROJE 1") 
    # Dosya uzantısı .jpg ise .jpg, .png ise .png yazmayı unutmayın
st.image("vba_proje.png.PNG", caption="Excel VBA ile Otomatik Palet Yerleşimi")
st.image("vba_proje1.png.PNG", caption="Excel VBA ile Otomatik Palet Yerleşimi")
st.image("vba_proje3.png.PNG", caption="Excel VBA ile Otomatik Palet Yerleşimi")

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
 # Dosya uzantısı .jpg ise .jpg, .png ise .png yazmayı unutmayın
st.image("ciro_hesaplama.PNG", caption="Excel VBA ile Otomatik Palet Yerleşimi")
st.image("3d_rapor.PNG", caption="Excel VBA ile Otomatik Palet Yerleşimi")
with col4:
    st.subheader("Python Veri Analizi")
    st.write("""
    **Kullanılanlar:** Python, Pandas, Matplotlib
    
    Satış verilerini analiz ederek otomatik raporlayan bir bot yazdım.
    """)

# Kapanış
st.divider()
st.caption("© 2024 - Tüm hakları saklıdır.")
