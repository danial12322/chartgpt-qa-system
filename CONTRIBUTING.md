# Contributing to ChartGPT

Thank you for your interest in contributing to ChartGPT! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read and adhere to our Code of Conduct:

- Be respectful and inclusive
- Welcome diverse perspectives and experiences
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Provide a clear and descriptive title
3. Include steps to reproduce the issue
4. Describe the expected behavior
5. Include screenshots or error messages if applicable
6. Specify your environment (Python version, OS, etc.)

### Suggesting Enhancements

1. Use a clear and descriptive title
2. Provide a step-by-step description of the suggested enhancement
3. Explain why this enhancement would be useful
4. List some examples of how this enhancement would be used

### Creating Pull Requests

#### Before Starting

1. Fork the repository
2. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
3. Make sure you have Python 3.8+ installed
4. Install dependencies: `pip install -r requirements.txt`

#### Making Changes

1. Follow the existing code style and conventions
2. Write clear and descriptive commit messages
3. Add or update docstrings for any new functions
4. Include type hints for function parameters and return values
5. Write unit tests for new functionality
6. Ensure all tests pass: `python -m pytest`

#### Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add comments for complex logic
- Keep functions focused and single-purpose
- Maximum line length: 100 characters

#### Documentation

- Update README.md if adding new features
- Update EXAMPLES.md with usage examples
- Add docstrings to all public functions
- Include type hints
- Update ARCHITECTURE.md if changing system design

#### Testing

- Write tests for all new functionality
- Ensure test coverage remains above 80%
- Test edge cases and error conditions
- Run tests locally before submitting PR

### Commit Message Guidelines

Use clear and descriptive commit messages:

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `style`: Code style changes

**Examples:**

```
feat: add support for new chart type (Sankey)

Adds Sankey diagram support with proper use cases and library recommendations.

Closes #123
```

```
fix: resolve scoring algorithm issue

The ranking algorithm was not properly weighing use case matches.
Now gives appropriate priority to use case relevance.

Fixes #456
```

## Development Workflow

### Setting Up Development Environment

1. Clone the repository: `git clone https://github.com/yourusername/chartgpt-qa-system.git`
2. Navigate to directory: `cd chartgpt-qa-system`
3. Create virtual environment: `python -m venv venv`
4. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest test_chart_knowledge_base.py

# Run with coverage
python -m pytest --cov=. --cov-report=html
```

### Testing Your Changes

```bash
# Run the interactive interface
python chart_main.py

# Test a specific query
# Type your question and verify the response
```

## Pull Request Process

1. Update documentation as needed
2. Add tests for new functionality
3. Ensure all tests pass locally
4. Submit pull request with clear description
5. Reference any related issues
6. Wait for review and feedback
7. Make requested changes
8. Once approved, maintainers will merge

## Areas for Contribution

### Adding New Charts

1. Research and document the new chart type
2. Add entry to `CHARTS` list in `chart_knowledge_base.py`
3. Include all required metadata fields
4. Write tests for the new chart
5. Update documentation with examples

### Improving Chart Analysis

1. Analyze current scoring algorithm
2. Identify improvement opportunities
3. Implement changes with tests
4. Document the improvements
5. Provide benchmark results

### Enhancing User Interface

1. Improve command-line interface
2. Add new interaction modes
3. Enhance output formatting
4. Add color support
5. Implement help system

### Documentation

1. Improve existing documentation
2. Add more examples
3. Create tutorials
4. Translate documentation
5. Create video guides

## Questions?

Feel free to open an issue for questions or discussions about the project.

## License

By contributing, you agree that your contributions will be licensed under the same license as ChartGPT.

---

**Thank you for contributing to ChartGPT!**

Your contributions help make this project better for everyone.

*Last Updated: December 2, 2025*
