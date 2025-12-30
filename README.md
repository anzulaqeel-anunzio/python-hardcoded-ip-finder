# Hardcoded IP Address Finder

A security checking tool that scans source code for hardcoded IPv4 addresses.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Recursive Scanning**: Checks all common code files (`.py`, `.js`, `.java`, etc.).
*   **Intelligent Filtering**: Ignores invalid IPs (like `999.999.999.999`) and localhost (`127.0.0.1`, `0.0.0.0`).
*   **Zero Dependencies**: Pure Python.

## Usage

```bash
python run_finder.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_finder.py src/
```

**2. Check Config File**
```bash
python run_finder.py config.json
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
