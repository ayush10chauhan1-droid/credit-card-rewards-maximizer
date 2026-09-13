#!/usr/bin/env python3
"""
=====================================================================
💳 SwipeSmart AI — Universal One-Click Launcher
=====================================================================
This script automatically sets up and runs both the FastAPI backend
and the React + Vite frontend with zero configuration needed.

Usage:
    python3 run.py            # Standard launch (both servers + open browser)
    python3 run.py --no-browser
    python3 run.py --install-only
=====================================================================
"""

import os
import sys
import shutil
import signal
import socket
import time
import argparse
import subprocess
import webbrowser
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

ROOT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = ROOT_DIR / "backend"
FRONTEND_DIR = ROOT_DIR / "frontend"

def print_banner():
    banner = """
\033[1;36m=====================================================================\033[0m
\033[1;32m  💳  SWIPESMART AI (ENTERPRISE EDITION)  —  LAUNCHER               \033[0m
\033[1;36m=====================================================================\033[0m
"""
    print(banner)

def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    """Check if a TCP port is currently listening."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        return s.connect_ex((host, port)) == 0

def check_python_version():
    """Verify minimum Python version."""
    if sys.version_info < (3, 10):
        print(f"\033[1;31m[ERROR] Python 3.10 or higher is required. You are using {sys.version.split()[0]}.\033[0m")
        print("Please download an updated Python version from https://www.python.org/downloads/")
        sys.exit(1)
    print(f"\033[1;32m✓\033[0m Python {sys.version.split()[0]} detected.")

def check_node():
    """Verify Node.js and npm are installed."""
    node_path = shutil.which("node")
    npm_path = shutil.which("npm") or shutil.which("npm.cmd")

    if not node_path or not npm_path:
        print("\n\033[1;31m[ERROR] Node.js and npm are required to run the frontend, but were not found in PATH.\033[0m")
        print("\033[1;33mPlease install Node.js (LTS recommended) from:\033[0m")
        print("  👉 https://nodejs.org/\n")
        print("After installation completes, restart your terminal and run this script again.\n")
        sys.exit(1)

    # Get node version
    try:
        node_ver = subprocess.check_output([node_path, "-v"], text=True).strip()
        print(f"\033[1;32m✓\033[0m Node.js {node_ver} detected ({node_path}).")
    except Exception:
        print(f"\033[1;32m✓\033[0m Node.js detected.")

    return node_path, npm_path

def ensure_env_file():
    """Copy .env.example to .env if .env is missing."""
    env_file = ROOT_DIR / ".env"
    env_example = ROOT_DIR / ".env.example"

    if not env_file.exists() and env_example.exists():
        shutil.copyfile(env_example, env_file)
        print("\033[1;32m✓\033[0m Created .env file from .env.example template.")
    elif env_file.exists():
        print("\033[1;32m✓\033[0m Environment file (.env) found.")

def check_and_install_python_deps():
    """Ensure backend requirements are installed."""
    print("\n\033[1;34m[1/2] Checking Python backend dependencies...\033[0m")
    
    missing = False
    for pkg in ["fastapi", "uvicorn", "pydantic", "dotenv"]:
        try:
            __import__(pkg)
        except ImportError:
            missing = True
            break

    req_file = BACKEND_DIR / "requirements.txt"
    if missing and req_file.exists():
        print("📦 Installing required Python packages from backend/requirements.txt...")
        cmd = [sys.executable, "-m", "pip", "install", "-r", str(req_file)]
        subprocess.check_call(cmd)
        print("\033[1;32m✓\033[0m Python backend dependencies installed successfully.")
    else:
        print("\033[1;32m✓\033[0m Python backend dependencies are ready.")

def check_and_install_node_deps(npm_path: str):
    """Ensure frontend node_modules are installed."""
    print("\n\033[1;34m[2/2] Checking React frontend dependencies...\033[0m")
    node_modules = FRONTEND_DIR / "node_modules"

    if not node_modules.exists():
        print("📦 'node_modules' folder not found. Running 'npm install' inside frontend/...")
        subprocess.check_call([npm_path, "install"], cwd=str(FRONTEND_DIR))
        print("\033[1;32m✓\033[0m Frontend dependencies installed successfully.")
    else:
        print("\033[1;32m✓\033[0m Frontend node_modules are ready.")

def wait_for_url(url: str, timeout: float = 12.0) -> bool:
    """Wait until an HTTP endpoint is responsive."""
    start_time = time.time()
    req = Request(url, headers={"User-Agent": "SwipeSmart-Launcher"})
    while time.time() - start_time < timeout:
        try:
            with urlopen(req, timeout=1.0) as resp:
                if resp.status in (200, 304):
                    return True
        except (URLError, Exception):
            time.sleep(0.4)
    return False

def main():
    parser = argparse.ArgumentParser(description="SwipeSmart AI One-Click Universal Launcher")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")
    parser.add_argument("--install-only", action="store_true", help="Only install dependencies and exit")
    parser.add_argument("--backend-only", action="store_true", help="Only start the FastAPI backend")
    parser.add_argument("--frontend-only", action="store_true", help="Only start the React frontend")
    args = parser.parse_args()

    print_banner()
    check_python_version()
    node_path, npm_path = check_node()
    ensure_env_file()

    check_and_install_python_deps()
    check_and_install_node_deps(npm_path)

    if args.install_only:
        print("\n\033[1;32m✨ All dependencies installed successfully. Exiting (--install-only).\033[0m")
        return

    # Check for port conflicts
    if not args.frontend_only and is_port_in_use(8000):
        print("\n\033[1;33m⚠️  Warning: Port 8000 is already in use by another process.\033[0m")
        print("   If a previous backend instance is running, you can stop it or run `kill -9 $(lsof -ti:8000)`.")

    if not args.backend_only and is_port_in_use(5173):
        print("\n\033[1;33m⚠️  Warning: Port 5173 is in use. Vite may choose another port (e.g. 5174).\033[0m")

    processes = []

    def cleanup(sig=None, frame=None):
        print("\n\n\033[1;33m🛑 Stopping SwipeSmart AI servers...\033[0m")
        for p in processes:
            if p.poll() is None:
                p.terminate()
        for p in processes:
            try:
                p.wait(timeout=3.0)
            except Exception:
                p.kill()
        print("\033[1;32m✓ All servers stopped cleanly. Have a great day!\033[0m")
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    print("\n\033[1;36m=====================================================================\033[0m")
    print("\033[1;32m🚀 Starting SwipeSmart AI Servers...\033[0m")

    # Start backend
    if not args.frontend_only:
        print("  • Starting FastAPI Backend on http://localhost:8000...")
        backend_cmd = [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8000"]
        backend_proc = subprocess.Popen(backend_cmd, cwd=str(BACKEND_DIR))
        processes.append(backend_proc)

    # Start frontend
    if not args.backend_only:
        print("  • Starting React + Vite Frontend on http://localhost:5173...")
        frontend_cmd = [npm_path, "run", "dev"]
        frontend_proc = subprocess.Popen(frontend_cmd, cwd=str(FRONTEND_DIR))
        processes.append(frontend_proc)

    print("\033[1;36m=====================================================================\033[0m")

    # Wait for servers and open browser
    if not args.backend_only:
        print("\n⏳ Waiting for frontend to be ready...")
        if wait_for_url("http://localhost:5173", timeout=10.0):
            print("\033[1;32m✓ Frontend is ready at http://localhost:5173\033[0m")
            if not args.no_browser:
                print("🌐 Opening http://localhost:5173 in your default browser...")
                try:
                    webbrowser.open("http://localhost:5173")
                except Exception:
                    pass
        else:
            print("\033[1;33mFrontend started. Navigate to http://localhost:5173 in your browser.\033[0m")

    print("\n\033[1;32m✨ SwipeSmart AI is up and running!\033[0m")
    print("   👉 Frontend: \033[4;34mhttp://localhost:5173\033[0m")
    print("   👉 Backend:  \033[4;34mhttp://localhost:8000\033[0m")
    print("   👉 API Docs: \033[4;34mhttp://localhost:8000/docs\033[0m")
    print("\n\033[1;30m(Press Ctrl+C anytime in this window to stop both servers cleanly)\033[0m\n")

    try:
        while True:
            for p in processes:
                if p.poll() is not None:
                    print(f"\n\033[1;31m[Notice] A server process exited with code {p.returncode}.\033[0m")
                    cleanup()
            time.sleep(1.0)
    except KeyboardInterrupt:
        cleanup()

if __name__ == "__main__":
    main()
