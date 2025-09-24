# QR Code Generator for CV
This is my personal fun project that generates custom QR codes for my CV, using [Segno](https://github.com/heuer/segno) for QR generation and [Pillow](https://python-pillow.org/) for image processing.  
It includes two versions:
- **Plain QR code** (no logo)
- **QR code with logo embedded**

<img width="300" height="289" alt="QR code without logo" src="https://github.com/user-attachments/assets/38bb5e17-9a00-4a39-bd01-76548e1d7659" />
<img width="300" height="289" alt="QR code with logo" src="https://github.com/user-attachments/assets/ae1abbbd-ea9e-4245-affa-c6252667a7c0" />

---

## 💡 Motivation 
I've always been curious about how QR codes work. Of course, there are plenty of free platforms to generate one, but I wanted to build my own.  

The idea came after a job interview where the recruiter asked for my CV, and I didn’t have a printed copy with me.
A personal QR code felt like the perfect solution. Simple to use, easy to share, and a step toward using less paper. Plus, it makes my CV and portfolio feel more modern and interactive.  

I also saw this as a chance to practice creative coding with Python, experimenting with custom colors, error correction, and embedding a logo into the QR code.

--- 

## ✨ Features
- Generate QR code linking to my CV
- Custom colors (foreground, background, finder patterns)
- High error correction (`H`) to support logo placement
- Option to embed a logo at the center of the QR code

---

## 🛠 Requirements
- Python 3.8+
- [Segno](https://pypi.org/project/segno/)
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies:
```bash
pip install segno pillow
