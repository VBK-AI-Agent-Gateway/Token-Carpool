@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 安装依赖...
pip install -r requirements.txt
echo 构建 UniversalProxy.exe...
python build.py
echo 构建完成：dist\UniversalProxy.exe
pause