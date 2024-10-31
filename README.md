# movie-recommendation-system
Bu proje, içerik tabanlı filtreleme algoritması kullanarak kullanıcıya film önerileri sunan bir sistem geliştirmeyi amaçlamaktadır. Flask tabanlı bir backend ve React tabanlı bir frontend ile oluşturulacaktır.
# Proje Yapısı
Backend: Flask ile API oluşturulacak. Film öneri algoritması burada çalışacak ve kullanıcıdan gelen talepler doğrultusunda öneri listesi döndürecek.
Frontend: React ile kullanıcı arayüzü geliştirilecek. Kullanıcıya öneri butonu ve film önerilerini gösteren bir arayüz sunulacak.
Gereksinimler
Python 3.8 veya üstü
Node.js ve npm
Flask, Pandas, scikit-learn gibi Python kütüphaneleri
React ve Axios gibi JavaScript kütüphaneleri
# Kurulum
Backend (Flask API)

Sanal Ortam Oluşturma:
cd backend
python3 -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
Gerekli Kütüphanelerin Yüklenmesi:
pip install flask pandas scikit-learn

Uygulamayı Çalıştırma:
python app.py
Frontend (React)

React Projesi Oluşturma:
bash
Copy code
cd frontend
npx create-react-app movie-recommendation-frontend
Axios Kurulumu:
bash
Copy code
npm install axios

# Kullanılan Kütüphaneler
Flask: API oluşturmak için.
 Pandas: Veri işleme ve analizi için.
scikit-learn: Makine öğrenimi ve benzerlik hesaplama için.
React: Kullanıcı arayüzü geliştirmek için.
Axios: API ile frontend arasındaki bağlantıyı sağlamak için.
Görev Dağılımı
Backend Geliştirme: API, veri işleme ve içerik tabanlı öneri algoritmasının geliştirilmesi.
Frontend Geliştirme: Kullanıcı arayüzü tasarımı ve API ile entegrasyon.
Dokümantasyon: Proje dökümantasyonunun ve kullanıcı rehberinin hazırlanması.
