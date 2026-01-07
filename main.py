import os
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin, urlparse

BASE_URL = "https://docs.polymarket.com/"
OUTPUT_DIR = "polymarket_docs"
START_URL = BASE_URL

# Создаём папку
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Сет посещенных и ссылок для обхода
visited = set()
to_visit = [START_URL]

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; DocsDownloader/1.0)"
}

h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.body_width = 0  # Не обрезать строки

while to_visit:
    url = to_visit.pop(0)
    if url in visited:
        continue
    print(f"Скачиваю: {url}")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")
        continue
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Конвертируем в Markdown
    md_content = h.handle(response.text)
    
    # Формируем путь файла
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if path == "":
        filename = "index.md"
    elif path.endswith("/"):
        filename = os.path.join(path, "index.md")
    else:
        filename = path.replace("/", os.path.sep) + ".md"
    
    full_path = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"# {soup.title.string if soup.title else 'Polymarket Docs'}\n\n")
        f.write(f"Source: {url}\n\n")
        f.write(md_content)
    
    print(f"Сохранено: {full_path}")
    
    # Ищем внутренние ссылки в навигации/сайдбаре
    for a in soup.find_all('a', href=True):
        href = a['href']
        full_link = urljoin(url, href)
        parsed_link = urlparse(full_link)
        
        # Только внутренние ссылки в домене docs.polymarket.com, без # и файлов
        if (parsed_link.netloc == urlparse(BASE_URL).netloc and
            parsed_link.path.startswith("/")):
            if not full_link.endswith(('.pdf', '.jpg', '.png')) and '#' not in full_link:
                normalized = full_link.rstrip("/") + "/"
                if normalized not in visited and normalized not in to_visit:
                    to_visit.append(full_link)
    
    visited.add(url)

print("Готово! Все страницы сохранены в папке", OUTPUT_DIR)