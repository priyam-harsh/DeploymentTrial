# import subprocess
# if __name__ == "__main__":
#     subprocess.call(
#         [
#             "gunicorn",
#             "-b",
#             "0.0.0.0:8080",
#             "api:app",  #
#             "--timeout",
#             "600",
#         ], 
#         shell=False,
#     )

import subprocess
if __name__ == "__main__":
    subprocess.call(
        [
            "gunicorn",
            "-b",
            "0.0.0.0:8080",
            "--certfile",
            "selfsigned.pem",
            "--keyfile",
            "selfsigned.key",
            "api:app",
            "--timeout",
            "600",
        ],
        shell=False,
    )
