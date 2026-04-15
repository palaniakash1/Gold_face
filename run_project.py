#!/usr/bin/env python3
"""
Gold Face - Virtual Jewelry Try-On
Run this script to launch the project.
"""

import sys
import os


def show_menu():
    print("\n" + "=" * 50)
    print("  Gold Face - Virtual Jewelry Try-On")
    print("=" * 50)
    print("\nChoose an option:\n")
    print("  1. Run Webapp (Recommended - Browser-based)")
    print("     - Uses face-api.js for face detection")
    print("     - Works in any modern browser")
    print("     - No additional setup required\n")
    print("  2. Run Desktop App (Python/OpenCV)")
    print("     - Uses dlib for face detection")
    print("     - Requires webcam\n")
    print("  3. Run Both\n")
    print("  0. Exit\n")


def run_webapp():
    print("\nStarting Webapp...")
    print("-" * 40)
    os.chdir(os.path.join(os.path.dirname(__file__), "webapp"))
    import http.server
    import socketserver
    import webbrowser

    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print(f"Open http://localhost:{PORT}/index.html in your browser")
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        print("\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)


def run_desktop():
    print("\nStarting Desktop App...")
    print("-" * 40)
    os.chdir(os.path.join(os.path.dirname(__file__), "Gold_face"))

    print("\nChoose desktop version:")
    print("  1. Basic (single jewelry)")
    print("  2. Enhanced (cycles through 3 combinations)")

    choice = input("\nEnter choice (1/2): ").strip()

    if choice == "1":
        os.system("python main.py")
    elif choice == "2":
        os.system("python new_main.py")
    else:
        print("Invalid choice. Running enhanced version...")
        os.system("python new_main.py")


def run_both():
    import threading

    webapp_thread = threading.Thread(target=run_webapp)
    webapp_thread.daemon = True
    webapp_thread.start()

    input("\nWebapp started in browser. Press Enter to run desktop app...")
    run_desktop()


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ["1", "webapp", "web"]:
            run_webapp()
        elif arg in ["2", "desktop", "app"]:
            run_desktop()
        elif arg in ["3", "both"]:
            run_both()
        elif arg in ["-h", "--help", "help"]:
            show_menu()
        else:
            show_menu()
    else:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            run_webapp()
        elif choice == "2":
            run_desktop()
        elif choice == "3":
            run_both()
        elif choice in ["0", "exit", "q"]:
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
