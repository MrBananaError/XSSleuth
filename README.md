
# <img src="https://user-images.githubusercontent.com/74038190/213866269-5d00981c-7c98-46d7-8a8e-16f462f15227.gif" width="100" /> XSSleuth
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">
  <br>
**XSSleuth** is a powerful and automated tool designed to help security researchers and penetration testers identify **Cross-Site Scripting (XSS)** vulnerabilities in web applications.  
This tool includes **151 XSS payloads** that it automatically tests against input fields in target URLs.
Python XSS scanner

## 🔍 Features

- Automatically scans the target URL for XSS vulnerabilities by submitting 151 different payloads  
- Extracts and submits all forms found on the page to test injection points  
- Displays colorful and clear output with ASCII banners for better readability  
- **Allows you to easily add your own custom payloads** by modifying the `XSS_PAYLOADS` list in the code, making it flexible to test new or targeted payloads  

## ⚙️ Python Libraries Used

This tool uses the following Python libraries:

| Library     | Description                                   | Requires Installation?  |
|-------------|-----------------------------------------------|-------------------------|
| `pyfiglet`  | For displaying ASCII art banners              | ✅ Yes                  |
| `colorama`  | For colored terminal output                    | ✅ Yes                  |
| `urllib`    | For URL parsing and joining (built-in module) | ❌ No                   |
| `bs4`       | BeautifulSoup for parsing HTML                 | ✅ Yes                  |
| `requests`  | For sending HTTP requests                       | ✅ Yes                  |

### ✅ How to install required libraries

Run the following command to install all necessary libraries:

```bash
pip install pyfiglet colorama beautifulsoup4 requests
```

> Note: `urllib` is part of Python's standard library and does not require installation.

## 🛠️ Prerequisites

- Python 3 or higher  
- Internet connection (to test URLs)  

## 📦 How to run

Clone the repository and run the tool:

```bash
git clone https://github.com/MrBananaError/XSSleuth.git
cd XSSleuth
python3 xssleuth.py
```

Enter the target URL (make sure to include `http://` or `https://`) when prompted.

## ⚠️ Legal Disclaimer

This tool is intended for **educational purposes only** and should only be used on websites you have explicit permission to test.  
**Unauthorized use against websites you do not own or have permission to test is illegal and unethical.**

---

## 🤝 Contributing & Expanding XSSleuth

We’re excited about the possibility of you contributing to and expanding XSSleuth!  
If you have ideas for new features, find bugs, or want to add more payloads, feel free to open an issue or submit a pull request on GitHub.  
Your help in making this project better is highly appreciated! 💜

<div align="center">
  
  <img src="https://user-images.githubusercontent.com/74038190/212284094-e50ceae2-de86-4dd6-9f9c-a3ebcb3ede9e.gif" width="400">
</div>

---

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">
  <br>


# فارسی - معرفی XSSleuth

**XSSleuth** یک ابزار قدرتمند و خودکار است که به پژوهشگران امنیت و تست‌کنندگان نفوذ کمک می‌کند تا آسیب‌پذیری‌های **Cross-Site Scripting (XSS)** را در برنامه‌های وب شناسایی کنند.  
این ابزار شامل **۱۵۱ پیلود XSS** است که به صورت خودکار روی فیلدهای ورودی سایت‌های هدف تست می‌کند.



## 🔍 ویژگی‌ها

- اسکن خودکار URL هدف با ارسال ۱۵۱ پیلود مختلف  
- استخراج و ارسال تمام فرم‌های موجود در صفحه برای تست نقاط تزریق  
- نمایش خروجی رنگی و واضح با بنرهای ASCII برای خوانایی بهتر  
- **امکان افزودن پیلودهای دلخواه خود به راحتی** از طریق ویرایش لیست `XSS_PAYLOADS` در کد  

## ⚙️ کتابخانه‌های پایتون استفاده شده

این ابزار از کتابخانه‌های زیر استفاده می‌کند:

| کتابخانه   | توضیح                                           | نیاز به نصب؟            |
|------------|------------------------------------------------|-------------------------|
| `pyfiglet` | نمایش بنرهای ASCII                              | ✅ بله                  |
| `colorama` | رنگی کردن خروجی ترمینال                         | ✅ بله                  |
| `urllib`   | برای پردازش و ترکیب URL (کتابخانه داخلی پایتون) | ❌ خیر                  |
| `bs4`      | BeautifulSoup برای پردازش HTML                   | ✅ بله                  |
| `requests` | ارسال درخواست‌های HTTP                          | ✅ بله                  |

### ✅ نحوه نصب کتابخانه‌ها

دستور زیر را اجرا کنید تا همه کتابخانه‌های مورد نیاز نصب شوند:

```bash
pip install pyfiglet colorama beautifulsoup4 requests
```

> توجه: `urllib` جزو کتابخانه‌های استاندارد پایتون است و نیازی به نصب ندارد.

## 🛠️ پیش‌نیازها

- پایتون ۳ یا بالاتر  
- اتصال اینترنت (برای تست URLها)  

## 📦 نحوه اجرا

ریپازیتوری را کلون کرده و ابزار را اجرا کنید:

```bash
git clone https://github.com/MrBananaError/XSSleuth.git
cd XSSleuth
python3 xssleuth.py
```

وقتی از شما خواسته شد، URL هدف را وارد کنید (حتما `http://` یا `https://` را اضافه کنید).

## ⚠️ هشدار قانونی

این ابزار فقط برای **اهداف آموزشی** ساخته شده و باید فقط روی سایت‌هایی استفاده شود که اجازه تست دارید.  
**استفاده بدون اجازه از سایت‌های دیگر غیرقانونی و غیراخلاقی است.**

---

## 🤝 مشارکت و توسعه XSSleuth

ما بسیار خوشحال می‌شویم اگر شما در توسعه و گسترش XSSleuth مشارکت کنید!  
اگر ایده‌ای برای ویژگی‌های جدید دارید، باگ پیدا کردید، یا می‌خواهید پیلودهای بیشتری اضافه کنید، حتما در گیت‌هاب issue باز کنید یا Pull Request ارسال کنید.  
کمک شما در بهتر شدن این پروژه بسیار ارزشمند است! 💜

<div align="center">
  
  <img src="https://user-images.githubusercontent.com/74038190/212284094-e50ceae2-de86-4dd6-9f9c-a3ebcb3ede9e.gif" width="400">
</div>




<div align="center">
    <img src="https://cultofthepartyparrot.com/parrots/hd/githubparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/flags/hd/iranparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/asyncparrot.gif" width="36" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/60fpsparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/jumpingparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/opensourceparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/dealwithitnowparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/hypnoparrotlight.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/databaseparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/fixparrot.gif" width="36" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/laptop_parrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/spinningparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/levitationparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/meldparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/slomoparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/moonwalkingparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/stableparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/scienceparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/pirateparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/footballparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/illuminatiparrot.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/hypnoparrotdark.gif" width="25" height="25"/>
    <img src="https://cultofthepartyparrot.com/parrots/hd/mustacheparrot.gif" width="25" height="25"/>
</div>
<br><br>
 

<br><br>
