# 📧 HTML Email Sender – Python-based, Template-Driven

This project is a customizable, Python-based HTML email sender that uses external templates for both the email content and its metadata. It allows users to send professional, responsive HTML emails via a specified SMTP server.

One of the key advantages of this solution is that the email content is stored in a separate `.html` file rather than being embedded directly in the Python script. This makes it easy to modify the visual appearance of the email—such as text, buttons, layout, or branding—without having to touch the code itself. Similarly, core email details like the subject line, sender, and recipient are defined in a dedicated `.json` file, allowing for fast and safe customization.


## 🚀 How It Works

When the script runs:
1. It loads the external HTML template.
2. Replaces predefined placeholders (e.g., `{{target_link}}`).
3. Sends the fully rendered HTML email through the configured SMTP connection.

This approach makes the tool well-suited for:
- Educational use
- Internal testing
- Corporate email simulations
- Light marketing automation


## 🔧 Customization

To make the system your own, you only need to modify:

- **The HTML template**  
  Customize text, branding, colors, buttons, etc.

- **The `template.json` file**  
  Define your own subject line, sender address, and recipient.

- **SMTP Configuration**  
  Managed in a secure `.env` file (not included in version control).

You don’t need to write or modify any Python code to use the system with your own content and email account.


## 🧩 Features

- 🔌 External HTML template support  
- 📄 JSON metadata input (from, to, subject)  
- 🔐 Environment-based SMTP configuration  
- 🔁 Placeholder support for dynamic content  
- ✅ Works with any SMTP-compatible provider  
- 🧰 Lightweight and dependency minimal (uses `smtplib`, `email`, and `dotenv`)


## 📂 Example File Structure

foxpost_mailer/
├── send_mail.py
├── template.html
├── template.json
├── .env
├── .gitignore
└── README.md

## 📥 Installation & Usage

1. Clone this repository  
2. Install dependencies: `pip install python-dotenv`  
3. Fill in `.env`, `template.html`, and `template.json`  
4. Run the script: `python send_mail.py`

## 📃 License

This project is provided as-is, without warranty. Use it responsibly and only for ethical or educational purposes.


## 🙋‍♂️ Need Help?

Feel free to open an issue or contribute with improvements.
