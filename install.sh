#!/bin/bash

echo "🛠️ Menginstal dependencies..."
pkg update -y
pkg install python -y
pip install requests colorama

echo "✅ Instalasi selesai. Jalankan dengan: python cuaca.py"
