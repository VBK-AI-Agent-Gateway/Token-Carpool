import os, sys, threading, webbrowser, logging, socket, mimetypes
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import requests
from flask import Flask, request, Response, stream_with_context

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("proxy")

TARGET_URL = os.environ.get("PROXY_TARGET", "http://154.12.86.206:8888")
LOCAL_PORT = int(os.environ.get("PROXY_PORT", "8899"))

app = Flask(__name__)
session = requests.Session()
session.headers.clear()

def rewrite_html(html, target, local):
    return html.replace(target, local)

def proxy_request(path, method="GET", body=None, headers=None, stream=False):
    target = TARGET_URL.rstrip("/") + "/" + path.lstrip("/")
    hdrs = {k: v for k, v in (headers or {}).items()
            if k.lower() not in ("host", "content-length", "transfer-encoding", "accept-encoding")}
    hdrs.setdefault("User-Agent", "UniversalProxy/1.0")
    try:
        if stream and method == "GET":
            resp = session.request(method, target, headers=hdrs, stream=True, timeout=30)
        else:
            resp = session.request(method, target, headers=hdrs, data=body, stream=True, timeout=30)
    except Exception as e:
        logger.error("Proxy error: %s", e)
        return Response(f"Proxy error: {e}", status=502)

    excluded = ("content-encoding", "content-length", "transfer-encoding", "connection")
    resp_headers = {k: v for k, v in resp.headers.items() if k.lower() not in excluded}

    ct = (resp.headers.get("content-type") or "").lower()

    if "text/html" in ct:
        text = resp.text
        text = rewrite_html(text, TARGET_URL, f"http://127.0.0.1:{LOCAL_PORT}")
        return Response(text, status=resp.status_code, headers=resp_headers)
    elif stream and "text/event-stream" in ct:
        def generate():
            for chunk in resp.iter_content(chunk_size=4096):
                if chunk:
                    yield chunk
        return Response(stream_with_context(generate()),
                        status=resp.status_code, headers=resp_headers,
                        content_type="text/event-stream")
    else:
        data = resp.content
        return Response(data, status=resp.status_code, headers=resp_headers,
                        content_type=resp.headers.get("content-type"))

@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
def catch_all(path):
    return proxy_request(path, method=request.method, body=request.get_data(),
                         headers=dict(request.headers), stream=True)

def start_server():
    logger.info("启动反向代理: http://127.0.0.1:%d -> %s", LOCAL_PORT, TARGET_URL)
    app.run(host="127.0.0.1", port=LOCAL_PORT, debug=False, use_reloader=False)

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", LOCAL_PORT))
        sock.close()
    except OSError:
        logger.error("端口 %d 已被占用", LOCAL_PORT)
        sys.exit(1)

    t = threading.Thread(target=start_server, daemon=True)
    t.start()

    tray_thread = None
    try:
        from pystray import Icon, Menu, MenuItem
        from PIL import Image

        def open_ui(icon, item):
            webbrowser.open(f"http://127.0.0.1:{LOCAL_PORT}")

        def do_quit(icon, item):
            icon.stop()
            os._exit(0)

        img = Image.new("RGB", (64, 64), (0, 120, 212))
        data = [0, 120, 212] * (64 * 64)
        try:
            icon_path = Path(getattr(sys, "_MEIPASS", Path(__file__).parent)) / "icon.png"
            if icon_path.exists():
                img = Image.open(icon_path)
        except Exception:
            pass

        menu = Menu(
            MenuItem("打开管理界面", open_ui, default=True),
            Menu.SEPARATOR,
            MenuItem("退出", do_quit),
        )
        tray = Icon("UniversalProxy", img, "Universal Proxy", menu)

        def run_tray():
            tray.run()

        tray_thread = threading.Thread(target=run_tray, daemon=True)
        tray_thread.start()
        logger.info("系统托盘已启动")
    except ImportError:
        logger.warning("pystray 未安装，跳过系统托盘")
        webbrowser.open(f"http://127.0.0.1:{LOCAL_PORT}")

    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("用户中断")
        os._exit(0)

if __name__ == "__main__":
    main()