"""LoliCode validator."""

from typing import Dict, List


class ValidationResult:
    """Result of LoliCode validation."""
    
    def __init__(self, is_valid: bool, errors: List[str]):
        self.is_valid = is_valid
        self.errors = errors
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            'is_valid': self.is_valid,
            'errors': self.errors
        }


class LoliCodeValidator:
    """Validator for LoliCode scripts."""
    
    def validate(self, script: str) -> ValidationResult:
        """
        Validate a LoliCode script.
        
        Args:
            script: The LoliCode script to validate
            
        Returns:
            ValidationResult object with validation status and errors
        """
        errors: List[str] = []
        
        # Check if script is empty
        if not script.strip():
            errors.append('Script is empty.')
        
        # Check for undefined values
        if 'undefined' in script:
            errors.append('Script contains "undefined" values.')
        
        # Check for None values
        if 'None' in script:
            errors.append('Script contains "None" values.')
        
        # Additional validation: Check for common syntax errors
        lines = script.split('\n')
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Skip lines that are part of PARSE blocks (they may have regex patterns)
            if 'PARSE' in line or 'REGEX' in line or 'JSON' in line:
                continue
            
            # Check for unmatched quotes (but skip CONTENT lines which may have escaped quotes)
            if 'CONTENT' not in line and stripped.count('"') % 2 != 0:
                errors.append(f'Line {i}: Unmatched quotes')
            
            # Check for empty REQUEST blocks
            if stripped.startswith('REQUEST') and len(stripped) < 10:
                errors.append(f'Line {i}: Empty or invalid REQUEST block')
        
        return ValidationResult(is_valid=len(errors) == 0, errors=errors)
