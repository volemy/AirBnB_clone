#!/usr/bin/python3
"""This method creates a unique FileStorgae instance for AirBnB
application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
