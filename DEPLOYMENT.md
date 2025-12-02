# ChartGPT Deployment Guide

## Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chartgpt-qa-system.git
cd chartgpt-qa-system
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the system:
```bash
python chart_main.py
```

## Requirements

- Python 3.8 or higher
- pip package manager
- ~5MB disk space
- No external API dependencies

## Installation Methods

### Method 1: From Source

```bash
git clone https://github.com/yourusername/chartgpt-qa-system.git
cd chartgpt-qa-system
pip install -r requirements.txt
```

### Method 2: Docker (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "chart_main.py"]
```

Build and run:
```bash
docker build -t chartgpt .
docker run -it chartgpt
```

## Configuration

### Environment Variables

Optional configuration:
```bash
export CHARTGPT_DEBUG=true       # Enable debug mode
export CHARTGPT_LOG_LEVEL=INFO   # Logging level
```

### Customization

Modify chart data in `chart_knowledge_base.py`:
- Add new charts to the CHARTS list
- Update scoring weights in `chart_qa_engine.py`

## Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest test_chart_knowledge_base.py

# Generate coverage report
python -m pytest --cov=. --cov-report=html
```

## Production Deployment

### Gunicorn Server

Create a WSGI wrapper:

```python
# app.py
from chart_main import ChartGPTInterface

interface = ChartGPTInterface()

def application(environ, start_response):
    # WSGI application
    pass
```

### Systemd Service

Create `/etc/systemd/system/chartgpt.service`:

```ini
[Unit]
Description=ChartGPT Service
After=network.target

[Service]
Type=simple
User=chartgpt
ExecStart=/path/to/venv/bin/python /path/to/chart_main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Health Checks

Test the deployment:

```bash
# Check installation
python -c "from chart_knowledge_base import ChartKnowledgeBase; print('OK')"

# Run quick test
python -m pytest --co -q
```

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Python version error
**Solution:** Ensure Python 3.8+:
```bash
python --version
```

### Issue: Permission denied
**Solution:** Check file permissions:
```bash
chmod +x chart_main.py
```

## Performance Optimization

1. **Memory:** Load charts once at startup
2. **Caching:** Cache frequent query results
3. **Indexing:** Add indexing for large datasets

## Security

- Validate all user input
- Use error handling for edge cases
- Never expose internal errors
- Keep dependencies updated

## Monitoring

Track:
- Query response times
- Error rates
- System resource usage
- User query patterns

## Backup & Recovery

- Version control all code changes
- Document configuration changes
- Keep dependency snapshot

## Scaling

For larger deployments:
1. Use load balancer
2. Add caching layer
3. Database for chart data
4. API service wrapper

---

**Last Updated:** December 2, 2025
