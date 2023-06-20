def apply_operation(text, position, operation):
    op_type = operation['op']
    
    if op_type == 'insert':
        chars = operation['chars']
        return text[:position] + chars + text[position:]
    
    if op_type == 'delete':
        count = operation['count']
        return text[:position] + text[position+count:]
    
    if op_type == 'skip':
        count = operation['count']
        return text[:position+count]
    
    return text


def isValid(stale, latest, otjson):
    operations = json.loads(otjson)
    text = stale
    position = 0

    for operation in operations:
        new_text = apply_operation(text, position, operation)
        
        if new_text != text:
            return False
        
        op_type = operation['op']
        
        if op_type == 'insert':
            position += len(operation['chars'])
        elif op_type == 'delete':
            position = max(0, position - operation['count'])
        elif op_type == 'skip':
            position += operation['count']
        
        text = new_text
    
    return text == latest
