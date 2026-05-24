import os
import sys
import json
import subprocess
from PySide6 import QtCore, QtGui, QtWidgets

# Premium Ubuntu Yaru-Dark Inspired QSS Stylesheet
UBUNTU_YARU_DARK_QSS = """
QMainWindow {
    background-color: #1E1E1E;
    color: #E3E3E3;
    font-family: 'Ubuntu', 'Inter', 'Segoe UI', sans-serif;
}

QFrame#SidebarFrame {
    background-color: #181818;
    border-right: 1px solid #2D2D2D;
}

QLabel#LogoLabel {
    color: #E95420; /* Ubuntu Orange */
    font-size: 20px;
    font-weight: bold;
}

QLabel#SubtitleLabel {
    color: #8C8C8C;
    font-size: 11px;
}

/* Navigation Buttons */
QPushButton#SidebarButton {
    background-color: transparent;
    color: #AEAEAE;
    border: none;
    border-radius: 6px;
    padding: 10px 15px;
    text-align: left;
    font-weight: bold;
    font-size: 13px;
}
QPushButton#SidebarButton:hover {
    background-color: #2D2D2D;
    color: #FFFFFF;
}
QPushButton#SidebarButton:checked {
    background-color: #E95420;
    color: #FFFFFF;
}

/* Headers */
QLabel#SectionTitle {
    font-size: 24px;
    font-weight: bold;
    color: #FFFFFF;
}

/* Card layout container */
QFrame#DashboardPanel {
    background-color: transparent;
}

/* Settings Group Panel */
QFrame#SettingsPanel {
    background-color: #242424;
    border: 1px solid #2D2D2D;
    border-radius: 8px;
}

/* Input Fields */
QLineEdit {
    background-color: #1E1E1E;
    border: 1px solid #3E3E3E;
    border-radius: 6px;
    padding: 8px 12px;
    color: #FFFFFF;
    font-size: 13px;
}
QLineEdit:focus {
    border: 1px solid #E95420;
}
QLineEdit:disabled {
    background-color: #1A1A1A;
    color: #666666;
    border: 1px solid #2D2D2D;
}

/* Primary Accent Button */
QPushButton#ActionButton {
    background-color: #E95420;
    color: #FFFFFF;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 13px;
}
QPushButton#ActionButton:hover {
    background-color: #FC6F38;
}
QPushButton#ActionButton:pressed {
    background-color: #C74213;
}
QPushButton#ActionButton:disabled {
    background-color: #2D2D2D;
    color: #666666;
}

/* Secondary Button */
QPushButton#SecondaryButton {
    background-color: #2E2E2E;
    color: #E3E3E3;
    border: 1px solid #3E3E3E;
    border-radius: 6px;
    padding: 8px 15px;
    font-size: 13px;
}
QPushButton#SecondaryButton:hover {
    background-color: #3E3E3E;
    color: #FFFFFF;
    border: 1px solid #4E4E4E;
}
QPushButton#SecondaryButton:pressed {
    background-color: #1A1A1A;
}

/* Dropdown Menu */
QComboBox {
    background-color: #1E1E1E;
    border: 1px solid #3E3E3E;
    border-radius: 6px;
    padding: 6px 12px;
    color: #FFFFFF;
    min-width: 70px;
}
QComboBox:focus {
    border: 1px solid #E95420;
}
QComboBox::drop-down {
    border: none;
}
QComboBox QAbstractItemView {
    background-color: #242424;
    border: 1px solid #3E3E3E;
    selection-background-color: #E95420;
    selection-color: #FFFFFF;
    color: #FFFFFF;
}

/* Checkbox Switches */
QCheckBox {
    color: #E3E3E3;
    font-size: 12px;
    spacing: 8px;
}

/* Flat Sleek Progress Bar */
QProgressBar {
    border: 1px solid #2D2D2D;
    border-radius: 4px;
    background-color: #181818;
    text-align: center;
    color: transparent;
    height: 6px;
}
QProgressBar::chunk {
    background-color: #E95420;
    border-radius: 3px;
}

/* Text Terminal Console Log */
QTextEdit#ConsoleLog {
    background-color: #0F0F0F;
    border: 1px solid #2D2D2D;
    border-radius: 6px;
    font-family: 'Ubuntu Mono', 'Courier New', monospace;
    font-size: 13px;
    color: #DFDFDF;
    padding: 10px;
}

/* Scroll Area styling */
QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollBar:vertical {
    border: none;
    background-color: #1E1E1E;
    width: 8px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background-color: #3E3E3E;
    min-height: 20px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background-color: #E95420;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
}

/* Figure Card styling */
QFrame#FigureCard {
    background-color: #242424;
    border: 1px solid #2D2D2D;
    border-radius: 8px;
}
QFrame#FigureCard:hover {
    border: 1px solid #E95420;
    background-color: #2A2A2A;
}

QLabel#CardTitle {
    font-weight: bold;
    font-size: 13px;
    color: #FFFFFF;
}

QLabel#CardCaption {
    font-size: 11px;
    color: #AEAEAE;
}

/* Custom Image Containers */
QLabel#ThumbnailLabel {
    background-color: #FFFFFF; /* White canvas so black-text transparent graphics are visible! */
    border: 1px solid #2D2D2D;
    border-radius: 4px;
}
QFrame#ImageContainer {
    background-color: #FFFFFF; /* White background for full zoom so details are perfectly visible */
    border: 1px solid #2D2D2D;
    border-radius: 8px;
}

/* Dynamic Help text support */
QLabel#HelpTitle {
    font-size: 16px;
    font-weight: bold;
    color: #E95420;
}
QLabel#HelpText {
    font-size: 13px;
    color: #E3E3E3;
}
QLabel#CapHeader {
    font-weight: bold;
    color: #FFFFFF;
}
QLabel#PageLabel {
    color: #E95420;
    font-size: 13px;
}
QLabel#StatusText {
    color: #8C8C8C;
    font-size: 12px;
}
QLabel#GalleryCount {
    color: #8C8C8C;
    font-size: 13px;
    font-weight: bold;
}
QLabel#EmptyLabel {
    color: #8C8C8C;
    font-style: italic;
    font-size: 13px;
}
"""

