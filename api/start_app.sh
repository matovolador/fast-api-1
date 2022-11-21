#!/bin/bash
alembic upgrade head || exit 1
coverage run tests.py || exit 1
coverage xml
coverage lcov
coverage html
genbadge coverage -i - < /app/coverage/coverage.xml -o /app/coverage/coverage-badge.svg
python main.py