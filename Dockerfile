FROM python:3.11-slim

WORKDIR /app

# Create the kaggle config directory
RUN mkdir -p /app/kaggle
RUN mkdir -p "/nonexistent/.kaggle/logs"

ARG MIGRATION_DB_URL

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=Mageiras.settings \
    PORT=8000 \
    WEB_CONCURRENCY=2 \
    KAGGLE_CONFIG_DIR=/app/kaggle

# Install system packages required Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project code
COPY . .

RUN #python manage.py collectstatic --noinput --clear

# Run as non-root user
RUN chown -R django:django /app
USER django

# Run application
# CMD gunicorn project_name.wsgi:application
CMD ["gunicorn", "Mageiras.wsgi"]