# Premium Ubuntu Yaru-Light Inspired QSS Stylesheet
UBUNTU_YARU_LIGHT_QSS = """
QMainWindow {
    background-color: #F6F6F6;
    color: #2D2D2D;
    font-family: 'Ubuntu', 'Inter', 'Segoe UI', sans-serif;
}

QFrame#SidebarFrame {
    background-color: #EAEAEA;
    border-right: 1px solid #D5D5D5;
}

QLabel#LogoLabel {
    color: #E95420; /* Ubuntu Orange */
    font-size: 20px;
    font-weight: bold;
}

QLabel#SubtitleLabel {
    color: #6D6D6D;
    font-size: 11px;
}

/* Navigation Buttons */
QPushButton#SidebarButton {
    background-color: transparent;
    color: #5D5D5D;
    border: none;
    border-radius: 6px;
    padding: 10px 15px;
    text-align: left;
    font-weight: bold;
    font-size: 13px;
}
QPushButton#SidebarButton:hover {
    background-color: #DCDCDC;
    color: #1E1E1E;
}
QPushButton#SidebarButton:checked {
    background-color: #E95420;
    color: #FFFFFF;
}

/* Headers */
QLabel#SectionTitle {
    font-size: 24px;
    font-weight: bold;
    color: #1E1E1E;
}

/* Card layout container */
QFrame#DashboardPanel {
    background-color: transparent;
}

/* Settings Group Panel */
QFrame#SettingsPanel {
    background-color: #FFFFFF;
    border: 1px solid #D5D5D5;
    border-radius: 8px;
}

/* Input Fields */
QLineEdit {
    background-color: #FFFFFF;
    border: 1px solid #C0C0C0;
    border-radius: 6px;
    padding: 8px 12px;
    color: #1E1E1E;
    font-size: 13px;
}
QLineEdit:focus {
    border: 1px solid #E95420;
}
QLineEdit:disabled {
    background-color: #F0F0F0;
    color: #888888;
    border: 1px solid #E0E0E0;
}

/* Primary Accent Button */
QPushButton#ActionButton {
    background-color: #E95420;
    color: #FFFFFF;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 13px;
}
QPushButton#ActionButton:hover {
    background-color: #FC6F38;
}
QPushButton#ActionButton:pressed {
    background-color: #C74213;
}
QPushButton#ActionButton:disabled {
    background-color: #D5D5D5;
    color: #888888;
}

/* Secondary Button */
QPushButton#SecondaryButton {
    background-color: #E6E6E6;
    color: #2D2D2D;
    border: 1px solid #C0C0C0;
    border-radius: 6px;
    padding: 8px 15px;
    font-size: 13px;
}
QPushButton#SecondaryButton:hover {
    background-color: #DCDCDC;
    color: #1E1E1E;
    border: 1px solid #B0B0B0;
}
QPushButton#SecondaryButton:pressed {
    background-color: #CCCCCC;
}

/* Dropdown Menu */
QComboBox {
    background-color: #FFFFFF;
    border: 1px solid #C0C0C0;
    border-radius: 6px;
    padding: 6px 12px;
    color: #1E1E1E;
    min-width: 70px;
}
QComboBox:focus {
    border: 1px solid #E95420;
}
QComboBox::drop-down {
    border: none;
}
QComboBox QAbstractItemView {
    background-color: #FFFFFF;
    border: 1px solid #D5D5D5;
    selection-background-color: #E95420;
    selection-color: #FFFFFF;
    color: #1E1E1E;
}

/* Checkbox Switches */
QCheckBox {
    color: #2D2D2D;
    font-size: 12px;
    spacing: 8px;
}

/* Flat Sleek Progress Bar */
QProgressBar {
    border: 1px solid #D5D5D5;
    border-radius: 4px;
    background-color: #EAEAEA;
    text-align: center;
    color: transparent;
    height: 6px;
}
QProgressBar::chunk {
    background-color: #E95420;
    border-radius: 3px;
}

/* Text Terminal Console Log */
QTextEdit#ConsoleLog {
    background-color: #FAFAFA;
    border: 1px solid #D5D5D5;
    border-radius: 6px;
    font-family: 'Ubuntu Mono', 'Courier New', monospace;
    font-size: 13px;
    color: #1E1E1E;
    padding: 10px;
}

/* Scroll Area styling */
QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollBar:vertical {
    border: none;
    background-color: #F6F6F6;
    width: 8px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background-color: #C5C5C5;
    min-height: 20px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background-color: #E95420;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
}

/* Figure Card styling */
QFrame#FigureCard {
    background-color: #FFFFFF;
    border: 1px solid #D5D5D5;
    border-radius: 8px;
}
QFrame#FigureCard:hover {
    border: 1px solid #E95420;
    background-color: #F9F9F9;
}

QLabel#CardTitle {
    font-weight: bold;
    font-size: 13px;
    color: #1E1E1E;
}

QLabel#CardCaption {
    font-size: 11px;
    color: #6D6D6D;
}

/* Custom Image Containers */
QLabel#ThumbnailLabel {
    background-color: #FFFFFF;
    border: 1px solid #D5D5D5;
    border-radius: 4px;
}
QFrame#ImageContainer {
    background-color: #FFFFFF;
    border: 1px solid #D5D5D5;
    border-radius: 8px;
}

/* Dynamic Help text support */
QLabel#HelpTitle {
    font-size: 16px;
    font-weight: bold;
    color: #E95420;
}
QLabel#HelpText {
    font-size: 13px;
    color: #333333;
}
QLabel#CapHeader {
    font-weight: bold;
    color: #1E1E1E;
}
QLabel#PageLabel {
    color: #E95420;
    font-size: 13px;
}
QLabel#StatusText {
    color: #6D6D6D;
    font-size: 12px;
}
QLabel#GalleryCount {
    color: #6D6D6D;
    font-size: 13px;
    font-weight: bold;
}
QLabel#EmptyLabel {
    color: #6D6D6D;
    font-style: italic;
    font-size: 13px;
}
"""

