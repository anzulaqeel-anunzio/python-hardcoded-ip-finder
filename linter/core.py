# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class IpFinder:
    # IPv4 regex
    # Matches 0-255.0-255.0-255.0-255
    # Simplified regex for detection:
    IPV4_PATTERN = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    @staticmethod
    def is_valid_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit(): return False
            if not 0 <= int(part) <= 255: return False
        return True

    @staticmethod
    def is_ignored_ip(ip):
        # Ignore localhost and 0.0.0.0 often valid in config
        return ip.startswith('127.0.0.1') or ip == '0.0.0.0' or ip.startswith('255.255')

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    # Skip comments logic? Too complex for generic.
                    # Just find matches
                    matches = IpFinder.IPV4_PATTERN.findall(line)
                    for ip in matches:
                        if IpFinder.is_valid_ip(ip) and not IpFinder.is_ignored_ip(ip):
                             issues.append({
                                'line': line_num,
                                'file': filepath,
                                'ip': ip,
                                'msg': 'Potential hardcoded IP address'
                            })
        except Exception:
            # Ignore binary files or read errors
            pass
            
        return issues

    @staticmethod
    def scan_directory(directory, extensions=None):
        if extensions is None:
            # Default to checking code files
            extensions = ['.py', '.js', '.ts', '.java', '.c', '.cpp', '.php', '.go', '.rb', '.yml', '.yaml', '.json', '.env']
            
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    path = os.path.join(root, file)
                    issues = IpFinder.scan_file(path)
                    all_issues.extend(issues)
                    
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
