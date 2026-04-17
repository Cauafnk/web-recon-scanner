import requests
import argparse
import sys

def banner():
    print("""
==============================
   Web Recon Scanner v1.0
==============================
    """)

def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao acessar {url}: {e}")
        sys.exit(1)

def search_keywords(text, keywords, context):
    lines = text.splitlines()
    found = False

    for i, line in enumerate(lines):
        for keyword in keywords:
            if keyword.lower() in line.lower():
                found = True
                print("\n[+] KEYWORD ENCONTRADA\n")

                start = max(0, i - context)
                end = min(len(lines), i + context)

                for j in range(start, end):
                    highlighted = lines[j]
                    for k in keywords:
                        highlighted = highlighted.replace(k, f">>>{k}<<<")
                    print(f"[Linha {j}] {highlighted}")

                print("\n" + "-"*40)

    if not found:
        print("\n[-] Nenhuma palavra encontrada.\n")

def main():
    parser = argparse.ArgumentParser(description="Web Recon Content Scanner")
    parser.add_argument("-u", "--url", required=True, help="URL alvo")
    parser.add_argument("-k", "--keywords", required=True, help="Palavras-chave (separadas por vírgula)")
    parser.add_argument("-c", "--context", type=int, default=5, help="Linhas de contexto (default: 5)")

    args = parser.parse_args()

    banner()

    keywords = [k.strip() for k in args.keywords.split(",")]

    print(f"[INFO] Alvo: {args.url}")
    print(f"[INFO] Keywords: {keywords}\n")

    content = fetch_url(args.url)
    search_keywords(content, keywords, args.context)

if __name__ == "__main__":
    main()
