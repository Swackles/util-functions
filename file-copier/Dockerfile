FROM python:3-alpine

# Install dependencies
RUN python -m pip install -U watchdog

COPY ./main.py ./

CMD ["python", "main.py"]