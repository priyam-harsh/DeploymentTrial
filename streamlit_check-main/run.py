import subprocess

if __name__ == "__main__":
    subprocess.call(
        [
            "streamlit",
            "run",
            "api.py",
            "--server.port=8080",
            "--server.address=0.0.0.0"
        ],
        shell=False,
    )
