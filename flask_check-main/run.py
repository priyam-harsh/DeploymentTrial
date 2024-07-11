import subprocess
if __name__ == "__main__":
    subprocess.call(
        [
            "gunicorn",
            "-b",
            "0.0.0.0:8080",
            "api:app",  #
            "--timeout",
            "600",
        ], 
        shell=False,
    )

