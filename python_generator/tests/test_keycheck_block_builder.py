"""Tests for KeycheckBlockBuilder."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generator.types import CustomAssertion
from generator.builders.keycheck_block_builder import KeycheckBlockBuilder


class TestKeycheckBlockBuilder:
    """Tests for KeycheckBlockBuilder."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.builder = KeycheckBlockBuilder()
    
    def test_status_assertion_success(self):
        """Test building status assertion with success action."""
        assertion = CustomAssertion(
            type='status',
            value='200',
            action='success'
        )
        
        result = self.builder.build(assertion)
        
        assert result == 'KEYCHECK\n  KEY "<RESPONSE.STATUS>" Equal "200"'
    
    def test_status_assertion_fail(self):
        """Test building status assertion with fail action."""
        assertion = CustomAssertion(
            type='status',
            value='404',
            action='fail'
        )
        
        result = self.builder.build(assertion)
        
        assert 'KEYCHECK FAIL' in result
        assert 'Equal "404"' in result
    
    def test_contains_assertion(self):
        """Test building contains assertion."""
        assertion = CustomAssertion(
            type='contains',
            value='success',
            action='success'
        )
        
        result = self.builder.build(assertion)
        
        assert 'KEYCHECK' in result
        assert 'Contains "success"' in result
        assert '<RESPONSE.BODY>' in result
    
    def test_regex_assertion(self):
        """Test building regex assertion."""
        assertion = CustomAssertion(
            type='regex',
            value=r'\d{4}',
            action='success'
        )
        
        result = self.builder.build(assertion)
        
        assert 'KEYCHECK' in result
        assert 'RegexMatch' in result
        assert r'\d{4}' in result
    
    def test_json_path_assertion(self):
        """Test building JSON path assertion."""
        assertion = CustomAssertion(
            type='json-path',
            value='$.token',
            expected_result='valid',
            action='success'
        )
        
        result = self.builder.build(assertion)
        
        assert 'KEYCHECK' in result
        assert 'JsonPath "$.token"' in result
        assert 'Equal "valid"' in result
    
    def test_retry_action(self):
        """Test building assertion with retry action."""
        assertion = CustomAssertion(
            type='contains',
            value='retry',
            action='retry'
        )
        
        result = self.builder.build(assertion)
        
        assert 'KEYCHECK RETRY' in result
    
    def test_ban_action(self):
        """Test building assertion with ban action."""
        assertion = CustomAssertion(
            type='contains',
            value='banned',
            action='ban'
        )
        
        result = self.builder.build(assertion)
        
        assert 'KEYCHECK BAN' in result
    
    def test_build_status_check_success(self):
        """Test building default status check for success codes."""
        result = self.builder.build_status_check(200)
        
        assert 'KEYCHECK SUCCESS' in result
        assert 'Equal "200"' in result
    
    def test_build_status_check_redirect(self):
        """Test building default status check for redirect codes."""
        result = self.builder.build_status_check(204)
        
        assert 'KEYCHECK SUCCESS' in result
    
    def test_build_status_check_fail(self):
        """Test building default status check for error codes."""
        result = self.builder.build_status_check(404)
        
        assert 'KEYCHECK FAIL' in result
        assert 'Equal "404"' in result
    
    def test_build_status_check_server_error(self):
        """Test building default status check for server error codes."""
        result = self.builder.build_status_check(500)
        
        assert 'KEYCHECK FAIL' in result
        assert 'Equal "500"' in result
