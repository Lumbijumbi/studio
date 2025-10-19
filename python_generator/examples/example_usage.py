"""Example usage of the LoliCode generator."""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generator import (
    LoliCodeGenerator,
    LoliCodeConfig,
    SemanticHarEntry,
    SemanticHarRequest,
    SemanticHarResponse,
    RequestBody,
    DependencyMatrix,
    CustomHeader,
    CustomAssertion,
    VariableExtraction,
)


async def example_basic():
    """Basic example with a simple GET request."""
    print("=" * 70)
    print("EXAMPLE 1: Basic GET Request")
    print("=" * 70)
    
    # Create a simple HAR entry
    entry = SemanticHarEntry(
        request=SemanticHarRequest(
            url='https://api.example.com/users',
            method='GET',
            headers={'accept': 'application/json'},
            cookies={}
        ),
        response=SemanticHarResponse(status=200)
    )
    
    # Create configuration
    config = LoliCodeConfig(
        selected_indices=[0],
        settings={
            'use_proxy': True,
            'timeout': 30
        }
    )
    
    # Create dependency matrix
    dependency_matrix = DependencyMatrix(topological_order=[0])
    
    # Generate script
    generator = LoliCodeGenerator()
    script = await generator.generate(config, [entry], dependency_matrix)
    
    print(script)
    print()


async def example_login_flow():
    """Example with a login flow including POST request."""
    print("=" * 70)
    print("EXAMPLE 2: Login Flow with Token Extraction")
    print("=" * 70)
    
    # Create HAR entries for login flow
    entries = [
        # Get login page (to extract CSRF token)
        SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/login',
                method='GET',
                headers={'accept': 'text/html'},
                cookies={}
            ),
            response=SemanticHarResponse(status=200)
        ),
        # Submit login
        SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/auth/login',
                method='POST',
                headers={'content-type': 'application/json'},
                cookies={},
                body=RequestBody(
                    data='{"username":"<INPUT.USERNAME>","password":"<INPUT.PASSWORD>","csrf":"<csrf_token>"}',
                    content_type='json'
                )
            ),
            response=SemanticHarResponse(status=200)
        ),
        # Access protected resource
        SemanticHarEntry(
            request=SemanticHarRequest(
                url='https://example.com/api/profile',
                method='GET',
                headers={'authorization': 'Bearer <auth_token>'},
                cookies={'session': 'abc123'}
            ),
            response=SemanticHarResponse(status=200)
        )
    ]
    
    # Create configuration with extractions and assertions
    config = LoliCodeConfig(
        selected_indices=[0, 1, 2],
        settings={
            'use_proxy': True,
            'follow_redirects': True,
            'timeout': 30
        },
        variable_extractions={
            0: [
                VariableExtraction(
                    type='regex',
                    pattern=r'name="csrf_token" value="([^"]+)"',
                    variable_name='csrf_token',
                    is_global=True
                )
            ],
            1: [
                VariableExtraction(
                    type='json',
                    pattern='$.token',
                    variable_name='auth_token',
                    is_global=True
                )
            ]
        },
        custom_assertions={
            1: [
                CustomAssertion(
                    type='contains',
                    value='success',
                    action='success'
                )
            ],
            2: [
                CustomAssertion(
                    type='status',
                    value='200',
                    action='success'
                )
            ]
        }
    )
    
    # Create dependency matrix (login page -> login -> profile)
    dependency_matrix = DependencyMatrix(topological_order=[0, 1, 2])
    
    # Generate script
    generator = LoliCodeGenerator()
    script = await generator.generate(config, entries, dependency_matrix)
    
    print(script)
    print()


async def example_advanced():
    """Advanced example with custom headers and multiple assertions."""
    print("=" * 70)
    print("EXAMPLE 3: Advanced Configuration")
    print("=" * 70)
    
    entry = SemanticHarEntry(
        request=SemanticHarRequest(
            url='https://api.example.com/search',
            method='POST',
            headers={'content-type': 'application/json'},
            cookies={},
            body=RequestBody(
                data='{"query":"test","limit":10}',
                content_type='json'
            )
        ),
        response=SemanticHarResponse(status=200)
    )
    
    config = LoliCodeConfig(
        selected_indices=[0],
        custom_headers={
            0: [
                CustomHeader(key='X-API-Key', value='secret-key-123', enabled=True),
                CustomHeader(key='X-Request-ID', value='<uuid>', enabled=True)
            ]
        },
        custom_assertions={
            0: [
                CustomAssertion(
                    type='regex',
                    value=r'"results":\s*\[',
                    action='success'
                ),
                CustomAssertion(
                    type='json-path',
                    value='$.success',
                    expected_result='true',
                    action='success'
                )
            ]
        },
        variable_extractions={
            0: [
                VariableExtraction(
                    type='json',
                    pattern='$.results[0].id',
                    variable_name='first_result_id',
                    is_global=False
                )
            ]
        },
        settings={
            'use_proxy': False,
            'timeout': 60,
            'retry_count': 3
        }
    )
    
    dependency_matrix = DependencyMatrix(topological_order=[0])
    
    generator = LoliCodeGenerator()
    script = await generator.generate(config, [entry], dependency_matrix)
    
    print(script)
    print()


async def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("LoliCode Generator - Python Implementation Examples")
    print("=" * 70 + "\n")
    
    await example_basic()
    await example_login_flow()
    await example_advanced()
    
    print("=" * 70)
    print("All examples completed successfully!")
    print("=" * 70)


if __name__ == '__main__':
    asyncio.run(main())
