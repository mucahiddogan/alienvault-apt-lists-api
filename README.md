# Alienvault apt lists api

otx.alienvault.com üzerinde yer alan APT gruplarını ve bunların paylaştığı IOC'leri gösteren Flask Fastapi uygulaması.
Web sitesine [apt-list.herokuapp.com](https://apt-list.herokuapp.com/) üzerinden erişebilirsiniz. 

## Kullanım

Uygulama heroku üzerinde deploy edilmiştir. Kullanabilmek için [otx.alienvault.com](otx.alienvault.com) üzerinden kendi API keyinizi üretmeniz gerekmektedir. Uygulama 2 parçadan oluşmaktadır.

1. app/test_scripts/search.py bu kod parçacığı, ünlü apt gruplarının paylaştığı IOC depolarını listeleyip otomatik olarak sizin alienvault hesabınızdan takip eder.

2. app/main.py bu uygulama sayesinde takip ettiğiniz apt gruplarının listelerine özelleştirilmiş şekilde erişebilirsiniz. Uygulamayı çalıştırmak için flask ve benzeri gereksinimleri cihazınıza kurmuş olmanız gerekmektedir. Ubuntu için:

Aldığınız API anahtarlarını search.py ve main.py dosyaları içerisinde aşağıdaki satıra eklemeniz gerekmektedir.

```python
headers = {"X-OTX-API-KEY":"<APIKEYY>"}  # WRITE YOUR API KEY TO HERE 
```
Kullanım:

```bash
cd app/
pip3 install -r requirements.txt
python3 main.py
```
127.0.0.1:5000 portuna web tarayıcınız üzerinden erişip ana dizine,

127.0.0.1:5000/docs üzerinde API servisinize erişmiş olursunuz

### :octocat: [github.com/mucahiddogan](https://github.com/mucahiddogan)

## License
[MIT](https://choosealicense.com/licenses/mit/)
