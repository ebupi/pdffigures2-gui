# Ubuntu Snap Store - Yayınlama ve Paketleme Kılavuzu

Bu kılavuz, geliştirdiğimiz modern **PDFFigures 2.0 PySide6 Yaru-Dark GUI** uygulamasını Canonical'ın **Snap** paketleme formatına dönüştürerek **Ubuntu Software Center (Uygulamalar)** mağazasında tüm dünyaya yayınlamanız için adım adım teknik yol haritasını içermektedir.

---

## 🌟 Snap Paketlemesinin Avantajları
1. **Tek Tıkla Kurulum:** Kullanıcılar Ubuntu Software arayüzünden uygulamanızı aratıp tek tıkla kurabilir.
2. **Tam Bağımlılık İzolasyonu:** Çalışması için gereken Python sürümü, PySide6 kütüphaneleri, Java 11 JRE (Sanal Makinesi) ve derlenmiş `pdffigures2.jar` dosyası tek bir `.snap` paketi içine gömülür. Kullanıcının sistemine hiçbir ek kütüphane kurması gerekmez.
3. **Otomatik Güncellemeler:** Uygulamada bir güncelleme yapıp mağazaya yüklediğinizde, kullanıcıların bilgisayarlarındaki uygulamalar arka planda otomatik olarak güncellenir.

---

## 🛠️ Adım 1: snapcraft.yaml Dosyasının Oluşturulması

Snapcraft aracının uygulamayı nasıl paketleyeceğini anlaması için projenin kök dizininde (`/home/ebupi/pdffigures2/`) **`snapcraft.yaml`** adında bir yapılandırma dosyası bulunmalıdır.

Sizin için Python + PySide6 (GUI) ve Java JRE (Çekirdek Motor) bağımlılıklarını mükemmel şekilde birleştiren **hazır ve eksiksiz** bir `snapcraft.yaml` şablonu hazırladım.

### `snapcraft.yaml` İçeriği:
```yaml
name: pdffigures2-gui
base: core22 # Ubuntu 22.04 LTS tabanını kullanır
version: '1.0'
summary: Modern Ubuntu GUI for the high-performance PDFFigures 2.0 extractor
description: |
  PDFFigures 2.0 is a Scala-based project built to extract figures, captions, 
  tables, and section titles from scholarly documents (scholarly PDFs). 
  This package adds a gorgeous, modern Yaru-Dark styled PySide6 (Qt6) desktop 
  user interface with native GNOME portal file choosers and an interactive gallery.

grade: stable # stable | devel
confinement: strict # strict (sandboxed) | devmode

# Sistemin donanım ivmelendirmesini ve yerel arayüz portallarını kullanabilmesi için izinler
plugs:
  desktop:
  desktop-legacy:
  wayland:
  x11:
  opengl:
  home: # Kullanıcının kendi ev dizinindeki PDF'leri okuyabilmesi için
  network: # Güncellemeler veya web entegrasyonu için

apps:
  pdffigures2-gui:
    command: bin/python $SNAP/gui.py
    desktop: local/share/applications/PDFFigures2.desktop
    plugs:
      - desktop
      - desktop-legacy
      - wayland
      - x11
      - opengl
      - home
      - network
    environment:
      # GUI'nin sistem temasına ve X11/Wayland sunucusuna bağlanabilmesi için ortam değişkenleri
      PATH: $SNAP/usr/bin:$SNAP/bin:$PATH
      LD_LIBRARY_PATH: $SNAP/usr/lib/$CRAFT_ARCH_TRIPLET:$LD_LIBRARY_PATH
      PYTHONPATH: $SNAP/lib/python3.10/site-packages:$PYTHONPATH
      JAVA_HOME: $SNAP/usr/lib/jvm/java-11-openjdk-amd64
      PATH: $SNAP/usr/lib/jvm/java-11-openjdk-amd64/bin:$PATH

parts:
  # 1. Parça: Java Çalışma Ortamı (JRE)
  jre:
    plugin: nil
    stage-packages:
      - openjdk-11-jre-headless
    prime:
      - usr/lib/jvm/java-11-openjdk-amd64

  # 2. Parça: Python ve GUI Bağımlılıkları
  python-env:
    plugin: python
    source: .
    python-requirements:
      - requirements.txt
    stage-packages:
      - libegl1
      - libgl1-mesa-glx
      - libxkbcommon0
      - libfontconfig1
      - libdbus-1-3
    prime:
      - lib/python3.10/site-packages

  # 3. Parça: PDFFigures 2.0 Kodları ve JAR Motoru
  app-code:
    plugin: dump
    source: .
    organize:
      gui.py: gui.py
      pdffigures2.jar: pdffigures2.jar
    prime:
      - gui.py
      - pdffigures2.jar
```

