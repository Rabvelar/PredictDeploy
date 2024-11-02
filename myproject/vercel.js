"routes": [
  {
    "src": "/api/(.*)",
    "dest": "myproject/wsgi.py"
  },
  {
    "src": "/(.*)",
    "dest": "myproject/wsgi.py"
  }
]
