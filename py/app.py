import time

from flask import Flask

TIMEOUT = 5
app = Flask(__name__)

@app.route("/")
def ping():
    return "python - ping"

@app.route("/timeout")
def timeout():
  time.sleep(TIMEOUT)
  return "python - timeout"

@app.route("/heavy")
def heavy():
  start = time.time()
  now = time.time()
  while now - start <= 5:
    now = time.time()

  return "python - heavy"

if (__name__ == "__main__"):
  app.run()
