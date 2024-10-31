# Movie Recommendation System

Bu proje, içerik tabanlı filtreleme algoritması kullanarak kullanıcıya film önerileri sunan bir sistem geliştirmeyi amaçlamaktadır. Flask tabanlı bir backend ve React tabanlı bir frontend ile oluşturulacaktır.

## Proje Yapısı

- **Backend**: Flask ile API oluşturulacak. Film öneri algoritması burada çalışacak ve kullanıcıdan gelen talepler doğrultusunda öneri listesi döndürecek.
- **Frontend**: React ile kullanıcı arayüzü geliştirilecek. Kullanıcıya öneri butonu ve film önerilerini gösteren bir arayüz sunulacak.

## Gereksinimler

- **Python 3.8** veya üstü
- **Node.js** ve **npm**
- Python kütüphaneleri: **Flask**, **Pandas**, **scikit-learn**
- JavaScript kütüphaneleri: **React**, **Axios**

## Kurulum

### Backend (Flask API)

1. **Sanal Ortam Oluşturma**:
   ```bash
   cd backend
   python3 -m venv env
   source env/bin/activate  # Mac/Linux
   env\Scripts\activate  # Windows