class FigureExtractionWorker(QtCore.QThread):
    log_received = QtCore.Signal(str)
    finished_successfully = QtCore.Signal(str)
    failed = QtCore.Signal(str)

    def __init__(self, cmd, output_dir):
        super().__init__()
        self.cmd = cmd
        self.output_dir = output_dir

    def run(self):
        try:
            process = subprocess.Popen(
                self.cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # Stream output in real-time
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                self.log_received.emit(line.strip())

            process.wait()

            if process.returncode == 0:
                self.finished_successfully.emit(self.output_dir)
            else:
                self.failed.emit(f"Process exited with code {process.returncode}")
        except Exception as e:
            self.failed.emit(str(e))


class FigureCard(QtWidgets.QFrame):
    clicked = QtCore.Signal(dict)

    def __init__(self, fig, base_dir):
        super().__init__()
        self.setObjectName("FigureCard")
        self.fig = fig
        self.base_dir = base_dir
        
        # Grid layout for elements inside card
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # 1. Resolve & Load Image
        render_url = fig.get("renderURL", "")
        img_path = ""
        if render_url:
            if os.path.isabs(render_url):
                img_path = render_url
            else:
                img_path = os.path.join(base_dir, render_url)

        # Thumbnail Label
        self.img_label = QtWidgets.QLabel()
        self.img_label.setObjectName("ThumbnailLabel")
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setFixedHeight(120)

        if img_path and os.path.exists(img_path):
            pixmap = QtGui.QPixmap(img_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    QtCore.QSize(180, 120),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation
                )
                self.img_label.setPixmap(scaled_pixmap)
            else:
                self.img_label.setText("[Invalid Image]")
        else:
            self.img_label.setText("[No Render Available]")

        layout.addWidget(self.img_label)

        # 2. Title / Name info
        fig_type = fig.get("figType", "Figure")
        fig_name = fig.get("name", "")
        fig_page = fig.get("page", 0) + 1
        
        self.title_lbl = QtWidgets.QLabel(f"{fig_type} {fig_name} (Page {fig_page})")
        self.title_lbl.setObjectName("CardTitle")
        layout.addWidget(self.title_lbl)

        # 3. Caption Excerpt
        fig_caption = fig.get("caption", "No caption.")
        truncated_caption = fig_caption[:65] + "..." if len(fig_caption) > 65 else fig_caption
        
        self.caption_lbl = QtWidgets.QLabel(truncated_caption)
        self.caption_lbl.setObjectName("CardCaption")
        self.caption_lbl.setWordWrap(True)
        self.caption_lbl.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        layout.addWidget(self.caption_lbl)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(self.fig)
        super().mousePressEvent(event)


class ZoomDialog(QtWidgets.QDialog):
    def __init__(self, fig, base_dir, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Preview - {fig.get('figType', 'Figure')} {fig.get('name', '')}")
        self.resize(900, 650)
        self.apply_color_scheme()
        QtGui.QGuiApplication.styleHints().colorSchemeChanged.connect(self.apply_color_scheme)

        # Main horizontal layout
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Left panel: Image container
        img_container = QtWidgets.QFrame()
        img_container.setObjectName("ImageContainer")
        img_layout = QtWidgets.QVBoxLayout(img_container)
        img_layout.setContentsMargins(10, 10, 10, 10)

        # Resolve image path
        render_url = fig.get("renderURL", "")
        img_path = ""
        if render_url:
            if os.path.isabs(render_url):
                img_path = render_url
            else:
                img_path = os.path.join(base_dir, render_url)

        self.img_lbl = QtWidgets.QLabel()
        self.img_lbl.setAlignment(QtCore.Qt.AlignCenter)
        if img_path and os.path.exists(img_path):
            pixmap = QtGui.QPixmap(img_path)
            if not pixmap.isNull():
                # Scale nicely keeping aspect ratio
                scaled_pixmap = pixmap.scaled(
                    QtCore.QSize(500, 580),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation
                )
                self.img_lbl.setPixmap(scaled_pixmap)
            else:
                self.img_lbl.setText("Error loading figure preview.")
        else:
            self.img_lbl.setText("No rendering image available.")

        img_layout.addWidget(self.img_lbl)
        main_layout.addWidget(img_container, stretch=3)

        # Right panel: Information and full caption
        info_panel = QtWidgets.QFrame()
        info_layout = QtWidgets.QVBoxLayout(info_panel)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(10)

        fig_type = fig.get("figType", "Figure")
        fig_name = fig.get("name", "")
        fig_page = fig.get("page", 0) + 1

        title_lbl = QtWidgets.QLabel(f"{fig_type} {fig_name}")
        title_lbl.setObjectName("SectionTitle")
        info_layout.addWidget(title_lbl)

        page_lbl = QtWidgets.QLabel(f"Document Page Location: <b>{fig_page}</b>")
        page_lbl.setObjectName("PageLabel")
        info_layout.addWidget(page_lbl)

        info_layout.addSpacing(10)

        cap_header = QtWidgets.QLabel("Full Extracted Caption Text:")
        cap_header.setObjectName("CapHeader")
        info_layout.addWidget(cap_header)

        # Scrollable caption text area
        caption_box = QtWidgets.QTextEdit()
        caption_box.setReadOnly(True)
        caption_box.setObjectName("ConsoleLog")
        caption_box.setText(fig.get("caption", "No caption text available."))
        info_layout.addWidget(caption_box)

        # Close button
        btn_close = QtWidgets.QPushButton("Close Preview")
        btn_close.setObjectName("SecondaryButton")
        btn_close.clicked.connect(self.accept)
        info_layout.addWidget(btn_close)

        main_layout.addWidget(info_panel, stretch=2)

    def apply_color_scheme(self):
        scheme = QtGui.QGuiApplication.styleHints().colorScheme()
        if scheme == QtCore.Qt.ColorScheme.Dark:
            self.setStyleSheet(UBUNTU_YARU_DARK_QSS)
        else:
            self.setStyleSheet(UBUNTU_YARU_LIGHT_QSS)


class PDFFiguresGUI(QtWidgets.QMainWindow):
    HELP_TEXT_TR = {
        "usage": (
            "1. <b>Giriş Seçimi:</b> 'Browse File' butonunu kullanarak tek bir PDF belgesi veya "
            "'Browse Folder' butonuyla birden fazla PDF içeren klasörü seçin.<br>"
            "2. <b>Çıkış Seçimi:</b> Çıkarılacak görsellerin ve verilerin kaydedileceği klasörü belirtin.<br>"
            "3. <b>Çıkarma Seçenekleri:</b><br>"
            "   • <i>Save Figure PNGs:</i> Görselleri resim olarak kaydeder.<br>"
            "   • <i>Save JSON Metadata:</i> Her bir görselin sayfa, altyazı (caption) ve koordinat bilgilerini içeren JSON dosyası üretir.<br>"
            "   • <i>Render Visualizations:</i> Makale sayfalarında tespit edilen bölgeleri renklendirip görselleştirme çıktıları oluşturur.<br>"
            "   • <i>Image DPI:</i> Görsellerin çözünürlüğünü ayarlar (akademik çıktılar için 150 veya 300 DPI önerilir).<br>"
            "4. <b>Başlatma:</b> 'START EXTRACTION' butonuna basarak işlemi başlatın. Log penceresinden süreci canlı izleyebilirsiniz.<br>"
            "5. <b>Galeri Görünümü:</b> İşlem bittiğinde görseller otomatik olarak 'Figure Gallery' sekmesine yüklenecektir. "
            "Görsellere tıklayarak açıklamalarını ve büyük hallerini inceleyebilirsiniz."
        ),
        "trouble": (
            "PDFFigures 2.0 motoru gelişmiş bilgisayarlı görü algoritmaları kullanır, ancak bazı PDF türlerinde grafiklerin sınırlarını tespit etmekte zorlanabilir. Bu durumda aşağıdaki yöntemleri uygulayabilirsiniz:<br><br>"
            "<b>1. Tarama (Scanned / Görüntü Tabanlı) PDF Belgeleri:</b><br>"
            "Eğer PDF dosyası tarayıcıdan geçirilmiş resimlerden oluşuyorsa ve metinler seçilemiyorsa, motor altyazıları veya grafikleri bulamaz. "
            "<i>Çözüm:</i> PDF belgesini <b>OCRmyPDF</b> veya benzeri bir OCR aracından geçirerek aranabilir metin katmanı ekledikten sonra tekrar deneyin.<br><br>"
            "<b>2. Eksik Grafik Dekoderleri (JPEG2000 / JBIG2 Formatları):</b><br>"
            "Makaledeki görseller JPEG2000 (.jp2) veya JBIG2 formatlarında sıkıştırılmış olabilir. Bu durumda Java motoru (PDFBox) lisans kısıtlamaları nedeniyle görselleri okuyamaz ve atlar. "
            "<i>Çözüm:</i> Projenin <code>build.sbt</code> dosyasında yer alan <code>jai-imageio-core</code>, <code>jai-imageio-jpeg2000</code> ve <code>levigo-jbig2-imageio</code> bağımlılıklarının önündeki yorum (//) işaretlerini kaldırıp motoru <code>sbt assembly</code> komutu ile tekrar derleyin.<br><br>"
            "<b>3. Bölgesiz Altyazılar (Regionless Captions - Seçeneği -c):</b><br>"
            "Motor bazen altyazıyı (örneğin 'Figure 1:') bulur fakat görselin sınırlarını (bounding box) ayırt edemediği için o figürü tamamen yok sayar. "
            "<i>Çözüm:</i> Kontrol panelinden <b>'Save Regionless Captions (-c)'</b> seçeneğini işaretleyin. Bu sayede görsel çıkarılamasa dahi altyazı ve sayfa bilgileri JSON dosyasına yazılır ve galeriye eklenir.<br><br>"
            "<b>4. Hataları Yok Sayma (Ignore Page Errors - Seçeneği -e):</b><br>"
            "İşlem sırasında bozuk sayfa yapıları nedeniyle motor hata verip durabilir. "
            "<i>Çözüm:</i> <b>'Ignore Page Errors (-e)'</b> seçeneğini işaretleyerek hatalı sayfaların atlanmasını ve kalan sayfaların işlenmeye devam edilmesini sağlayabilirsiniz.<br><br>"
            "<b>5. DPI Çözünürlüğünü Yükseltme:</b><br>"
            "Karmaşık veya küçük figürlerin tespiti için DPI değerini 200 veya 300'e çıkararak görsel sınırlarının netleşmesini sağlayın."
        )
    }

    HELP_TEXT_EN = {
        "usage": (
            "1. <b>Input Selection:</b> Click 'Browse File' to select a single PDF, or 'Browse Folder' to select a directory containing multiple PDFs.<br>"
            "2. <b>Output Directory:</b> Choose the directory where the extracted figures and metadata should be saved.<br>"
            "3. <b>Extraction Options:</b><br>"
            "   • <i>Save Figure PNGs:</i> Renders and saves figures as individual images.<br>"
            "   • <i>Save JSON Metadata:</i> Generates a JSON file containing metadata (page, caption, and coordinates) for each figure.<br>"
            "   • <i>Render Visualizations:</i> Creates visualizations highlight-marking the detected regions on document pages.<br>"
            "   • <i>Image DPI:</i> Controls resolution of saved figures (150 or 300 DPI is recommended for publication-quality output).<br>"
            "4. <b>Execution:</b> Click 'START EXTRACTION'. You can monitor the real-time execution in the log console.<br>"
            "5. <b>Gallery View:</b> Once processing is completed, extracted figures are automatically loaded into the 'Figure Gallery' tab. Click on any figure to zoom in and view its full caption."
        ),
        "trouble": (
            "PDFFigures 2.0 uses computer vision algorithms, but it may fail to resolve graphics in certain PDF types. Try the following solutions:<br><br>"
            "<b>1. Scanned (Image-only) PDF Documents:</b><br>"
            "If the PDF consists of scanned pages without digital text, the engine cannot read captions or identify visual coordinates. "
            "<i>Solution:</i> Use an OCR tool (like <b>OCRmyPDF</b> or <b>Tesseract</b>) to add a searchable text layer to the PDF before processing.<br><br>"
            "<b>2. Missing Image Decoders (JPEG2000 / JBIG2 Formats):</b><br>"
            "Figures in some papers use JPEG2000 (.jp2) or JBIG2 compression. The default Java PDFBox engine cannot decode them due to license exclusions. "
            "<i>Solution:</i> Uncomment the <code>jai-imageio-core</code>, <code>jai-imageio-jpeg2000</code>, and <code>levigo-jbig2-imageio</code> dependencies in <code>build.sbt</code> and rebuild the project using <code>sbt assembly</code>.<br><br>"
            "<b>3. Regionless Captions (-c flag):</b><br>"
            "Sometimes the engine identifies a caption (e.g. 'Figure 1:') but cannot determine the exact graphic boundary, discarding the figure. "
            "<i>Solution:</i> Enable <b>'Save Regionless Captions (-c)'</b> to preserve the captions and page indices in the JSON file and load them into the gallery.<br><br>"
            "<b>4. Ignore Page Errors (-e flag):</b><br>"
            "Corrupted page structures can halt the batch execution. "
            "<i>Solution:</i> Check <b>'Ignore Page Errors (-e)'</b> to skip corrupted pages and continue extracting the rest of the document.<br><br>"
            "<b>5. Image DPI Resolution:</b><br>"
            "Increase the DPI to 200 or 300 to improve detail recognition and shape clustering for complex figures."
        )
    }

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDFFigures 2.0 - Scientific Figure Extractor")
        self.resize(1150, 750)
        self.setMinimumSize(1000, 650)

        # Listen to system color scheme changes (Light/Dark mode)
        self.apply_color_scheme()
        QtGui.QGuiApplication.styleHints().colorSchemeChanged.connect(self.apply_color_scheme)

        # Set Window Icon
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon_v3.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QtGui.QIcon(icon_path))

        # Default path setup
        self.jar_path = "/home/ebupi/pdffigures2/pdffigures2.jar"
        self.extracted_figures = []
        self.json_base_dir = ""
        self.worker = None

        # Build UI layout structure
        self.setup_ui()

    def apply_color_scheme(self):
        scheme = QtGui.QGuiApplication.styleHints().colorScheme()
        if scheme == QtCore.Qt.ColorScheme.Dark:
            self.setStyleSheet(UBUNTU_YARU_DARK_QSS)
        else:
            self.setStyleSheet(UBUNTU_YARU_LIGHT_QSS)

    def setup_ui(self):
        # Main central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QtWidgets.QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ----------------- SIDEBAR -----------------
        self.sidebar = QtWidgets.QFrame()
        self.sidebar.setObjectName("SidebarFrame")
        self.sidebar.setFixedWidth(240)
        sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(20, 30, 20, 20)
        sidebar_layout.setSpacing(5)

        # Sidebar Title Block
        logo_label = QtWidgets.QLabel("PDFFigures 2.0")
        logo_label.setObjectName("LogoLabel")
        sidebar_layout.addWidget(logo_label)

        sub_label = QtWidgets.QLabel("AI Figure & Table Extractor")
        sub_label.setObjectName("SubtitleLabel")
        sidebar_layout.addWidget(sub_label)

        sidebar_layout.addSpacing(35)

        # Sidebar Buttons Group
        self.btn_group = QtWidgets.QButtonGroup(self)
        self.btn_group.setExclusive(True)

        self.btn_extractor = QtWidgets.QPushButton("  Extractor Dashboard")
        self.btn_extractor.setObjectName("SidebarButton")
        self.btn_extractor.setCheckable(True)
        self.btn_extractor.setChecked(True)
        self.btn_extractor.setIcon(QtGui.QIcon.fromTheme("dashboard"))
        self.btn_extractor.clicked.connect(self.show_extractor_view)
        sidebar_layout.addWidget(self.btn_extractor)
        self.btn_group.addButton(self.btn_extractor)

        self.btn_gallery = QtWidgets.QPushButton("  Figure Gallery")
        self.btn_gallery.setObjectName("SidebarButton")
        self.btn_gallery.setCheckable(True)
        self.btn_gallery.setIcon(QtGui.QIcon.fromTheme("image-x-generic"))
        self.btn_gallery.clicked.connect(self.show_gallery_view)
        sidebar_layout.addWidget(self.btn_gallery)
        self.btn_group.addButton(self.btn_gallery)
        self.btn_help = QtWidgets.QPushButton("  User Guide")
        self.btn_help.setObjectName("SidebarButton")
        self.btn_help.setCheckable(True)
        self.btn_help.setIcon(QtGui.QIcon.fromTheme("help-browser"))
        self.btn_help.clicked.connect(self.show_help_view)
        sidebar_layout.addWidget(self.btn_help)
        self.btn_group.addButton(self.btn_help)

        sidebar_layout.addStretch()

        # Engine Status Indicators at Sidebar Bottom
        status_frame = QtWidgets.QFrame()
        status_layout = QtWidgets.QHBoxLayout(status_frame)
        status_layout.setContentsMargins(0, 0, 0, 0)
        status_layout.setSpacing(6)

        self.status_led = QtWidgets.QLabel("●")
        self.status_led.setStyleSheet("color: #10B981; font-size: 14px;") # Green
        status_layout.addWidget(self.status_led)

        self.status_text = QtWidgets.QLabel("Engine Connected")
        self.status_text.setObjectName("StatusText")
        status_layout.addWidget(self.status_text)
        status_layout.addStretch()

        sidebar_layout.addWidget(status_frame)

        main_layout.addWidget(self.sidebar)

        # ----------------- MAIN PAGES CONTAINER -----------------
        self.pages = QtWidgets.QStackedWidget()
        
        # 1. Extractor Dashboard Page
        self.extractor_page = QtWidgets.QWidget()
        self.setup_extractor_page()
        self.pages.addWidget(self.extractor_page)

        # 2. Figures Gallery Page
        self.gallery_page = QtWidgets.QWidget()
        self.setup_gallery_page()
        self.pages.addWidget(self.gallery_page)

        # 3. Help & Guide Page
        self.help_page = QtWidgets.QWidget()
        self.setup_help_page()
        self.pages.addWidget(self.help_page)

        main_layout.addWidget(self.pages)

    def show_extractor_view(self):
        self.btn_extractor.setChecked(True)
        self.pages.setCurrentIndex(0)

    def show_gallery_view(self):
        self.btn_gallery.setChecked(True)
        self.pages.setCurrentIndex(1)
        self.refresh_gallery_display()

    def show_help_view(self):
        self.btn_help.setChecked(True)
        self.pages.setCurrentIndex(2)

    def on_json_toggled(self, checked):
        if checked:
            self.chk_viz.setChecked(False)

    def on_viz_toggled(self, checked):
        if checked:
            self.chk_json.setChecked(False)

    def setup_extractor_page(self):
        layout = QtWidgets.QVBoxLayout(self.extractor_page)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Header Title
        title_lbl = QtWidgets.QLabel("Extractor Dashboard")
        title_lbl.setObjectName("SectionTitle")
        layout.addWidget(title_lbl)

        # settings panel
        settings_panel = QtWidgets.QFrame()
        settings_panel.setObjectName("SettingsPanel")
        settings_layout = QtWidgets.QGridLayout(settings_panel)
        settings_layout.setContentsMargins(20, 20, 20, 20)
        settings_layout.setSpacing(12)

        # Row 0: Input path
        settings_layout.addWidget(QtWidgets.QLabel("<b>PDF Input File or Directory:</b>"), 0, 0, 1, 4)
        
        self.entry_input = QtWidgets.QLineEdit()
        self.entry_input.setPlaceholderText("Select a PDF document or a folder of PDFs...")
        settings_layout.addWidget(self.entry_input, 1, 0, 1, 2)

        self.btn_browse_file = QtWidgets.QPushButton("Browse File")
        self.btn_browse_file.setObjectName("SecondaryButton")
        self.btn_browse_file.clicked.connect(self.browse_file)
        settings_layout.addWidget(self.btn_browse_file, 1, 2)

        self.btn_browse_folder = QtWidgets.QPushButton("Browse Folder")
        self.btn_browse_folder.setObjectName("SecondaryButton")
        self.btn_browse_folder.clicked.connect(self.browse_folder)
        settings_layout.addWidget(self.btn_browse_folder, 1, 3)

        # Row 2: Output path
        settings_layout.addWidget(QtWidgets.QLabel("<b>Output Directory:</b>"), 2, 0, 1, 4)
        
        self.entry_output = QtWidgets.QLineEdit()
        self.entry_output.setPlaceholderText("Select where to save extracted figures and metadata...")
        settings_layout.addWidget(self.entry_output, 3, 0, 1, 3)

        self.btn_browse_out = QtWidgets.QPushButton("Browse")
        self.btn_browse_out.setObjectName("SecondaryButton")
        self.btn_browse_out.clicked.connect(self.browse_output)
        settings_layout.addWidget(self.btn_browse_out, 3, 4)

        # Row 4: Switches & Configurations
        config_frame = QtWidgets.QFrame()
        config_layout = QtWidgets.QVBoxLayout(config_frame)
        config_layout.setContentsMargins(0, 5, 0, 5)
        config_layout.setSpacing(10)

        # Row 4a: Checkboxes
        chk_layout = QtWidgets.QHBoxLayout()
        chk_layout.setSpacing(15)

        self.chk_images = QtWidgets.QCheckBox("Save Figure PNGs")
        self.chk_images.setChecked(True)
        chk_layout.addWidget(self.chk_images)

        self.chk_json = QtWidgets.QCheckBox("Save JSON Metadata (-d)")
        self.chk_json.setChecked(True)
        self.chk_json.setToolTip("Save figure metadata to JSON. Cannot be combined with Full Text JSON.")
        self.chk_json.toggled.connect(self.on_json_toggled)
        chk_layout.addWidget(self.chk_json)

        self.chk_viz = QtWidgets.QCheckBox("Save Full Text & Figures (-g)")
        self.chk_viz.setToolTip("Save full text structure and figures to JSON. Cannot be combined with JSON Metadata.")
        self.chk_viz.toggled.connect(self.on_viz_toggled)
        chk_layout.addWidget(self.chk_viz)

        self.chk_regionless = QtWidgets.QCheckBox("Save Regionless Captions (-c)")
        self.chk_regionless.setToolTip("Include captions in metadata even if figure bounding box cannot be resolved")
        chk_layout.addWidget(self.chk_regionless)

        self.chk_errors = QtWidgets.QCheckBox("Ignore Page Errors (-e)")
        self.chk_errors.setToolTip("Skip pages with errors instead of failing entire process")
        chk_layout.addWidget(self.chk_errors)

        chk_layout.addStretch()
        config_layout.addLayout(chk_layout)

        # Row 4b: Settings Inputs (DPI, Prefix)
        inputs_layout = QtWidgets.QHBoxLayout()
        inputs_layout.setSpacing(15)

        inputs_layout.addWidget(QtWidgets.QLabel("Image DPI:"))
        self.combo_dpi = QtWidgets.QComboBox()
        self.combo_dpi.addItems(["72", "100", "150", "200", "300"])
        self.combo_dpi.setCurrentText("150")
        inputs_layout.addWidget(self.combo_dpi)

        inputs_layout.addWidget(QtWidgets.QLabel("Figure Prefix:"))
        self.entry_prefix = QtWidgets.QLineEdit("fig")
        self.entry_prefix.setFixedWidth(80)
        inputs_layout.addWidget(self.entry_prefix)

        inputs_layout.addStretch()
        config_layout.addLayout(inputs_layout)

        settings_layout.addWidget(config_frame, 4, 0, 1, 4)

        layout.addWidget(settings_panel)

        # Run action block
        action_layout = QtWidgets.QVBoxLayout()
        action_layout.setSpacing(10)

        self.btn_run = QtWidgets.QPushButton("START EXTRACTION")
        self.btn_run.setObjectName("ActionButton")
        self.btn_run.setFixedHeight(45)
        self.btn_run.clicked.connect(self.run_extraction)
        action_layout.addWidget(self.btn_run)

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(0)
        action_layout.addWidget(self.progress_bar)

        layout.addLayout(action_layout)

        # Real-time Monospace Console Terminal Log
        log_header = QtWidgets.QLabel("<b>Real-Time Execution Console Log:</b>")
        layout.addWidget(log_header)

        self.console_log = QtWidgets.QTextEdit()
        self.console_log.setObjectName("ConsoleLog")
        self.console_log.setReadOnly(True)
        layout.addWidget(self.console_log, stretch=1)

    def setup_gallery_page(self):
        layout = QtWidgets.QVBoxLayout(self.gallery_page)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Gallery Title Header
        header_frame = QtWidgets.QFrame()
        header_layout = QtWidgets.QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        title_lbl = QtWidgets.QLabel("Extracted Figure Gallery")
        title_lbl.setObjectName("SectionTitle")
        header_layout.addWidget(title_lbl)

        header_layout.addStretch()

        self.btn_load_json = QtWidgets.QPushButton("Load Extraction JSON")
        self.btn_load_json.setObjectName("SecondaryButton")
        self.btn_load_json.clicked.connect(self.browse_load_json)
        header_layout.addWidget(self.btn_load_json)

        layout.addWidget(header_frame)

        # Scrollable widget container for Card Grid
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.gallery_container = QtWidgets.QWidget()
        self.gallery_container.setStyleSheet("background-color: transparent;")
        self.gallery_grid = QtWidgets.QGridLayout(self.gallery_container)
        self.gallery_grid.setContentsMargins(0, 0, 0, 0)
        self.gallery_grid.setSpacing(15)

        self.scroll_area.setWidget(self.gallery_container)
        layout.addWidget(self.scroll_area, stretch=1)

        # Footer layout for status/statistics
        footer_layout = QtWidgets.QHBoxLayout()
        footer_layout.setContentsMargins(0, 0, 0, 0)
        footer_layout.addStretch()

        self.lbl_gallery_count = QtWidgets.QLabel("Total Figures: 0")
        self.lbl_gallery_count.setObjectName("GalleryCount")
        footer_layout.addWidget(self.lbl_gallery_count)

        layout.addLayout(footer_layout)

    def setup_help_page(self):
        layout = QtWidgets.QVBoxLayout(self.help_page)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Header Frame for Title and Language Switcher
        header_frame = QtWidgets.QFrame()
        header_layout = QtWidgets.QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.help_title_lbl = QtWidgets.QLabel("User Guide & Troubleshooting")
        self.help_title_lbl.setObjectName("SectionTitle")
        header_layout.addWidget(self.help_title_lbl)

        header_layout.addStretch()

        # Language Switch Button
        self.btn_lang = QtWidgets.QPushButton("Türkçe'ye Geç")
        self.btn_lang.setObjectName("SecondaryButton")
        self.btn_lang.setCheckable(True)
        self.btn_lang.clicked.connect(self.toggle_help_language)
        header_layout.addWidget(self.btn_lang)

        layout.addWidget(header_frame)

        # Scrollable container for help content
        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent;")
        
        help_container = QtWidgets.QWidget()
        help_container.setStyleSheet("background-color: transparent;")
        help_layout = QtWidgets.QVBoxLayout(help_container)
        help_layout.setContentsMargins(0, 0, 0, 0)
        help_layout.setSpacing(20)

        # CARD 1: How to Use
        card_usage = QtWidgets.QFrame()
        card_usage.setObjectName("SettingsPanel")
        card_usage_layout = QtWidgets.QVBoxLayout(card_usage)
        card_usage_layout.setContentsMargins(20, 20, 20, 20)
        card_usage_layout.setSpacing(10)

        self.usage_title = QtWidgets.QLabel("📖 How to Use the Application")
        self.usage_title.setObjectName("HelpTitle")
        card_usage_layout.addWidget(self.usage_title)

        self.usage_text = QtWidgets.QLabel(self.HELP_TEXT_EN["usage"])
        self.usage_text.setObjectName("HelpText")
        self.usage_text.setWordWrap(True)
        card_usage_layout.addWidget(self.usage_text)

        help_layout.addWidget(card_usage)

        # CARD 2: Troubleshooting
        card_trouble = QtWidgets.QFrame()
        card_trouble.setObjectName("SettingsPanel")
        card_trouble_layout = QtWidgets.QVBoxLayout(card_trouble)
        card_trouble_layout.setContentsMargins(20, 20, 20, 20)
        card_trouble_layout.setSpacing(10)

        self.trouble_title = QtWidgets.QLabel("⚠️ Graphics Not Found & Troubleshooting")
        self.trouble_title.setObjectName("HelpTitle")
        card_trouble_layout.addWidget(self.trouble_title)

        self.trouble_text = QtWidgets.QLabel(self.HELP_TEXT_EN["trouble"])
        self.trouble_text.setObjectName("HelpText")
        self.trouble_text.setWordWrap(True)
        card_trouble_layout.addWidget(self.trouble_text)

        help_layout.addWidget(card_trouble)

        help_layout.addStretch()
        scroll.setWidget(help_container)
        layout.addWidget(scroll, stretch=1)

    def toggle_help_language(self):
        if self.btn_lang.isChecked():
            # Switch to Turkish
            self.btn_lang.setText("Switch to English")
            self.help_title_lbl.setText("Kullanım Kılavuzu & Sorun Giderme")
            self.usage_title.setText("📖 Uygulama Nasıl Kullanılır?")
            self.usage_text.setText(self.HELP_TEXT_TR["usage"])
            self.trouble_title.setText("⚠️ Grafiklerin Bulunamaması & Çözüm Yolları")
            self.trouble_text.setText(self.HELP_TEXT_TR["trouble"])
        else:
            # Switch to English
            self.btn_lang.setText("Türkçe'ye Geç")
            self.help_title_lbl.setText("User Guide & Troubleshooting")
            self.usage_title.setText("📖 How to Use the Application")
            self.usage_text.setText(self.HELP_TEXT_EN["usage"])
            self.trouble_title.setText("⚠️ Graphics Not Found & Troubleshooting")
            self.trouble_text.setText(self.HELP_TEXT_EN["trouble"])

    # ----------------- BROWSE ACTIONS (GNOME NATIVE INTEGRATION) -----------------
    def browse_file(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select PDF Document", "", "PDF Documents (*.pdf)"
        )
        if filename:
            self.entry_input.setText(filename)
            # Suggest output directory nearby
            if not self.entry_output.text():
                self.entry_output.setText(
                    os.path.join(os.path.dirname(filename), "extracted_figures")
                )

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select PDF Directory", ""
        )
        if directory:
            self.entry_input.setText(directory)
            # Suggest output directory nearby
            if not self.entry_output.text():
                self.entry_output.setText(
                    os.path.join(directory, "extracted_figures")
                )

    def browse_output(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Output Directory", ""
        )
        if directory:
            self.entry_output.setText(directory)

    # ----------------- REAL-TIME LOGGING & RUN -----------------
    def append_log(self, text):
        clean_text = text.strip()
        if not clean_text:
            return

        # Simple terminal ANSI style color coding
        color = "#E3E3E3" # Default gray
        if "INFO" in clean_text:
            color = "#60A5FA" # Light blue
        elif "DEBUG" in clean_text:
            color = "#6B7280" # Slate dark gray
        elif "Finished" in clean_text:
            color = "#34D399" # Emerald green
        elif "ERROR" in clean_text or "Failed" in clean_text:
            color = "#F87171" # Coral red

        formatted_html = f"<span style='color: {color};'>{clean_text}</span><br>"
        self.console_log.insertHtml(formatted_html)
        
        # Auto-scroll console log
        self.console_log.verticalScrollBar().setValue(
            self.console_log.verticalScrollBar().maximum()
        )

    def run_extraction(self):
        if self.worker and self.worker.isRunning():
            return

        input_path = self.entry_input.text().strip()
        output_dir = self.entry_output.text().strip()

        if not input_path:
            QtWidgets.QMessageBox.critical(self, "Input Error", "Please specify a valid PDF Input File or Directory.")
            return
        if not output_dir:
            QtWidgets.QMessageBox.critical(self, "Output Error", "Please specify a valid Output Directory.")
            return

        os.makedirs(output_dir, exist_ok=True)

        if not os.path.exists(self.jar_path):
            QtWidgets.QMessageBox.critical(
                self, "Engine Error", 
                f"PDFFigures compiled engine was not found at:\n{self.jar_path}\n\nPlease build the assembly JAR first."
            )
            return

        # Prepare Command Line Args
        cmd = ["java", "-jar", self.jar_path, input_path]
        
        if self.chk_images.isChecked():
            prefix = self.entry_prefix.text().strip() or "fig"
            cmd.extend(["-m", os.path.join(output_dir, prefix)])
        if self.chk_json.isChecked():
            # JSON output prefix (must end with separator)
            cmd.extend(["-d", os.path.join(output_dir, "")])
        if self.chk_viz.isChecked():
            prefix = self.entry_prefix.text().strip() or "fig"
            cmd.extend(["-g", os.path.join(output_dir, "viz_" + prefix)])
        if self.chk_regionless.isChecked():
            cmd.append("-c")
        if self.chk_errors.isChecked():
            cmd.append("-e")

        cmd.extend(["-i", self.combo_dpi.currentText()])

        # Clear logs & lock down UI
        self.console_log.clear()
        self.append_log(">>> INITIALIZING NATIVE EXTRACTION ENGINE...")
        self.append_log(f">>> Command: {' '.join(cmd)}")
        self.append_log(">>> Running in dedicated thread... please wait.\n")

        self.btn_run.setEnabled(False)
        self.btn_run.setText("EXTRACTING...")
        self.progress_bar.setRange(0, 0) # Smooth animated marquee mode
        
        self.status_led.setStyleSheet("color: #F59E0B; font-size: 14px;") # Warning amber
        self.status_text.setText("Extracting figures...")

        # Spawn Threaded Worker to keep GUI incredibly responsive
        self.worker = FigureExtractionWorker(cmd, output_dir)
        self.worker.log_received.connect(self.append_log)
        self.worker.finished_successfully.connect(self.extraction_success)
        self.worker.failed.connect(self.extraction_failed)
        self.worker.start()

    def extraction_success(self, output_dir):
        self.btn_run.setEnabled(True)
        self.btn_run.setText("START EXTRACTION")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(100)

        self.status_led.setStyleSheet("color: #10B981; font-size: 14px;") # Green
        self.status_text.setText("Extraction Successful!")
        self.append_log("\n>>> EXTRACTION COMPLETED SUCCESSFULLY!")

        # Dynamic scanner to load the latest generated JSON file automatically
        try:
            json_files = [f for f in os.listdir(output_dir) if f.endswith(".json")]
            if json_files:
                json_files = [os.path.join(output_dir, f) for f in json_files]
                json_files.sort(key=os.path.getmtime, reverse=True)
                latest_json = json_files[0]

                self.load_figures_json(latest_json)
                QtWidgets.QMessageBox.information(
                    self, "Extraction Success", 
                    f"Figures successfully extracted and loaded from:\n{os.path.basename(latest_json)}\n\nOpening Figure Gallery!"
                )
                self.show_gallery_view()
            else:
                QtWidgets.QMessageBox.information(self, "Extraction Success", "Figures successfully extracted.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Load Error", f"Extraction completed, but failed to load gallery:\n{e}")

    def extraction_failed(self, error_message):
        self.btn_run.setEnabled(True)
        self.btn_run.setText("START EXTRACTION")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        self.status_led.setStyleSheet("color: #EF4444; font-size: 14px;") # Red
        self.status_text.setText("Extraction Failed")
        self.append_log(f"\n>>> ENGINE FAILED: {error_message}")
        QtWidgets.QMessageBox.critical(self, "Extraction Failed", f"Extraction failed:\n{error_message}")

    # ----------------- GALLERY CORE LOGIC -----------------
    def browse_load_json(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Load PDFFigures JSON Metadata", "", "JSON Files (*.json)"
        )
        if filename:
            self.load_figures_json(filename)
            self.refresh_gallery_display()

    def load_figures_json(self, json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if isinstance(data, dict):
                if "figures" in data:
                    self.extracted_figures = data["figures"]
                else:
                    self.extracted_figures = []
            elif isinstance(data, list):
                self.extracted_figures = data
            else:
                self.extracted_figures = []
                
            self.json_base_dir = os.path.dirname(json_path)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "JSON Parse Error", f"Failed to load JSON file:\n{e}")

    def refresh_gallery_display(self):
        # Clear existing cards in layout
        while self.gallery_grid.count():
            item = self.gallery_grid.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        total_figures = len(self.extracted_figures)
        self.lbl_gallery_count.setText(f"Total Figures Extracted: {total_figures}")

        if not self.extracted_figures:
            self.lbl_gallery_count.setText("Total Figures Extracted: 0")
            empty_lbl = QtWidgets.QLabel("No figures loaded. Select 'Extractor Dashboard' to run extraction or load a JSON file.")
            empty_lbl.setAlignment(QtCore.Qt.AlignCenter)
            empty_lbl.setObjectName("EmptyLabel")
            self.gallery_grid.addWidget(empty_lbl, 0, 0)
            return

        row, col = 0, 0
        for fig in self.extracted_figures:
            card = FigureCard(fig, self.json_base_dir)
            card.clicked.connect(self.open_zoom_view)
            self.gallery_grid.addWidget(card, row, col)

            col += 1
            if col > 3: # 4 columns wide
                col = 0
                row += 1

        # Add empty spacer at bottom of layout to prevent spacing issues
        self.gallery_grid.setRowStretch(row + 1, 1)

    def open_zoom_view(self, fig):
        # Launch beautiful dialog
        dialog = ZoomDialog(fig, self.json_base_dir, self)
        dialog.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Configure desktop integration for Linux/GNOME Dock
    app.setApplicationName("PDFFigures2")
    app.setApplicationDisplayName("PDFFigures 2.0")
    app.setDesktopFileName("PDFFigures2")
    
    # Set App-wide Icon
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon_v3.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QtGui.QIcon(icon_path))
    
    window = PDFFiguresGUI()
    window.show()
    
    # Self-screenshot helper to capture high-quality app visual under Wayland/X11
    if "--screenshot" in sys.argv:
        def capture_self():
            # Grab window pixmap and save
            pixmap = window.grab()
            output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshot.png")
            pixmap.save(output_path, "PNG")
            print(f"App screenshot saved successfully to {output_path}")
            sys.exit(0)
            
        QtCore.QTimer.singleShot(2500, capture_self)
        
    sys.exit(app.exec())
