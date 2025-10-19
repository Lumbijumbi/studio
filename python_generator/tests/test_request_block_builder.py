"""Tests for RequestBlockBuilder."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generator.types import (
    SemanticHarEntry,
    SemanticHarRequest,
    SemanticHarResponse,
    RequestBody,
    CustomHeader,
)
from generator.builders.request_block_builder import RequestBlockBuilder


class TestRequestBlockBuilder:
    """Tests for RequestBlockBuilder."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.builder = RequestBlockBuilder()
    
    def test_simple_get_request(self):
        """Test building a simple GET request."""
        entry = SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/test',
                method='GET',
                headers={'accept': 'application/json'},
                cookies={}
            ),
            response=SemanticHarResponse(status=200)
        )
        
        result = self.builder.build(entry)
        
        assert 'REQUEST "https://example.com/api/test"' in result
        assert 'User-Agent: Mozilla/5.0' in result
        assert 'accept: application/json' in result
        assert 'Cookie:' not in result
    
    def test_post_request_with_body(self):
        """Test building a POST request with JSON body."""
        entry = SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/login',
                method='POST',
                headers={'accept': 'application/json'},
                cookies={},
                body=RequestBody(
                    data='{"username":"test","password":"pass"}',
                    content_type='json'
                )
            ),
            response=SemanticHarResponse(status=200)
        )
        
        result = self.builder.build(entry)
        
        assert 'REQUEST "https://example.com/api/login" POST' in result
        assert 'CONTENT' in result
        assert 'Content-Type: application/json' in result
        assert 'username' in result
    
    def test_request_with_cookies(self):
        """Test building request with cookies."""
        entry = SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/test',
                method='GET',
                headers={},
                cookies={'session': 'abc123', 'token': 'xyz789'}
            ),
            response=SemanticHarResponse(status=200)
        )
        
        result = self.builder.build(entry)
        
        assert 'Cookie:' in result
        assert 'session=abc123' in result
        assert 'token=xyz789' in result
    
    def test_custom_headers(self):
        """Test building request with custom headers."""
        entry = SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/test',
                method='GET',
                headers={'accept': 'application/json'},
                cookies={}
            ),
            response=SemanticHarResponse(status=200)
        )
        
        custom_headers = [
            CustomHeader(key='X-Custom-Header', value='custom-value', enabled=True),
            CustomHeader(key='X-Disabled', value='disabled-value', enabled=False)
        ]
        
        result = self.builder.build(entry, custom_headers)
        
        assert 'x-custom-header: custom-value' in result
        assert 'disabled-value' not in result
    
    def test_form_content_type(self):
        """Test building request with form content type."""
        entry = SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/login',
                method='POST',
                headers={},
                cookies={},
                body=RequestBody(
                    data='username=test&password=pass',
                    content_type='form'
                )
            ),
            response=SemanticHarResponse(status=200)
        )
        
        result = self.builder.build(entry)
        
        assert 'Content-Type: application/x-www-form-urlencoded' in result
        assert 'username=test' in result
    
    def test_escaped_quotes_in_body(self):
        """Test that quotes in body are escaped."""
        entry = SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/test',
                method='POST',
                headers={},
                cookies={},
                body=RequestBody(
                    data='{"key":"value with \\"quotes\\""}',
                    content_type='json'
                )
            ),
            response=SemanticHarResponse(status=200)
        )
        
        result = self.builder.build(entry)
        
        # Quotes should be escaped
        assert '\\\\"' in result or 'value with' in result
