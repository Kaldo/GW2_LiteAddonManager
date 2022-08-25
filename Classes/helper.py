import os
import sys
import shutil
import requests
from tqdm.auto import tqdm
from rich.console import Console, detect_legacy_windows
import platform
system = platform.system()
if system == 'Windows':
    from ctypes import windll, wintypes

def download_file(url, path, enable_progress_bar = True):
    with requests.get(url, stream=True) as r:
        if enable_progress_bar is True and 'Content-Length' in r.headers:
            total_size = int(r.headers.get('Content-Length'))
            with tqdm.wrapattr(r.raw, "read", total=total_size, desc="") as raw:
                # save the output to a file
                # path = f"{os.path.basename(r.url)}"
                with open(path, 'wb') as output:
                    shutil.copyfileobj(raw, output)
        else:
            with open(path, 'wb') as download:
                download.write(r.content)

        # with open(full_path, 'wb') as download:
            # chunk_size = 1
            # for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
            #     p = i * chunk_size / total_size * 100
            #     sys.stdout.write(f"\r{round(c, 4)}%")
            #     time.sleep(.1)
            #     sys.stdout.flush()


    # with requests.get(url) as r:
    #     with open(full_path, 'wb') as download:
    #         download.write(r.content)

    return True

def get_github_latest_release_info(github_id):
    api_url = "https://api.github.com/repos/% s/releases/latest" % (github_id)
    with requests.get(api_url) as r:
        if r.status_code == 200:
            json_data = r.json()
            return {
                'version': json_data['tag_name'],
                'file_name': json_data['assets'][0]['name']
            }
    return None

def get_github_version(github_id):
    api_url = "https://api.github.com/repos/% s/releases/latest" % (github_id)
    with requests.get(api_url) as r:
        if r.status_code == 200:
            json_data = r.json()
            if 'tag_name' in json_data:
                return json_data['tag_name']
    return None

def clear_screen():
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def set_terminal_title(title):
    if system == 'Windows':
        os.system(f'title {title}')
    else:
        os.system(f'echo "\033]0;{title}\007"')


def set_terminal_size(w, h):
    if system == 'Windows':
        os.system(f'mode con: cols={w} lines={h}')
    else:
        os.system(f'printf \'\033[8;{h};{w}t\'')

def tag_text(text, tag):
    return "[% s]%s[/% s]" % (tag, text, tag)

def setup_console():    
    # if self.headless:
    #     self.console = Console(record=True)
    #     if self.os == 'Windows':
    #         window = windll.kernel32.GetConsoleWindow()
    #         if window:
    #             windll.user32.ShowWindow(window, 0)
    # elif
    if detect_legacy_windows():
        set_terminal_size(80, 100)
        set_terminal_title("GW2 KLAM v0.1")
        windll.kernel32.SetConsoleScreenBufferSize(windll.kernel32.GetStdHandle(-11), wintypes._COORD(100, 200))
        return Console(width=97)
    else:
        return Console()