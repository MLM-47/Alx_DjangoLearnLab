#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#CREATE
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output: <Book: 1984 by George Orwell (1949)>

#RETRIEVE
Book.objects.all()
# Expected Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output: ('1984', 'George Orwell', 1949)

#UPDATE
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

#DELETE
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected Output: (1, {'bookshelf.Book': 1})

Book.objects.all()
# Expected Output: <QuerySet []>