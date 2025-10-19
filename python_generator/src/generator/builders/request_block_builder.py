"""Request block builder for LoliCode generation."""

from typing import List, Optional
from ..types import SemanticHarEntry, CustomHeader


class RequestBlockBuilder:
    """Builder for REQUEST blocks in LoliCode."""
    
    def build(self, entry: SemanticHarEntry, custom_headers: Optional[List[CustomHeader]] = None) -> str:
        """
        Build a REQUEST block from a HAR entry.
        
        Args:
            entry: The HAR entry to convert
            custom_headers: Optional list of custom headers to add
            
        Returns:
            The generated REQUEST block as a string
        """
        lines: List[str] = []
        request = entry.request
        
        # Build REQUEST line
        content = f'"{request.url}"'
        if request.method != 'GET':
            content += f' {request.method}'
        lines.append(f'REQUEST {content}')
        
        # Add default User-Agent
        lines.append('  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"')
        
        # Merge custom headers if provided
        headers = dict(request.headers)
        if custom_headers:
            for h in custom_headers:
                if h.enabled:
                    headers[h.key.lower()] = h.value
        
        # Add headers (skip some default ones)
        skip_headers = ['user-agent', 'cookie', 'content-length']
        for key, value in headers.items():
            if key.lower() not in skip_headers:
                lines.append(f'  "{key}: {value}"')
        
        # Add cookies if present
        if request.cookies:
            cookie_string = '; '.join(f'{k}={v}' for k, v in request.cookies.items())
            lines.append(f'  "Cookie: {cookie_string}"')
        
        # Add body if present
        if request.body:
            # Escape quotes in body content
            body = request.body.data.replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'  CONTENT "{body}"')
            content_type = 'application/json' if request.body.content_type == 'json' else 'application/x-www-form-urlencoded'
            lines.append(f'  "Content-Type: {content_type}"')
        
        return '\n'.join(lines)