*Not: Snap paketinin Python bağımlılıklarını çekebilmesi için proje klasöründe bir de **`requirements.txt`** bulunmalıdır. İçeriği şu iki satırdan ibarettir:*
```text
PySide6==6.11.1
pillow==12.2.0
```

---

## 📦 Adım 2: Snap Paketinin Derlenmesi (Build)

Uygulamanızı paketlemek için sisteminize Snapcraft yükleyip derleme işlemini başlatmalısınız.

Terminalde şu komutları çalıştırın:
```bash
# 1. Snapcraft paketleme aracını sisteminize kurun
sudo snap install snapcraft --classic

# 2. Proje klasörüne geçiş yapın
cd /home/ebupi/pdffigures2/

# 3. Derleme işlemini başlatın (Bu işlem tüm bağımlılıkları indirip izole bir .snap dosyası oluşturur)
snapcraft
```
*İşlem bittiğinde dizinde **`pdffigures2-gui_1.0_amd64.snap`** adında bir paket oluşacaktır.*

---

## 🧪 Adım 3: Yerel Olarak Test Etmek (Local Install)

Paketi mağazaya göndermeden önce kendi bilgisayarınızda kurup çalışıp çalışmadığını test edebilirsiniz:
```bash
# Kendi bilgisayarınıza yerel olarak yükleyin (--dangerous kendi imzaladığınız paket olduğu içindir)
sudo snap install pdffigures2-gui_1.0_amd64.snap --dangerous

# Uygulamayı terminalden test etmek için:
snap run pdffigures2-gui
```

---

## 🚀 Adım 4: Ubuntu Software Center Mağazasında Yayınlamak

Her şeyin mükemmel çalıştığından emin olduktan sonra uygulamanızı resmi mağazaya gönderebilirsiniz:

1. **Hesap Oluşturun:** [Canonical Developer Portal](https://dashboard.snapcraft.io/) sitesine gidin ve ücretsiz bir Ubuntu geliştirici hesabı açın.
2. **Giriş Yapın:** Terminalden mağaza hesabınıza giriş yapın:
   ```bash
   snapcraft login
   ```
3. **Uygulama Adını Kaydedin:** Rezerve ettiğiniz adı Snap sistemine kaydedin:
   ```bash
   snapcraft register pdffigures2-gui
   ```
4. **Yayınlayın!** Paketinizi kararlı (stable) kanalına yükleyin:
   ```bash
   snapcraft upload --release=stable pdffigures2-gui_1.0_amd64.snap
   ```

Tebrikler! Birkaç dakikalık otomatik güvenlik taramasından sonra uygulamanız tüm dünyadaki **Ubuntu Software** mağazasında indirilebilir duruma gelecektir!

---

*İyi uykular dilerim! Yarın uyandığınızda kaldığımız yerden, acele etmeden adım adım bu süreci tamamlayabiliriz. Zihniniz dinlenmiş olarak projenizi resmi olarak yayınlamaya hazır olacağız.* 😊
