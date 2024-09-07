# -*- coding: utf-8 -*-

import os

os.system("pip install yt_dlp colorama")

import yt_dlp
from colorama import Fore, init
import requests
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("MP3 Downloader Tool")
os.system("cls")
init(autoreset=True)

def download_video(language):
    os.system("cls")

    if language == 1:
        url = input(f"{Fore.YELLOW}[~] Quel URL de la vidéo souhaites-tu télécharger ? : {Fore.RED}")
    else:
        url = input(f"{Fore.YELLOW}[~] What is the URL of the video you want to download? : {Fore.RED}")

    try:
        reponse = requests.get(url, timeout=5)
        if language == 1:
            print(f"{Fore.GREEN}[+] Requête sur {url} envoyée.")
            print(f"{Fore.YELLOW}[~] Vérification de la requête...")
        else:
            print(f"{Fore.GREEN}[+] Request sent to {url}.")
            print(f"{Fore.YELLOW}[~] Checking the request...")

        if reponse.status_code != 200:
            if language == 1:
                print(f"{Fore.RED}[-] Il y a eu un problème lors de la requête vers {url} : [{reponse.status_code}] = {reponse}")
            else:
                print(f"{Fore.RED}[-] There was an issue with the request to {url} : [{reponse.status_code}] = {reponse}")
            os.system("pause")
            exit()
        else:
            if language == 1:
                print(f'{Fore.GREEN}[+] Requête bonne ! Code : {reponse.status_code}')
            else:
                print(f'{Fore.GREEN}[+] Request successful! Code: {reponse.status_code}')
    except requests.Timeout:
        if language == 1:
            print(f"{Fore.RED}[-] La requête a pris trop de temps.")
            bypass = input(f"{Fore.YELLOW}[~] Veux-tu ignorer la vérification de la requête et continuer ? (oui/non) : {Fore.RED}").strip().lower()
            if bypass != 'oui':
                os.system("pause")
                exit()
        else:
            print(f"{Fore.RED}[-] The request took too long.")
            bypass = input(f"{Fore.YELLOW}[~] Do you want to bypass the request check and continue? (yes/no) : {Fore.RED}").strip().lower()
            if bypass != 'yes':
                os.system("pause")
                exit()
    except Exception as e:
        if language == 1:
            print(f"{Fore.RED}[-] Erreur lors de la requête vers {url} : {e}")
        else:
            print(f"{Fore.RED}[-] Error during the request to {url} : {e}")
        os.system("pause")
        exit()

    while True:
        if language == 1:
            output_dir = input(f"{Fore.YELLOW}[~] Où veux-tu enregistrer la vidéo ? (chemin complet) : {Fore.RED}")
        else:
            output_dir = input(f"{Fore.YELLOW}[~] Where do you want to save the video? (full path) : {Fore.RED}")
        if os.path.isdir(output_dir):
            break
        else:
            print("\033[F\033[K", end='')
            if language == 1:
                print(f"{Fore.RED}[-] Le chemin spécifié n'est pas un dossier valide. Veuillez réessayer.")
            else:
                print(f"{Fore.RED}[-] The specified path is not a valid directory. Please try again.")
            time.sleep(2)
            print("\033[F\033[K", end='')

    while True:
        if language == 1:
            output_filename = input(f"{Fore.YELLOW}[~] Quel nom de fichier veux-tu utiliser ? (sans extension) : {Fore.RED}")
        else:
            output_filename = input(f"{Fore.YELLOW}[~] What filename do you want to use? (without extension) : {Fore.RED}")
        if output_filename.strip() != "":
            break
        else:
            print("\033[F\033[K", end='')
            if language == 1:
                print(f"{Fore.RED}[-] Le nom de fichier ne peut pas être vide. Veuillez réessayer.")
            else:
                print(f"{Fore.RED}[-] The filename cannot be empty. Please try again.")
            time.sleep(2)
            print("\033[F\033[K", end='')

    ydl_opts = {
        'outtmpl': os.path.join(output_dir, f"{output_filename}.%(ext)s"),
        'format': 'bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if language == 1:
        print(f"{Fore.GREEN}[+] Téléchargement terminé. Fichier enregistré à l'emplacement : {os.path.join(output_dir, f'{output_filename}.mp4')}")
    else:
        print(f"{Fore.GREEN}[+] Download complete. File saved at: {os.path.join(output_dir, f'{output_filename}.mp4')}")

while True:
    os.system("cls")
    print(f"{Fore.YELLOW}[~] Choisissez votre langue / Choose your language :")
    print(f"1. 🇫🇷 (Français, French)")
    print(f"2. 🇺🇸 (English, Anglais)")

    try:
        lang_choice = int(input(f"{Fore.RED}Entrer 1 ou 2 / Enter 1 or 2: {Fore.RED}"))
        if lang_choice not in [1, 2]:
            raise ValueError
    except ValueError:
        continue

    download_video(lang_choice)

    if lang_choice == 1:
        retry = input(f"{Fore.YELLOW}[~] Veux-tu télécharger une autre vidéo ? (oui/non) : {Fore.RED}").strip().lower()
        if retry != 'oui':
            break
    else:
        retry = input(f"{Fore.YELLOW}[~] Do you want to download another video? (yes/no) : {Fore.RED}").strip().lower()
        if retry != 'yes':
            break

exit()
