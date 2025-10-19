"""Tests for ParseBlockBuilder."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generator.types import VariableExtraction
from generator.builders.parse_block_builder import ParseBlockBuilder


class TestParseBlockBuilder:
    """Tests for ParseBlockBuilder."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.builder = ParseBlockBuilder()
    
    def test_regex_extraction_global(self):
        """Test building regex extraction with global scope."""
        extraction = VariableExtraction(
            type='regex',
            pattern=r'token=(\w+)',
            variable_name='token',
            is_global=True
        )
        
        result = self.builder.build(extraction)
        
        assert 'PARSE "<RESPONSE.BODY>" REGEX' in result
        assert r'token=(\w+)' in result
        assert 'VAR "token" true' in result
    
    def test_regex_extraction_local(self):
        """Test building regex extraction with local scope."""
        extraction = VariableExtraction(
            type='regex',
            pattern=r'csrf=([^&]+)',
            variable_name='csrf_token',
            is_global=False
        )
        
        result = self.builder.build(extraction)
        
        assert 'PARSE "<RESPONSE.BODY>" REGEX' in result
        assert r'csrf=([^&]+)' in result
        assert 'VAR "csrf_token" false' in result
    
    def test_json_extraction(self):
        """Test building JSON extraction."""
        extraction = VariableExtraction(
            type='json',
            pattern='$.data.token',
            variable_name='auth_token',
            is_global=True
        )
        
        result = self.builder.build(extraction)
        
        assert 'PARSE "<RESPONSE.BODY>" JSON' in result
        assert '$.data.token' in result
        assert 'VAR "auth_token" true' in result
    
    def test_css_extraction(self):
        """Test building CSS selector extraction."""
        extraction = VariableExtraction(
            type='css',
            pattern='input[name="csrf"]',
            variable_name='csrf',
            is_global=False
        )
        
        result = self.builder.build(extraction)
        
        assert 'PARSE "<RESPONSE.BODY>" CSS' in result
        assert 'input[name="csrf"]' in result
        assert 'VAR "csrf" false' in result
    
    def test_xpath_extraction(self):
        """Test building XPath extraction."""
        extraction = VariableExtraction(
            type='xpath',
            pattern='//input[@name="token"]/@value',
            variable_name='form_token',
            is_global=True
        )
        
        result = self.builder.build(extraction)
        
        assert 'PARSE "<RESPONSE.BODY>" XPATH' in result
        assert '//input[@name="token"]/@value' in result
        assert 'VAR "form_token" true' in result
    
    def test_complex_pattern(self):
        """Test building extraction with complex pattern."""
        extraction = VariableExtraction(
            type='regex',
            pattern=r'<input[^>]+name="authenticity_token"[^>]+value="([^"]+)"',
            variable_name='authenticity_token',
            is_global=False
        )
        
        result = self.builder.build(extraction)
        
        assert 'REGEX' in result
        assert 'authenticity_token' in result
        assert 'false' in result
