import random

# ==========================================
# إعدادات المولد
# ==========================================
filename = "passwords.txt"
correct_password = "admin"
total_lines = 2000
# أين تريد وضع كلمة السر الصحيحة؟ (اجعلها رقم 15 عشان الديمو يخلص بسرعة)
winning_index = 15

# ==========================================
# التنفيذ
# ==========================================
print(f"[*] جاري إنشاء ملف {filename} يحتوي على {total_lines} كلمة...")

common_words = ["password", "hello", "dragon", "master", "football", "system", "access"]

with open(filename, "w") as f:
    for i in range(total_lines):
        # إذا وصلنا للسطر المحدد، نكتب كلمة السر الصحيحة
        if i == winning_index:
            f.write(correct_password + "\n")
            print(f"[+] تم زرع كلمة '{correct_password}' في السطر رقم {i+1}")
        else:
            # توليد كلمات عشوائية لملء الملف
            # مثال: password8372, dragon1029
            base = random.choice(common_words)
            number = random.randint(1000, 9999)
            fake_pass = f"{base}{number}"
            f.write(fake_pass + "\n")

print("-" * 40)
print(f"[OK] الملف جاهز! يمكنك الآن تشغيل أداة الهجوم.")