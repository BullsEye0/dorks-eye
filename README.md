# Dorks Eye v2.0
**Google Hacking Dork Scraping and Searching Script - Now with 5 Search Engines**

Dorks Eye is a script I made in Python 3. With this tool, you can easily find Google Dorks. Dorks Eye collects potentially vulnerable web pages and applications on the Internet or other interesting info that search engines pick up.

## Why this major update v2.0?

Google doesn't like automated searches anymore. They started blocking them more aggressively. That's annoying.

So I added 4 more search engines:

* **DuckDuckGo** - Reliable, privacy-focused
* **Bing** - Fast and reliable  
* **Google** - Still there (Often blocked due to bot detection (YMMV)
* **Brave Search** - Privacy-focused, independent
* **Yandex** - Different results, reliable

Yes, it's called "Google Dorking" but dorks work on any search engine. When Google blocks you, switch engines. Keep searching. Simple as that.

****

Here you can read the article about Dorks Eye:

https://hackingpassion.com/dorks-eye-google-hacking-dork-scraping-and-searching-script/

**New article about v2.0 coming soon on HackingPassion.com**

****

![Screenshot](Img/dork-eye-banner.png)
***

You can save the output in a file. You decide how many results you want.

Dorks Eye shows only the links, no ads, and it's fast.

But be careful. Too many requests in a short time = captchas or IP blocks. That's why having 5 engines helps.

****

# What data can we find using Dorks?

* Username and passwords
* Admin login pages
* Sensitive documents
* Govt/military data
* Email lists
* Bank account details
* Vulnerable websites
* So much more …

****

![Screenshot](Img/dorks-eye.png)
****

## Install Dorks Eye

A prerequisite for scripts I make is that they must be simple and easy to use for everyone.

Dorks Eye has been tested on:
* Kali Linux
* Parrot Security OS
* BlackArch
* Termux

This list will be expanded.

****

Dorks Eye is written for Python 3. Clone the git repository and install the requirements.

****

# Installing Dorks Eye in a Virtual Environment

Recent changes in Parrot OS and Kali Linux require Dorks Eye to be installed in an isolated Python environment to avoid dependency conflicts. Follow these steps:

## Installation Steps:

1. **Clone the repository:**
```bash
git clone https://github.com/BullsEye0/dorks-eye.git
cd dorks-eye
```

2. **Create a virtual environment (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip3 install -r requirements.txt
```

****

# How to use Dorks Eye

```bash
python3 dorks-eye.py
```

You'll be asked to choose your search engine (1-6), or select option 6 to search ALL engines at once.

To deactivate the virtual environment when done:
```bash
deactivate
```

That's all!  
Have fun 😃

****

# Termux

```bash
git clone https://github.com/BullsEye0/dorks-eye.git
cd dorks-eye
pip install -r requirements.txt
```

# Usage Termux

```bash
python dorks-eye.py
```

****

![Screenshot](Img/vb2.png)
****

## A collection of Dorks:

13,760 dorks that work across all search engines. Updated regularly.

* https://github.com/BullsEye0/google_dork_list

****

![Screenshot](Img/banner_dork-list.png)
****

## Video Dorks Eye on YouTube:

New video coming soon showing v2.0 with all 5 search engines!

****

# Contact

Social Networks - Connect

* Website: [HackingPassion.com](https://hackingpassion.com)
* [Facebook Personal](https://www.facebook.com/profile.php?id=100069546190609)
* [LinkedIn](https://www.linkedin.com/in/jolandadekoff/)
* [YouTube](https://www.youtube.com/@HackingPassion)
* [Facebook Page](https://www.facebook.com/ethical.hack.group)
* [Facebook Group](https://www.facebook.com/groups/ethical.hack.group/)

***

## 💻 Support this project

If you find this tool useful, consider supporting my work:  
[❤️ Sponsor BullsEye](https://github.com/sponsors/BullsEye0)

**Want to learn ethical hacking from scratch?**

Want to master ethical hacking from zero to expert?
Check out my complete ethical hacking course:

**[Ethical Hacking Complete Course – Zero to Expert](https://www.udemy.com/course/ethical-hacking-complete-course-zero-to-expert/?couponCode=FEBRUARY26)**  
(This link supports me directly as your instructor)

HACKING IS NOT A HOBBY, BUT A WAY OF LIFE 🎯

***

## Donate

I developed Dorks Eye because I'm passionate about this. Donations are one of the many ways to support what I do.

[Donate](https://hackingpassion.com/donate/)

BAT: Use [Brave](https://brave.com/bul891) and donate on any of my web pages/profiles

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=R96YN2PUS8V8W)
