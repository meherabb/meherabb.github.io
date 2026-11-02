#!/usr/bin/env python3
"""Update the self-contained page's JPEG portrait or embedded PDF using only Python's standard library."""
import argparse
import base64
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--html', type=Path, default=Path(__file__).resolve().parent / 'index.html')
parser.add_argument('--photo', type=Path, help='Replacement JPEG photo')
parser.add_argument('--cv', type=Path, help='Replacement PDF CV')
args = parser.parse_args()
if not args.photo and not args.cv:
    parser.error('Provide --photo and/or --cv.')
text = args.html.read_text(encoding='utf-8')
if args.photo:
    data = args.photo.read_bytes()
    if not data.startswith(b'\xff\xd8\xff'):
        parser.error('--photo must be a JPEG file.')
    uri = 'data:image/jpeg;base64,' + base64.b64encode(data).decode('ascii')
    text, count = re.subn(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', lambda _: uri, text)
    if count != 1:
        raise ValueError(f'Expected one portrait; found {count}. No file saved.')
if args.cv:
    data = args.cv.read_bytes()
    if not data.startswith(b'%PDF-'):
        parser.error('--cv must be a PDF file.')
    uri = 'data:application/pdf;base64,' + base64.b64encode(data).decode('ascii')
    text, count = re.subn(r'data:application/pdf;base64,[A-Za-z0-9+/=]+', lambda _: uri, text)
    if count != 2:
        raise ValueError(f'Expected two CV links; found {count}. No file saved.')
args.html.write_text(text, encoding='utf-8')
print(f'Updated {args.html}. Upload it to GitHub to publish the changes.')
