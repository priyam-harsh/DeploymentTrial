import subprocess
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)
if __name__ == "__main__":
    subprocess.call(
        [
            "gunicorn",
            "-b",
            "0.0.0.0:8080",
            "api:app",  # This assumes the file is named run.py
            "--timeout",
            "600",
        ], 
        shell=False,
    )

