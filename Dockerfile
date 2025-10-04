FROM python:3.13-slim

WORKDIR /

COPY sistema_faculdade.py .

CMD ["python", "sistema_faculdade.py"]