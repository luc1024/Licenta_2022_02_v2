## Requirements
This project needs Microsoft Word in order to convert DOC files to PDF.

If the Word application is not present on the host machine, the output will consist of ZIPs of DOC files instead of PDFs.
## How to run the project with fake data
```bash
git clone https://github.com/luc1024/Licenta_2022_02_v2.git
cd Licenta_2022_02_v2
pip install -r requirements.txt
cp fake_items.json secret/items.json
cp .env-example .env
```
Then set **GET_FROM_LOCAL_FILE = TRUE** in .env

Run it with
```bash
python main.py
```

That's all.