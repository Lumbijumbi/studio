"""Keycheck block builder for LoliCode generation."""

from ..types import CustomAssertion


class KeycheckBlockBuilder:
    """Builder for KEYCHECK blocks in LoliCode."""
    
    def build(self, assertion: CustomAssertion) -> str:
        """
        Build a KEYCHECK block from an assertion.
        
        Args:
            assertion: The assertion configuration
            
        Returns:
            The generated KEYCHECK block as a string
        """
        block = 'KEYCHECK'
        if assertion.action != 'success':
            block += f' {assertion.action.upper()}'
        
        if assertion.type == 'status':
            return f'{block}\n  KEY "<RESPONSE.STATUS>" Equal "{assertion.value}"'
        elif assertion.type == 'contains':
            return f'{block}\n  KEY "<RESPONSE.BODY>" Contains "{assertion.value}"'
        elif assertion.type == 'regex':
            return f'{block}\n  KEY "<RESPONSE.BODY>" RegexMatch "{assertion.value}"'
        elif assertion.type == 'json-path':
            return f'{block}\n  KEY "<RESPONSE.BODY>" JsonPath "{assertion.value}" Equal "{assertion.expected_result}"'
        else:
            return ''
    
    def build_status_check(self, status: int) -> str:
        """
        Build a default status check KEYCHECK block.
        
        Args:
            status: The HTTP status code to check
            
        Returns:
            The generated KEYCHECK block as a string
        """
        check_type = 'SUCCESS' if 200 <= status < 300 else 'FAIL'
        return f'KEYCHECK {check_type}\n  KEY "<RESPONSE.STATUS>" Equal "{status}"'
