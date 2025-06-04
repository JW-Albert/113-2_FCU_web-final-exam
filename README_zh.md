# 逢甲大學商品販賣部

這是一個基於 Django 框架開發的逢甲大學商品販賣部網站。

## 功能特點

- 用戶認證（登入/登出）
- 商品列表展示（包含圖片和詳細描述）
- 購物車功能
- 結帳系統
- 購買歷史記錄
- 使用 Bootstrap 實現響應式設計

## 技術架構

- Python 3.x
- Django
- SQLite（資料庫）
- Bootstrap 5（前端框架）
- Pillow（圖片處理）

## 安裝說明

1. 複製專案：
```bash
git clone https://github.com/JW-Albert/113-2_FCU_web-final-exam.git
cd 113-2_FCU_web-final-exam
```

2. 建立並啟動虛擬環境：
```bash
python -m venv .venv
# Windows 系統
.venv\Scripts\activate
# Unix 或 MacOS 系統
source .venv/bin/activate
```

3. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

4. 執行資料庫遷移：
```bash
python manage.py migrate
```

5. 建立管理員帳號：
```bash
python manage.py createsuperuser
```

6. 啟動開發伺服器：
```bash
python manage.py runserver
```

網站將在 `http://127.0.0.1:8000/` 運行

## 專案結構

```
fcu-shop/
├── fcu_shop/          # 主專案配置
├── shop/             # 主要應用程式
├── templates/        # HTML 模板
├── static/          # 靜態檔案（CSS、JS、圖片）
├── media/           # 用戶上傳的檔案
└── manage.py        # Django 管理腳本
```

## 使用說明

1. 訪問管理介面 `http://127.0.0.1:8000/admin` 管理商品
2. 在 `http://127.0.0.1:8000/product_list/` 瀏覽商品
3. 將商品加入購物車並進行結帳
4. 完成訂單後可查看購買歷史

## 管理員帳號

- 帳號：admin
- 密碼：123

## 開發者

- 逢甲大學資訊工程學系 王建葦

## 授權

本專案採用 MIT 授權條款 - 詳見 LICENSE 檔案 