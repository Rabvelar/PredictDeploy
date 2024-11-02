"routes": [
  {
    "src": "/static/(.*)",
    "dest": "/myproject/static/$1"
  },
  {
    "src": "/(.*)",
    "dest": "myproject/wsgi.py"
  }
]
