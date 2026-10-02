#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

# ===== #
#
# ▀█████████▄     ▄████████         Websites: HackingPassion.com | Bullseye0.com
#   ███    ███   ███    ███         Author: Jolanda de Koff | Bulls Eye
#   ███    ███   ███    █▀          GitHub: https://github.com/BullsEye0
#  ▄███▄▄▄██▀   ▄███▄▄▄             LinkedIn: https://www.linkedin.com/in/jolandadekoff
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀             Facebook Group: https://www.facebook.com/groups/hack.passion/
#   ███    ██▄   ███    █▄          Facebook Page: https://www.facebook.com/ethical.hack.group/
#   ███    ███   ███    ███         YouTube: https://www.youtube.com/@HackingPassion
# ▄█████████▀    ██████████         LBRY: https://lbry.tv/$/invite/@hackingpassion:9
#                                   GitHub Sponsor: https://github.com/sponsors/BullsEye0
#          Bulls Eye..!
# ===== #

# ===== #
# Created April | Copyright (c) 2020 - 2026 Jolanda de Koff.
# Updated September 2026 - Multi Search Engine
# ===== #

########################################################################

# A notice to all nerds and n00bs...
# If you copy the developer's work, it will not make you a hacker..!
# Respect all developers, we're doing this because it's fun...

########################################################################


from __future__ import print_function
try:
    from ddgs import DDGS
except ImportError:
    print("\n[!] Error: ddgs is not installed!")
    print("[!] Install with: pip install ddgs\n")
    exit(1)

import sys
import time
import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib.parse


if sys.version_info.major < 3:
    print ("\n[x] ..n00b.. Dorks Eye Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tDorks Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""

    ▓█████▄  ▒█████   ██▀███   ██ ▄█▀  ██████    ▓█████▓██   ██▓▓█████
    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██    ▒    ▓█   ▀ ▒██  ██▒▓█   ▀
    ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ░ ▓██▄      ▒███    ▒██ ██░▒███
    ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄   ▒   ██▒   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄
    ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██████▒▒   ░▒████▒ ░ ██▒▓░░▒████▒
    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
    ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░    ░ ░  ░▓██ ░▒░  ░ ░  ░
    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░  ░  ░        ░   ▒ ▒ ░░     ░
    ░        ░ ░     ░     ░  ░         ░        ░  ░░ ░        ░  ░
    ░                                                  ░ ░  v3.0 """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  Jolanda de Koff | Bulls Eye
                Github:  https://github.com/BullsEye0
                Website: https://HackingPassion.com\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there, Shall we play a game..? 😃\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.1)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


def duckduckgo(dork, amount):
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(dork, max_results=amount):
                results.append(r['href'])
    except Exception as e:
        print(f"[!] DuckDuckGo: {str(e)}")
    return results


def bing(dork, amount):
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(dork, backend="bing", max_results=amount):
                results.append(r['href'])
    except Exception as e:
        print(f"[!] Bing: {str(e)}")
    return results


def google(dork):
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(dork)
    print("[~] Google blocks searches from scripts, so the search opens in your browser.")
    print(f"[+]  {url}")
    if not webbrowser.open_new_tab(url):
        print("[!] No browser found. Open the link above yourself.")
    return url


def brave(dork, amount):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate'
    }

    try:
        query = urllib.parse.quote_plus(dork)
        url = f"https://search.brave.com/search?q={query}"

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a')

        for link in links[:amount * 3]:
            href = link.get('href')
            if href and href.startswith('http') and 'brave.com' not in href:
                results.append(href)
                if len(results) >= amount:
                    break

    except Exception as e:
        print(f"[!] Brave: {str(e)}")

    return results


def yandex(dork, amount):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        query = urllib.parse.quote_plus(dork)
        url = f"https://yandex.com/search/?text={query}"

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', attrs={'class': 'Link'})

        for link in links[:amount]:
            href = link.get('href')
            if href and href.startswith('http') and 'yandex' not in href:
                results.append(href)

    except Exception as e:
        print(f"[!] Yandex: {str(e)}")

    return results


def search_engine(engine, dork, amount):
    if engine == "duckduckgo":
        return duckduckgo(dork, amount)
    elif engine == "bing":
        return bing(dork, amount)
    elif engine == "brave":
        return brave(dork, amount)
    elif engine == "yandex":
        return yandex(dork, amount)
    else:
        return []


def _ask_engine_and_logfile():
    """Ask for search engine and logfile. Returns (engine_choice, save_output, logfile)."""
    print ("\n" + "  " + "»" * 78 + "\n")
    print ("[~] Choose Your Search Engine:\n")
    print ("[1] DuckDuckGo - Reliable, privacy-focused")
    print ("[2] Bing - Reliable, fast results")
    print ("[3] Google - Opens in your browser")
    print ("[4] Brave Search - Privacy-focused, independent index")
    print ("[5] Yandex - Reliable, different results")
    print ("[6] ALL")

    engine_choice = input("\n[+] Select Option (1-6): ").strip()

    data = input("[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")
    if data.lower().startswith("y"):
        l0g = input("[~] Give The File a Name: ")
    else:
        print ("[!] Saving is Skipped...")
        print ("\n" + "  " + "»" * 78 + "\n")
    return engine_choice, data, l0g


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


def dorks():
    global l0g
    try:
        engine_choice, data, l0g = _ask_engine_and_logfile()
        dork = input("\n[+] Enter The Dork Search Query: ")
        amount = int(input("[+] Enter The Number Of Websites To Display: "))
        print ("\n ")

        engines = []
        if engine_choice == "1":
            engines = [("DuckDuckGo", "duckduckgo")]
        elif engine_choice == "2":
            engines = [("Bing", "bing")]
        elif engine_choice == "3":
            engines = [("Google", "google")]
        elif engine_choice == "4":
            engines = [("Brave Search", "brave")]
        elif engine_choice == "5":
            engines = [("Yandex", "yandex")]
        elif engine_choice == "6":
            engines = [("DuckDuckGo", "duckduckgo"), ("Bing", "bing"), ("Google", "google"), ("Brave Search", "brave"), ("Yandex", "yandex")]
        else:
            print("[!] Invalid choice, using DuckDuckGo...")
            engines = [("DuckDuckGo", "duckduckgo")]

        counter = 0

        for engine_name, engine_type in engines:
            print(f"\n[•] Searching {engine_name}...\n")

            if engine_type == "google":
                url = google(dork)
                if data.lower().startswith("y"):
                    logger(f"Google: {url}")
                if len(engines) > 1:
                    time.sleep(2)
                continue

            results = search_engine(engine_type, dork, amount)

            if results:
                for result in results:
                    counter += 1
                    print(f"[+]  {counter} {result}")

                    if data.lower().startswith("y"):
                        logger(f"{counter} {result}")

                    time.sleep(0.1)
            else:
                print(f"[!] No results from {engine_name}")

            if len(engines) > 1:
                time.sleep(2)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)
    except ValueError:
        print("[!] Please enter a valid number!")
        sys.exit(1)

    print ("\n[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mDorks Eye\033[0m")
    print ("\t\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
    sys.exit()


if __name__ == "__main__":
    dorks()
