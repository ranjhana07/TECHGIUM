#!/usr/bin/env python3
"""
InfraSense Dashboard Launcher
Quick start script for the real-time sensor dashboard
"""

import os
import sys
import subprocess
import time
import importlib
import socket

def check_requirements():
    """Check if required packages are installed (robust module mapping)."""
    # Map pip package name -> importable module name
    pkg_to_module = {
        'dash': 'dash',
        'plotly': 'plotly',
        'paho-mqtt': 'paho.mqtt',  # paho-mqtt installs module 'paho.mqtt'
        'python-dotenv': 'dotenv',  # python-dotenv installs module 'dotenv'
        'dash-bootstrap-components': 'dash_bootstrap_components',
    }

    missing_packages = []
    for pkg, module in pkg_to_module.items():
        try:
            importlib.import_module(module)
        except Exception:
            missing_packages.append(pkg)

    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install missing packages with:")
        print("pip install " + " ".join(missing_packages))
        return False

    return True

def check_env_file():
    """Check if .env file exists and has required variables"""
    env_file = '.env'
    
    if not os.path.exists(env_file):
        print(f"❌ Environment file '{env_file}' not found")
        print("📝 Create a .env file with your MQTT broker settings")
        return False
    
    required_vars = ['MQTT_HOST', 'MQTT_PORT', 'MQTT_USERNAME', 'MQTT_PASSWORD']
    missing_vars = []
    
    with open(env_file, 'r') as f:
        content = f.read()
        for var in required_vars:
            if var not in content:
                missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        return False
    
    return True

def main():
    print("�️  INFRA SENSE DASHBOARD LAUNCHER")
    print("=" * 50)
    
    # Check requirements
    print("🔍 Checking requirements...")
    if not check_requirements():
        sys.exit(1)
    
    # Check environment file
    print("📄 Checking environment configuration...")
    if not check_env_file():
        sys.exit(1)
    
    print("✅ All checks passed!")
    # Choose a port: prefer DASH_PORT/PORT env, else 8050. If busy, pick next free.
    def find_free_port(start_port: int) -> int:
        port = start_port
        while port < start_port + 50:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    s.bind(("127.0.0.1", port))
                    return port
                except OSError:
                    port += 1
        return start_port

    preferred = os.getenv('DASH_PORT') or os.getenv('PORT') or '8050'
    try:
        preferred_port = int(preferred)
    except Exception:
        preferred_port = 8050

    chosen_port = find_free_port(preferred_port)
    os.environ['DASH_PORT'] = str(chosen_port)

    print("\n🚀 Starting InfraSense Dashboard...")
    print(f"📊 Dashboard URL: http://localhost:{chosen_port}")
    print("🔄 Real-time updates every second")
    print("🛑 Press Ctrl+C to stop the dashboard\n")
    
    try:
        # Start the dashboard with env containing chosen port
        env = os.environ.copy()
        subprocess.run([sys.executable, 'mine_armour_dashboard.py'], env=env)
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped by user")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")

if __name__ == "__main__":
    main()
