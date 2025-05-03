# 🧼 FairTask

公平で柔軟な掃除当番管理アプリ。  
タスクの労力をポイント化して、真の公平性を実現！

---

## 🔧 セットアップ手順（開発者向け）

```bash
# リポジトリをクローンして移動
git clone https://github.com/arataka1313/FairTask.git
cd FairTask

# 仮想環境を作成して起動（WSL or Windows）
python3 -m venv venv
source venv/bin/activate  # Windowsなら venv\Scripts\activate

# ライブラリをインストール
pip install -r requirements.txt

# アプリを起動
streamlit run app.py
