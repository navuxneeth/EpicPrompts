#!/usr/bin/env python3
"""
EpicPrompts Validation Tool
Validates JSON prompt files for consistency and correctness.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

def validate_json_syntax(file_path: str) -> tuple[bool, str]:
    """Validate JSON syntax."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, "Valid JSON syntax"
    except json.JSONDecodeError as e:
        return False, f"JSON syntax error: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"

def validate_prompt_structure(data: Dict[str, Any], file_path: str) -> List[str]:
    """Validate prompt structure and required fields."""
    issues = []
    
    # Check for recommended top-level fields
    recommended_fields = ['task', 'description', 'parameters']
    for field in recommended_fields:
        if field not in data:
            issues.append(f"Missing recommended field: '{field}'")
    
    # Validate task field
    if 'task' in data:
        if not isinstance(data['task'], str) or len(data['task'].strip()) == 0:
            issues.append("Field 'task' should be a non-empty string")
    
    # Check for overly long strings that might indicate formatting issues
    def check_string_lengths(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                check_string_lengths(value, new_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                new_path = f"{path}[{i}]"
                check_string_lengths(item, new_path)
        elif isinstance(obj, str) and len(obj) > 1000:
            issues.append(f"Very long string at {path} ({len(obj)} chars) - consider breaking into smaller parts")
    
    check_string_lengths(data)
    
    return issues

def validate_file_naming(file_path: str) -> List[str]:
    """Validate file naming conventions."""
    issues = []
    
    file_name = os.path.basename(file_path)
    dir_name = os.path.basename(os.path.dirname(file_path))
    
    # Check if file follows naming convention (XXX_V#.json)
    if not file_name.endswith('.json'):
        return issues  # Not a JSON file, skip naming validation
    
    name_without_ext = file_name[:-5]  # Remove .json
    if '_V' not in name_without_ext:
        issues.append(f"File name should follow pattern 'ACRONYM_V#.json', got '{file_name}'")
    else:
        parts = name_without_ext.split('_V')
        if len(parts) != 2:
            issues.append(f"File name should have exactly one '_V' separator, got '{file_name}'")
        else:
            acronym, version = parts
            if not version.isdigit():
                issues.append(f"Version should be numeric, got 'V{version}' in '{file_name}'")
            if len(acronym) < 2:
                issues.append(f"Acronym should be at least 2 characters, got '{acronym}' in '{file_name}'")
    
    return issues

def validate_directory_structure(base_path: str) -> List[str]:
    """Validate overall directory structure."""
    issues = []
    
    # Check for YAML versions consistency
    json_dirs = set()
    yaml_dirs = set()
    
    # Find all JSON directories
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item not in ['.git', '.github', 'YAML-versions']:
            json_dirs.add(item)
    
    # Check YAML-versions directory
    yaml_versions_path = os.path.join(base_path, 'YAML-versions')
    if os.path.exists(yaml_versions_path):
        for item in os.listdir(yaml_versions_path):
            item_path = os.path.join(yaml_versions_path, item)
            if os.path.isdir(item_path):
                yaml_dirs.add(item)
    
    # Check for missing YAML versions
    missing_yaml = json_dirs - yaml_dirs
    if missing_yaml:
        issues.append(f"Missing YAML versions for directories: {', '.join(missing_yaml)}")
    
    # Check for orphaned YAML directories
    orphaned_yaml = yaml_dirs - json_dirs
    if orphaned_yaml:
        issues.append(f"YAML directories without corresponding JSON directories: {', '.join(orphaned_yaml)}")
    
    return issues

def main():
    """Main validation function."""
    base_path = os.getcwd()
    all_issues = []
    
    print("🔍 EpicPrompts Validation Tool")
    print("=" * 50)
    
    # Validate directory structure
    print("\n📁 Checking directory structure...")
    structure_issues = validate_directory_structure(base_path)
    if structure_issues:
        all_issues.extend([f"STRUCTURE: {issue}" for issue in structure_issues])
        for issue in structure_issues:
            print(f"  ❌ {issue}")
    else:
        print("  ✅ Directory structure looks good")
    
    # Find all JSON files to validate
    json_files = []
    for root, dirs, files in os.walk(base_path):
        # Skip .git and other system directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    
    if not json_files:
        print("\n⚠️  No JSON files found to validate")
        return
    
    print(f"\n📋 Found {len(json_files)} JSON files to validate")
    print("-" * 30)
    
    # Validate each JSON file
    for file_path in json_files:
        relative_path = os.path.relpath(file_path, base_path)
        print(f"\n🔎 Validating: {relative_path}")
        
        # Check JSON syntax
        is_valid_json, json_message = validate_json_syntax(file_path)
        if not is_valid_json:
            print(f"  ❌ {json_message}")
            all_issues.append(f"{relative_path}: {json_message}")
            continue
        else:
            print(f"  ✅ {json_message}")
        
        # Load and validate structure
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        structure_issues = validate_prompt_structure(data, relative_path)
        naming_issues = validate_file_naming(file_path)
        
        file_issues = structure_issues + naming_issues
        
        if file_issues:
            for issue in file_issues:
                print(f"  ⚠️  {issue}")
                all_issues.append(f"{relative_path}: {issue}")
        else:
            print("  ✅ Structure and naming look good")
    
    # Summary
    print("\n" + "=" * 50)
    if all_issues:
        print(f"🚨 Found {len(all_issues)} issues:")
        print("\nSUMMARY:")
        for issue in all_issues:
            print(f"  • {issue}")
        
        print(f"\n💡 See CONTRIBUTING.md for guidelines on prompt structure and naming.")
        sys.exit(1)
    else:
        print("🎉 All validations passed!")
        print("✨ Your prompts look great!")

if __name__ == "__main__":
    main()