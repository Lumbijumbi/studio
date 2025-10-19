"""Parse block builder for LoliCode generation."""

from ..types import VariableExtraction


class ParseBlockBuilder:
    """Builder for PARSE blocks in LoliCode."""
    
    def build(self, extraction: VariableExtraction) -> str:
        """
        Build a PARSE block from a variable extraction configuration.
        
        Args:
            extraction: The variable extraction configuration
            
        Returns:
            The generated PARSE block as a string
        """
        is_global = 'true' if extraction.is_global else 'false'
        var_name = f'"{extraction.variable_name}"'
        pattern = f'"{extraction.pattern}"'
        
        if extraction.type == 'regex':
            return f'PARSE "<RESPONSE.BODY>" REGEX {pattern} -> VAR {var_name} {is_global}'
        elif extraction.type == 'json':
            return f'PARSE "<RESPONSE.BODY>" JSON {pattern} -> VAR {var_name} {is_global}'
        elif extraction.type == 'css':
            return f'PARSE "<RESPONSE.BODY>" CSS {pattern} -> VAR {var_name} {is_global}'
        elif extraction.type == 'xpath':
            return f'PARSE "<RESPONSE.BODY>" XPATH {pattern} -> VAR {var_name} {is_global}'
        else:
            return ''
